## BELLROY SENTIMENT ANALYSIS
- install requirements:
```
pip install -r requirements.txt
```
### Scraping tutorial:
First we need to get the authentication information to create an instance:
(refer to : https://towardsdatascience.com/scraping-reddit-data-1c0af3040768)
- go to this [page](https://www.reddit.com/prefs/apps).
- click on "create another app" or "create app".
- fill the form that pops up. 
    - select on script radio button.
    - choose redirect uri as: http://localhost:8080.
- copy the information and add it to the .env file (using the .env.sample as a reference).

Next, if needed you can add more subreddits to line 62 in scrape.py:
```
posts = reddit.subreddit("BuyItForLife+ManyBaggers+wallets+backpacks+EDC+onebag+EDCexchange+GooglePixel+frugalmalefashion").search('Bellroy', limit=1000)
```

Finally, you can run the python file by typing this in the terminal:
```
python scrape.py
```
### Sentiment analysis:
In order to open jupyter notebook, type this to the terminal:
```
jupyter notebook
```
And run sentiment_analysis.ipynb!!