import re

import openai
from django.conf import settings

from api.constants import (ANSWER_CONTENT_PROMPT, ANSWER_HEADLINE_PROMPT,
                           CLASSIFY_PROMPT, EMAIL_LABEL_CHOICES,
                           ORTHOGRAPH_PROMPT, SCORE_EMAIL_PROMPT)

openai.api_key = settings.OPENAI_API_KEY


class ModelException(Exception):
    pass


def call_model(prompt, temperature=0.5, max_tokens=250, top_p=1, **kwargs):
    return openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        **kwargs
    )


def classify_email(subject: str, sender: str) -> str:
    prompt = CLASSIFY_PROMPT.format(subject, sender, EMAIL_LABEL_CHOICES)
    response = call_model(prompt)
    return response["choices"][0]["text"].strip()


def orthograph_correction(source):
    prompt = ORTHOGRAPH_PROMPT.format(source)
    response = call_model(prompt)
    return response["choices"][0]["text"].strip()



def headlines_generation(sender, source):
    prompt = ANSWER_HEADLINE_PROMPT.format(sender, source)
    response = call_model(prompt)
    return response["choices"][0]["text"].strip()



def response_generation(sender, source, headline):
    prompt = ANSWER_CONTENT_PROMPT.format(sender, source, headline)
    response = call_model(prompt)
    return response["choices"][0]["text"].strip()


def score_email(subject, sender):
    """
    Scores the importance of an email based on the subject and sender.
    Returns a score from 0 to 100.
    """

    prompt = SCORE_EMAIL_PROMPT.format(subject, sender)
    response = call_model(prompt)
    # score = int(response.choices[0].text.strip())
    pattern = re.compile(r'([0-9]+)')
    match = pattern.search(response.choices[0].text.strip())
    print(response.choices[0])

    if match:
        number = match.group(1)
        return int(number)
    raise ModelException("Error during calculating score of this email")
