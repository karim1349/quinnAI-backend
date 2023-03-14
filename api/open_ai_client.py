import re

import openai
from django.conf import settings

from api.constants import (ANSWER_CONTENT_PROMPT, ANSWER_HEADLINE_PROMPT,
                           CLASSIFY_PROMPT, EMAIL_LABEL_CHOICES,
                           ORTHOGRAPH_PROMPT, SCORE_EMAIL_PROMPT,
                           SUMMARIZE_BULLETPOINTS_PROMPT, SUMMARIZE_LONG_PROMPT, SUMMARIZE_SHORT_PROMPT,
                           TRANSLATE_PROMPT, 
                           MELIORATE_PROMPT, SHORTEN_PROMPT, LENGTHEN_PROMPT, SIMPLIFY_PROMPT,
                           CHANGE_TONE_PROMPT,
                           DETECT_ACTIONS_PROMPT, 
                           REDACT_ANSWER_PROMPT
)

openai.api_key = settings.OPENAI_API_KEY


class ModelException(Exception):
    pass


def call_model(prompt, temperature=0.5, max_tokens=500, top_p=1, **kwargs):
    return openai.Completion.create(
        engine="text-davinci-003",
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


def conversation_summary(source, sub_action):
    if sub_action == "BULLET_POINTS":
        prompt = SUMMARIZE_BULLETPOINTS_PROMPT.format(source)
        response = call_model(prompt)
    elif sub_action == "SHORT_SUMMARY":
        prompt = SUMMARIZE_SHORT_PROMPT.format(source)
        response = call_model(prompt)
    elif sub_action == "LONG_SUMMARY":
        prompt = SUMMARIZE_LONG_PROMPT.format(source)
        response = call_model(prompt)
    else: 
        raise ModelException("Invalid summary type")
    return response["choices"][0]["text"].strip()

def translate(source, sub_action):
    if sub_action in ["ENGLISH", "FRENCH", "GERMAN", "SPANISH", "DUTCH", "PORTUGUESE"]:
        prompt = TRANSLATE_PROMPT.format(source, sub_action)
        response = call_model(prompt)
    else:
        raise ModelException("Invalid translation language")
    return response["choices"][0]["text"].strip()

def meliorate(source, sub_action):
    valid_actions = {
        "MELIORATE_WRITING": MELIORATE_PROMPT,
        "SHORTEN": SHORTEN_PROMPT,
        "LENGTHEN": LENGTHEN_PROMPT,
        "SIMPLIFY": SIMPLIFY_PROMPT
    }

    if sub_action not in valid_actions:
        raise ModelException("Invalid melioration type")

    prompt = valid_actions[sub_action].format(source)
    response = call_model(prompt)
    return response["choices"][0]["text"].strip()


def change_tone(source, sub_action):
    if sub_action in ["PROFESSIONAL", "CASUAL", "DIRECT", "FRIENDLY"]:
        prompt = CHANGE_TONE_PROMPT.format(source, sub_action)
        response = call_model(prompt)
    else:
        raise ModelException("Invalid tone change type")
    return response["choices"][0]["text"].strip()

def detect_actions(source):
    prompt = DETECT_ACTIONS_PROMPT.format(source)
    response = call_model(prompt)
    return response["choices"][0]["text"].strip()

def redact_answer(source, user):
    prompt = REDACT_ANSWER_PROMPT.format(user, source)
    response = call_model(prompt)
    return response["choices"][0]["text"].strip()

def score_email(subject, sender, source):
    """
    Scores the importance of an email based on the subject and sender.
    Returns a score from 0 to 100.
    """

    prompt = SCORE_EMAIL_PROMPT.format(subject, sender, source)
    response = call_model(prompt)
    # score = int(response.choices[0].text.strip())
    pattern = re.compile(r'([0-9]+)')
    match = pattern.search(response.choices[0].text.strip())
    print(response.choices[0])

    if match:
        number = match.group(1)
        return int(number)
    return
    # raise ModelException("Error during calculating score of this email")
