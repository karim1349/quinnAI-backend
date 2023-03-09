import base64


def get_email_elements(email_detail):

    headers = email_detail['payload']['headers']
    subject = [header['value'] for header in headers if header['name'] == 'Subject'][0]
    receiver = [header['value'] for header in headers if header['name'] == 'To'][0]
    payload = email_detail['payload']
    if 'parts' in payload:
        parts = payload['parts']
        try:
            data = parts[0]['body']['data']
        except KeyError:
            pass
            data = parts[0]['parts'][0]['body']['data']
    else:
        data = payload['body']['data']
    body = base64.urlsafe_b64decode(data).decode('utf-8')

    return subject, body

# from api.tasks import scoring_emails_of_user
# u = User.objects.last()
# scoring_emails_of_user(u.pk, max_results=10)
