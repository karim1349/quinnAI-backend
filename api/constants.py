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

ANSWER_HEADLINE_PROMPT = "Generate four responses to an email from a specific person or the first email if you detect multiples emails. Each response should be between 5 and 7 words long and separated by a pipe symbol (|). The goal is to provide at least four outcomes to the original email. To clarify, the responses should be mutually exclusive and cannot all be true at the same time. The format for the four responses should be 'response1|response2|response3|response4'. Email : '{}'. Email sender : '{}'"
ANSWER_CONTENT_PROMPT = "You are an email assistant and you can reply like it was me ({}) , i want you to reply to the email or the first email  if you detect multiple emails : '{}' taking in consideration the following reply summary : '{}', in the same idiom as the source message."
SCORE_EMAIL_PROMPT = "Score the importance of the email with subject '{}' from sender '{}' on a scale from 0 to 100."

Labels = labels = [
    {
        "name": "Health or Medical",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#b39ddb"},
    },
    {
        "name": "Recipes",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#ffb74d"},
    },
    {
        "name": "Events or Parties",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#64b5f6"},
    },
    {
        "name": "To Read or Follow Up",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#f06292"},
    },
    {
        "name": "Education or School",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#81c784"},
    },
    {
        "name": "Volunteer or Charity",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#fbc02d"},
    },
    {
        "name": "Client or Customer",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#9575cd"},
    },
    {
        "name": "Feedback or Suggestions",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#90a4ae"},
    },
    {
        "name": "Legal",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#ff8a65"},
    },
    {
        "name": "Government or Official",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#4db6ac"},
    },
    {
        "name": "News or Current Events",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#aed581"},
    },
    {
        "name": "Job Search or Career",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#ffa726"},
    },
    {
        "name": "Personal Development",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#a1887f"},
    },
    {
        "name": "Fitness or Exercise",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#4dd0e1"},
    },
    {
        "name": "Hobbies or Interests",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#ffd54f"},
    },
    {
        "name": "Social Media Notifications",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#26a69a"},
    },
    {
        "name": "Marketing or Advertising",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#e57373"},
    },
    {
        "name": "Travel Planning",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#ba68c8"},
    },
    {
        "name": "Home or Property",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#7986cb"},
    },
    {
        "name": "Emergency or Urgent",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#ef5350"},
    },
    {
        "name": "Productivity or Time Management",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#4caf50"},
    },
    {
        "name": "News or Updates from Companies",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#9ccc65"},
    },
    {
        "name": "Memos or Notes",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#bcaaa4"},
    },
    {
        "name": "News or Updates from Family or Friends",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#ffe082"},
    },
    {
        "name": "General Correspondence",
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
        "color": {"textColor": "#ffffff", "backgroundColor": "#f48fb1"},
    },
]