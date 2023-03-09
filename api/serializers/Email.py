import os

import openai
from rest_framework.serializers import CharField, ModelSerializer

from api.models import Email

openai.api_key = os.environ.get("OPENAI_API_KEY")


class EmailSerializer(ModelSerializer):
    label_id = CharField(max_length=100, required=False)
    body = CharField(required=False)
    subject = CharField(max_length=255, required=False)
    sender = CharField(max_length=255, required=False)
    headline = CharField(max_length=255, required=False)
    source = CharField(required=False)
    sub_action = CharField(required=False)

    class Meta:
        model = Email
        fields = ['id', 'email_id', 'body', 'user', 'created_at', 'subject', 'sender', 'source', 'label_id', 'headline', 'sub_action']
        read_only_fields = ['id', 'user', 'created_at']

    def create(self, validated_data):
        user = self.context["request"].user
        # todo move it to open_ai_client
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="génère le texte d'une réponse de "
            + validated_data["user"]
            + " à cette conversation d'emails : "
            + validated_data["source"],
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        validated_data["body"] = response["choices"][0]["text"]
        return super().create(user=user, **validated_data)
