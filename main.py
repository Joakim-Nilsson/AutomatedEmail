# Api Key: eca72bf95e2d4f4c910aa058209534db
import requests
from pprint import pprint

class NewsFeed:
    """Representing multiple news titles and links as a single string"""
    api_key = "apiKey=eca72bf95e2d4f4c910aa058209534db"
    base_url = "https://newsapi.org/v2/everything?"

    def __init__(self,interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        pass


url = "https://newsapi.org/v2/everything?" \
       "qInTitle=tesla&" \
       "from=2023-02-10&" \
       "to=2023-03-10&" \
       "language=en&" \
       "apiKey=eca72bf95e2d4f4c910aa058209534db"

response = requests.get(url)
content = response.json()
articles = content['articles']

email_body = ''
for article in articles:
    email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

print(email_body)




