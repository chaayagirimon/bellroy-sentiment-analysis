'''
Created on 

@author: 
    Chaaya

source:
https://praw.readthedocs.io/en/stable/index.html
https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
'''
from datetime import datetime
import os
from dotenv import load_dotenv

import pandas as pd

import praw

load_dotenv()

YOUR_CLIENT_ID        = os.environ.get("YOUR_CLIENT_ID")
YOUR_CLIENT_SECRET        = os.environ.get("YOUR_CLIENT_SECRET")
YOUR_USER_AGENT        = os.environ.get("YOUR_USER_AGENT")

csv_name = "bellroy.csv"    

reddit = praw.Reddit(client_id=YOUR_CLIENT_ID,
                     client_secret=YOUR_CLIENT_SECRET,
                     user_agent=YOUR_USER_AGENT)

def scrape(post):
    return {
            'title': post.title,
            'selftext': post.selftext,
            'comments': [comment.body for comment in post.comments.list() if hasattr(comment, 'body')],
            'comment_upvotes': [comment.score for comment in post.comments.list() if hasattr(comment, 'score')],
            'comments_utc': [str(datetime.fromtimestamp(comment.created_utc)) 
                            for comment in post.comments.list() if hasattr(comment, 'created_utc')], 
            'upvotes': post.score,
            'time_stamp': datetime.fromtimestamp(post.created_utc)
            }

def not_exists(posts):
    data = []
    for post in posts:
            print(post.title)
            data.append(scrape(post))

    df = pd.DataFrame(data)
    df.to_csv(csv_name, index=False)
    
def if_exists(posts, df_main):
    data = []
    for post in posts:
        if post.title not in df_main['title'].tolist():
            print(post.title)
            data.append(scrape(post))
    df = pd.DataFrame(data)
    df.to_csv(csv_name, index=False, mode='a', header=False)

def main():
    posts = reddit.subreddit("BuyItForLife+ManyBaggers+wallets+backpacks+EDC+onebag+EDCexchange+GooglePixel+frugalmalefashion").search('Bellroy', limit=1000)

    if not os.path.isfile(csv_name):
        open(csv_name, mode='x')
        not_exists(posts)
    else:
        df_main = pd.read_csv(csv_name) 
        if_exists(posts, df_main)   

if __name__ == "__main__":
    main()