import yagmail
import pandas
from news import NewsFeed
import datetime

while True:
    # Execute program at 17.43
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 43:

        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            news_feed = NewsFeed(interest=row['interest'],
                                 from_date=yesterday,
                                 to_date=today)

            email = yagmail.SMTP(user="youraccount@gmail.com", password="YourPassword")
            email.send(to=row['email'],
                       subject=f"Your {row['interest']} news for today!",
                       content=f"Hi {row['name']} \n See what´s on about {row['interest']} today. \n{news_feed.get()}\n Joakim")

    time.sleep(60)  #paus the execution for 60 seconds

