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
        model="text-davinci-003",
        prompt="generate an answer for this email : " + validated_data['source'],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        validated_data['body'] = response['choices'][0]['text']
        return super().create(validated_data)