
from rest_framework.viewsets import ModelViewSet

from api.open_ai_client import classify_email
from api.serializers import EmailSerializer
from api.models import Email
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


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
