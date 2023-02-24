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

ANSWER_HEADLINE_PROMPT = "Generate 3 responses to this email from {} with minimum 2 words, separated with pipe only : '{}'. Please generate at least three contradictive outcomes, for example : 'I agree|I disagree|We will see later' , with the following format : 'outcome1|outcome2|outcome3'"

ANSWER_CONTENT_PROMPT = "Generate a response to this email from {} : '{}'. The response's content should be related to this headline : '{}'"