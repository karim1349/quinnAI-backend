import os

import openai

from api.constants import CLASSIFY_PROMPT, EMAIL_LABEL_CHOICES, ORTHOGRAPH_PROMPT

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


def orthograph_correction(source):
    prompt = ORTHOGRAPH_PROMPT.format(source)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text'].strip()