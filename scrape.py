'''
Created on 

@author: 
    Chaaya

source:
https://praw.readthedocs.io/en/stable/index.html
    
'''
import pandas as pd
import os

import praw
from dotenv import load_dotenv

load_dotenv()

YOUR_CLIENT_ID        = os.environ.get("YOUR_CLIENT_ID")
YOUR_CLIENT_SECRET        = os.environ.get("YOUR_CLIENT_SECRET")
YOUR_USER_AGENT        = os.environ.get("YOUR_USER_AGENT")

df_main = pd.read_csv("bellroy.csv")

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
df.to_csv("bellroy.csv", index=False, mode='a')