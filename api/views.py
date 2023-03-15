from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Email, Label
from api.open_ai_client import (classify_email, headlines_generation,
                                orthograph_correction, response_generation,
                                score_email, conversation_summary, translate, meliorate, change_tone, detect_actions, redact_answer)
from api.serializers import EmailSerializer, LabelSerializer
from api.services import set_email_label
from api.tasks import task_creating_user_labels, scoring_emails_of_user
from utils.parser import parse_email_content_html


class EmailViewSet(ModelViewSet):
    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        #return Email.objects.filter(user=self.request.user)
        return Email.objects.all()

    @property
    def user(self):
        return self.request.user

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["post"],permission_classes=[AllowAny])
    def predict_label(self, request, *args, **kwargs):
        """
        need only email id
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        suggestions = classify_email(data["subject"], data["sender"])
        return Response({"suggestions": suggestions}, status=200)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def orthographe(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            correction = orthograph_correction(data['source'])
            return Response({'body': correction})
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def set_label(self, request, *args, **kwargs):
        """
            need only email id
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        try:
            predicted_label = set_email_label(request.user, data['email_id'], data['label_id'])

            return Response(predicted_label)
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)

    @csrf_exempt
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def generate_headlines(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        #source = parse_email_content_html(data['source'])
        #print("source =  " + source)
        try:
            correction = headlines_generation(data['sender'], data['source'])
            return Response({'body': correction})
        except (ValueError, TypeError):
            return Response({'error': 'An error has occured.'}, status=400)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
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
        
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    @csrf_exempt
    def summarize_conversation(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            summary = conversation_summary(data['source'], data['sub_action'])
            return Response({'body': summary})
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    @csrf_exempt
    def translate_email(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            translation = translate(data['source'], data['sub_action'])
            return Response({'body': translation})
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)
    
    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    @csrf_exempt
    def meliorate_email(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            melioration = meliorate(data['source'], data['sub_action'])
            return Response({'body': melioration})
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    @csrf_exempt
    def change_tone_email(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            tone = change_tone(data['source'], data['sub_action'])
            return Response({'body': tone})
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)
    
    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    @csrf_exempt
    def detect_actions_email(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            actions = detect_actions(data['source'])
            return Response({'body': actions})
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)
    
    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    @csrf_exempt
    def redact_answer_email(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        print(data)
        try:
            redaction = redact_answer(data['source'], data['sender'])
            return Response({'body': redaction})
        except (ValueError, TypeError):
            return Response({"error": "An error has occured."}, status=400)
        
    @action(detail=False, methods=["post"])
    @csrf_exempt
    def predict_email_score(self, request, *args, **kwargs):
        """
        need only email id
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            score = score_email(data["subject"], data["sender"], data['body'])
            return Response({"score": score})
        except (ValueError, TypeError) as ex:
            return Response({"error": f"An error has occured.{ex}"}, status=400)

    @action(detail=False, methods=["get"])
    @csrf_exempt
    def predict_multiple_emails_score(self, request, *args, **kwargs):

        try:
            scoring_emails_of_user.delay(self.request.user.pk, max_results=10)
            return Response({"score": "success"})
        except (ValueError, TypeError) as ex:
            return Response({"error": f"An error has occured.{ex}"}, status=400)


class LabelViewSet(ModelViewSet):

    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    @action(detail=False, methods=["post"])
    @csrf_exempt
    def create_labels(self, request, *args, **kwargs):
        """
        we must add permissions
        """

        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        task_creating_user_labels.delay(request.user.pk, data)
        return Response({"message":"labels created"}, status=status.HTTP_201_CREATED)
