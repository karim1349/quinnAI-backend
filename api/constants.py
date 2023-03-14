PREDICT_LABEL_PROMPT = "suggest me a lebel to the email subject : {} and sender is : {}, give me only value names in output separate it using comma"
CLASSIFY_PROMPT = "suggest me a lebel to the email subject {} and sender is {}, choose me one value from this list {} give just the value without any other text"
EMAIL_LABEL_CHOICES = CATEGORIES = [
    "Health or Medical",
    "Recipes",
    "Events or Parties",
    "To Read or Follow Up",
    "Education or School",
    "Volunteer or Charity",
    "Client or Customer",
    "Feedback or Suggestions",
    "Legal",
    "Government or Official",
    "News or Current Events",
    "Job Search or or Career",
    "Personal Development",
    "Fitness or Exercise",
    "Hobbies or Interests",
    "Social Media Notifications",
    "Marketing or Advertising",
    "Travel Planning",
    "Home or Property",
    "Emergency or Urgent",
    "Productivity or Time Management",
    "News or Updates from Companies",
    "Memos or Notes",
    "News or Updates from Family or Friends",
    "General Correspondence",
    "Government or Official",
    "News or Current Events",
    "Job Search or Career",
    "Personal Development",
    "Fitness or Exercise",
    "Hobbies or Interests",
]
ORTHOGRAPH_PROMPT = (
    "renvoie moi ce texte sans les potentielles fautes d'orthographes : {}"
)

ANSWER_HEADLINE_PROMPT = "Detect the last email of the thread and then generate four responses of this last email. Each response should be between 5 and 7 words long and separated by a pipe symbol (|). The goal is to provide at least four outcomes. To clarify, the responses should be mutually exclusive and cannot all be true at the same time. The format for the four responses should be 'response1|response2|response3|response4'. Email : '{}'. Email sender : '{}'"
ANSWER_CONTENT_PROMPT = "You are an email assistant and you can reply like it was me ({}) , I want you to detect the last email of the thread and answer it : '{}' taking in consideration the following reply summary : '{}', in the same idiom as the source message."
SCORE_EMAIL_PROMPT = "Score the importance of  this email from 0 to 100 where the subject {} from sender {} and the body is {} on a scale from 0 to 100, print only a number not a string"

SUMMARIZE_BULLETPOINTS_PROMPT = "Résume le contenu de cette conversation d'email en puces :  {}."
SUMMARIZE_SHORT_PROMPT = "Fais un résumé synthétique de l'email que j'ai reçu: {}."
SUMMARIZE_LONG_PROMPT = "Fais un résumé détaillé de l'email que j'ai reçu: {}"

TRANSLATE_PROMPT = "Translate this text : '{}' to {}."

MELIORATE_PROMPT = "Meliorate this text : '{}'."
SHORTEN_PROMPT = "Shorten this text : '{}'."
LENGTHEN_PROMPT = "Lengthen this text : '{}'."
SIMPLIFY_PROMPT = "Simplify this text : '{}'."

CHANGE_TONE_PROMPT = "Tu es un expert de la rédaction d'e-mails, transforme mon email pour le rendre plus {} : '{}'."

DETECT_ACTIONS_PROMPT = "Tu es un assistant expert, je veux que tu identifies les actions importantes que je dois réaliser à partir de cet email {}."

REDACT_ANSWER_PROMPT = "Redact an answer from {} to this email conversation : '{}'."

Labels = labels = [
    {
        "name": "Health or Medical",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#f7a7c0"},
    },
    {
        "name": "Recipes",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#b65775"},
    },
    {
        "name": "Events or Parties",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#cccccc"},
    },
    {
        "name": "To Read or Follow Up",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#fcda83"},
    },
    {
        "name": "Education or School",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#434343"},
    },
    {
        "name": "Volunteer or Charity",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#666666"},
    },
    {
        "name": "Client or Customer",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#fef1d1"},
    },
    {
        "name": "Feedback or Suggestions",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#3c78d8"},
    },
    {
        "name": "Legal",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#149e60"},
    },
    {
        "name": "Government or Official",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#89d3b2"},
    },
    {
        "name": "News or Current Events",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#434343"},
    },
    {
        "name": "Job Search or Career",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#fb4c2f"},
    },
    {
        "name": "Personal Development",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#e4d7f5"},
    },
    {
        "name": "Fitness or Exercise",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#ffe6c7"},
    },
    {
        "name": "Hobbies or Interests",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#2a9c68"},
    },
    {
        "name": "Social Media Notifications",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#f691b3"},
    },
    {
        "name": "Marketing or Advertising",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#a4c2f4"},
    },
    {
        "name": "Travel Planning",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#a46a21"},
    },
    {
        "name": "Home or Property",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#076239"},
    },
    {
        "name": "Emergency or Urgent",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#d5ae49"},
    },
    {
        "name": "Productivity or Time Management",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#89d3b2"},
    },
    {
        "name": "News or Updates from Companies",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#f2c960"},
    },
    {
        "name": "Memos or Notes",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#fcdee8"},
    },
    {
        "name": "News or Updates from Family or Friends",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#89d3b2"},
    },
    {
        "name": "General Correspondence",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#3c78d8"},
    },
]