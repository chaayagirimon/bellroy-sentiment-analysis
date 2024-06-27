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

import pandas as pd

import praw
from dotenv import load_dotenv

load_dotenv()

YOUR_CLIENT_ID        = os.environ.get("YOUR_CLIENT_ID")
YOUR_CLIENT_SECRET        = os.environ.get("YOUR_CLIENT_SECRET")
YOUR_USER_AGENT        = os.environ.get("YOUR_USER_AGENT")

csv_name = "bellroy.csv"

# df_main = pd.read_csv(csv_name)   

reddit = praw.Reddit(client_id=YOUR_CLIENT_ID,
                     client_secret=YOUR_CLIENT_SECRET,
                     user_agent=YOUR_USER_AGENT)

def scrape(post):
    return {
            'title': post.title,
            'selftext': post.selftext,
            'comments': [comment.body for comment in post.comments.list() if hasattr(comment, 'body')],
            'comment_upvotes': [comment.score for comment in post.comments.list() if hasattr(comment, 'score')],
            'comments_utc': [str(datetime.fromtimestamp(comment.created_utc)) for comment in post.comments.list() if hasattr(comment, 'created_utc')], 
            'upvotes': post.score,
            'time_stamp': datetime.fromtimestamp(post.created_utc)
            }

def main():
    posts = reddit.subreddit("BuyItForLife+ManyBaggers+wallets+backpacks+EDC+onebag+EDCexchange+GooglePixel+frugalmalefashion").search('Bellroy', limit=1000)

    data = []
    # print(df_main['title'].head())
    for post in posts:
        # if post.title not in df_main['title'].tolist():
            print(post.title)
            data.append(scrape(post))

    df = pd.DataFrame(data)
    # print(df.head())
    # df.to_csv(csv_name, index=False, mode='a', header=False)
    df.to_csv(csv_name, index=False)

if __name__ == "__main__":
    main()


'''
1.need to generalise
'''