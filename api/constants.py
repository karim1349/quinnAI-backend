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
    "Hobbies or Interests"
]
ORTHOGRAPH_PROMPT = "renvoie moi ce texte sans les potentielles fautes d'orthographes : {}"

ANSWER_HEADLINE_PROMPT = "Generate four responses to an email from a specific person. Each response should be between 5 and 7 words long and separated by a pipe symbol (|). The goal is to provide at least four outcomes to the original email. To clarify, the responses should be mutually exclusive and cannot all be true at the same time. The format for the four responses should be 'response1|response2|response3|response4'. Email : '{}'. Email sender : '{}'"

ANSWER_CONTENT_PROMPT = "You are an email assistant and you can reply like it was me ({}) , i want you to reply to the email : '{}' taking in consideration the following reply summary : '{}', in the same idiom as the source message."