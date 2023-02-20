from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai

@api_view(['POST'])
def orthographe(request):
    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="renvoie moi ce texte sans les potentielles fautes d'orthographes : \"" + request.data['source'] + "\"",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return Response({'body': response['choices'][0]['text']})
    except (ValueError, TypeError):
        return Response({'error': 'An error has occured.'}, status=400)