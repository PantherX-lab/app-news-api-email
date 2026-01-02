import requests
from send_email import send_email

api_key ="b7f076167504401e9a8cb70f259ae4c4"
url = ("https://newsapi.org/v2/everything?q=tesla&" \
       "from=2025-12-02&sortBy=publishedAt&apiKey=" \
       "b7f076167504401e9a8cb70f259ae4c4")

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""

for article in content["articles"]:
    title = article.get("title")
    description = article.get("description")

    if title:
        body += title + "\n"
        if description:
            body += description
        body += "\n\n"

send_email(message=body)




