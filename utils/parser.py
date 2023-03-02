from bs4 import BeautifulSoup


def parse_email_content_html(email_content: str):
    soup = BeautifulSoup(email_content, 'html.parser')
    text_content = ""

    messages_unquoted = soup.select('div:not(.gmail_quote)')[0]
    for d in messages_unquoted.find_all(['div', 'h1', 'a']):
        text_content += " " + d.get_text(strip=True)
    return text_content



clear_examp = """
<div dir="ltr">Bonjour,
    <div>Merci ! tu le trouveras en pièce jointe.</div>
    <div><br></div>
    <div>Bonne journée,</div>
    <h1>hello fucking world</h1>
    <a href="hello">aywaa</a>

</div><br>
<div class="gmail_quote">
    <a>helloo</a>
</div>
<div><br></div>-- <br>
<div dir="ltr">
    <div dir="ltr">EL HASSANE</div>
</div>
"""
xx = parse_email_content_html(clear_examp)
print(xx)
