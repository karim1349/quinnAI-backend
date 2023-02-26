from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Email
from api.open_ai_client import (
    classify_email,
    headlines_generation,
    orthograph_correction,
    response_generation,
    score_email,
)
from api.serializers import EmailSerializer
from api.services import set_email_label
from utils.parser import parse_email_content_html


class EmailViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["post"])
    def predict_label(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        suggestions = classify_email(data["subject"], data["sender"])
        return Response({"suggestions": suggestions}, status=200)

    @action(detail=False, methods=["post"])
    def orthographe(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            correction = orthograph_correction(data['source'])
            return Response({'body': correction})
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)

    @action(detail=False, methods=["post"])
    def set_label(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        try:
            predicted_label = set_email_label(request.user, data['email_id'], data['label_id'])

            return Response(predicted_label)
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)

    @csrf_exempt
    @action(detail=False, methods=['post'])
    def generate_headlines(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        source = parse_email_content_html(data['source'])
        print("source =  " + source)
        try:
            correction = headlines_generation(data['sender'], source)
            return Response({'body': correction})
        except (ValueError, TypeError):
            return Response({'error': 'An error has occured.'}, status=400)

    @action(detail=False, methods=['post'])
    @csrf_exempt
    def generate_responses(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            correction = response_generation(data['sender'], data['source'], data['headline'])
            return Response({'body': correction})
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)

    @action(detail=False, methods=["post"])
    @csrf_exempt
    def predict_email_score(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            score = score_email(data["subject"], data["sender"])
            return Response({"score": score})
        except (ValueError, TypeError) as ex:
            return Response({"error": f"An error has occured.{ex}"}, status=400)
