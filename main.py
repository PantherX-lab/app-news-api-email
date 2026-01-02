import requests
from send_email import send_email

topic = "tesla"

api_key ="b7f076167504401e9a8cb70f259ae4c4"
url = ("https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "sortBy=publishedAt&" \
       "apiKey=b7f076167504401e9a8cb70f259ae4c4&" \
       "language=en")

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""

for article in content["articles"][:20]:
    title = article.get("title")
    description = article.get("description")
    url = article.get("url")

    if title:
        body += title + "\n"
        if description:
            body += description + "\n"
        if url:
            body += f"Read more: {url}\n"
        body += "\n"

send_email(
    message=body,
    subject="Today's News")




