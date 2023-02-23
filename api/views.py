from rest_framework.viewsets import ModelViewSet

from api.open_ai_client import classify_email, orthograph_correction, headlines_generation
from api.serializers import EmailSerializer
from api.models import Email
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt


class EmailViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post'])
    def predict_label(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        suggestions = classify_email(data["subject"], data["sender"])
        return Response({'suggestions': suggestions}, status=200)

    @action(detail=False, methods=['post'])
    def orthographe(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            correction = orthograph_correction(data['source'])
            return Response({'body': correction})
        except (ValueError, TypeError):
            return Response({'error': 'An error has occured.'}, status=400)

    @action(detail=False, methods=['post'])
    @csrf_exempt
    def headlines(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            correction = headlines_generation(data['source'])
            return Response({'body': correction})
        except (ValueError, TypeError):
            return Response({'error': 'An error has occured.'}, status=400)