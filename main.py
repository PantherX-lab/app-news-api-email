import requests

api_key = "b7f076167504401e9a8cb70f259ae4c4"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2025-12-02&sortBy=publishedAt&apiKey=" \
      "b7f076167504401e9a8cb70f259ae4c4"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
