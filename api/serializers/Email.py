import os

import openai
from rest_framework.serializers import CharField, ModelSerializer

from api.models import Email

openai.api_key = os.environ.get("OPENAI_API_KEY")


class EmailSerializer(ModelSerializer):
    label_id = CharField(max_length=100, required=False)

    class Meta:
        model = Email
        fields = ['id', 'email_id', 'body', 'user', 'created_at', 'subject', 'sender', 'source', 'labels', 'label_id', 'headline']
        read_only_fields = ['id', 'user', 'created_at', 'labels']

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
