import openai
from django.conf import settings

from api.constants import (
    ANSWER_CONTENT_PROMPT,
    ANSWER_HEADLINE_PROMPT,
    CLASSIFY_PROMPT,
    EMAIL_LABEL_CHOICES,
    ORTHOGRAPH_PROMPT,
    SCORE_EMAIL_PROMPT,
)

openai.api_key = settings.OPENAI_API_KEY


def classify_email(subject: str, sender: str) -> str:
    prompt = CLASSIFY_PROMPT.format(subject, sender, EMAIL_LABEL_CHOICES)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
    )
    return response["choices"][0]["text"].strip()


def orthograph_correction(source):
    prompt = ORTHOGRAPH_PROMPT.format(source)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response["choices"][0]["text"].strip()


def headlines_generation(sender, source):
    prompt = ANSWER_HEADLINE_PROMPT.format(sender, source)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response["choices"][0]["text"].strip()


def response_generation(sender, source, headline):
    prompt = ANSWER_CONTENT_PROMPT.format(sender, source, headline)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response["choices"][0]["text"].strip()


def score_email(subject, sender):
    """
    Scores the importance of an email based on the subject and sender.
    Returns a score from 0 to 100.
    """

    prompt = SCORE_EMAIL_PROMPT.format(subject, sender)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # score = int(response.choices[0].text.strip())

    return response
