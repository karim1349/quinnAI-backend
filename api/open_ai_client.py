import os

import openai

from api.constants import CLASSIFY_PROMPT, EMAIL_LABEL_CHOICES

openai.api_key = os.environ.get('OPENAI_API_KEY')


def classify_email(subject: str, sender:str) -> str:
    prompt = CLASSIFY_PROMPT.format(subject, sender, EMAIL_LABEL_CHOICES)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1
    )
    return response['choices'][0]['text'].strip()
