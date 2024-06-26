'''
Created on 

@author: 
    Chaaya

source:
https://praw.readthedocs.io/en/stable/index.html
https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
'''
import pandas as pd
import os

import praw
from dotenv import load_dotenv

load_dotenv()

YOUR_CLIENT_ID        = os.environ.get("YOUR_CLIENT_ID")
YOUR_CLIENT_SECRET        = os.environ.get("YOUR_CLIENT_SECRET")
YOUR_USER_AGENT        = os.environ.get("YOUR_USER_AGENT")

csv_name = "bellroy.csv"

df_main = pd.read_csv(csv_name)

reddit = praw.Reddit(client_id=YOUR_CLIENT_ID,
                     client_secret=YOUR_CLIENT_SECRET,
                     user_agent=YOUR_USER_AGENT)

posts = reddit.subreddit("BuyItForLife+ManyBaggers+wallets+backpacks").search('Bellroy', limit=100000)

data = []
for post in posts:
    if post.title not in df_main['title']:
        data.append({
            'title': post.title,
            'selftext': post.selftext,
            'comments': [comment.body for comment in post.comments.list() if hasattr(comment, 'body')]
        })

df = pd.DataFrame(data)
# print(df.head())
df.to_csv(csv_name, index=False, mode='a', header=False)

'''
need to generalise
'''