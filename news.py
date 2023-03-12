import requests

class NewsFeed:
    """Representing multiple news titles and links as a single string"""
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "eca72bf95e2d4f4c910aa058209534db"

    def __init__(self,interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"

        response = requests.get(url)
        content = response.json()

        if 'articles' in content:
            articles = content['articles']
            email_body = ''
            for article in articles:
                email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
            return email_body
        else:
            return 'no articles found.'

news_feed = NewsFeed(interest='nasa', from_date='2020-11-12', to_date='2022-11-13', language='en')
print(news_feed.get())


