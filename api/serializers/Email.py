from rest_framework.serializers import ModelSerializer
from api.models import Email
import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

class EmailSerializer(ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

    def create(self, validated_data):

        response = openai.Completion.create(
        model="text-ada-001",
        prompt="generate an answer for this email : " + validated_data['source'],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )

        for chunk in response:
            if chunk['object'] == 'text':
                validated_data['body'] = chunk['text']
                break
        return super().create(validated_data)