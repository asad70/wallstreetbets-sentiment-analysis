'''*****************************************************************************
Purpose: To analyze the sentiments of r/wallstreetbets
This program uses Vader SentimentIntensityAnalyzer to calculate the ticker compound value. 
You can change multiple parameters to suit your needs. See below under "set program parameters."
Implementation:
I am using sets to compare that if the ticker is valid, sets time complexity for
"x in s" is O(1) compare to list: O(n).
Limitations:
It depends mainly on the defined parameters for current implementation:
It completely ignores the heavily downvoted comments, and there can be a time when
the most mentioned ticker is heavily downvoted, but you can change that in upvotes variable.
Author: github:asad70
-------------------------------------------------------------------
****************************************************************************'''
import praw
from data import *
import time
import pandas as pd
import matplotlib.pyplot as plt
import squarify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class WallStreetBets:
    def __init__(self, current_time, c_analyzed, posts, picks, top_picks, symbols, titles, picks_ayz, scores):
        self.current_time = current_time
        self.c_analyzed = c_analyzed
        self.posts = posts
        self.picks = picks
        self.top_picks = top_picks
        self.symbols = symbols
        self.titles = titles
        self.picks_ayz = picks_ayz
        self.scores = scores


def analyze(clientid, clientsecret, usernme, passwrd):
    # set the program parameters
    limit = 500      # define the limit
    upvotes = 2     # define # of upvotes, comment is considered if upvotes exceed this #
    picks = 10     # define # of picks here, prints as "Top ## picks are:"
    picks_ayz = 5   # define # of picks for sentiment analysis
    post_flairs = ['Daily Discussion', 'Weekend Discussion', 'Discussion']    # posts flairs to search
    posts, count, c_analyzed, tickers, titles, a_comments = 0, 0, 0, {}, [], {}

    start_time = time.time()
    reddit = reddit_login("Comment Extraction", clientid, clientsecret, usernme, passwrd)
    subreddit = configure_reddit_subreddit(reddit)
    hot_python = subreddit.hot()    # sorting posts by hot
    extract_comments_symbols(hot_python, post_flairs, titles, posts, limit, upvotes, tickers, a_comments, count, c_analyzed)

    # sorts the dictionary
    symbols = dict(sorted(tickers.items(), key=lambda item: item[1], reverse = True))
    top_picks = list(symbols.keys())[0:picks]
    current_time = (time.time() - start_time)
    scores = apply_sentiment_analysis(symbols, picks_ayz, a_comments)
    
    WSB = WallStreetBets(current_time, c_analyzed, posts, picks, top_picks, symbols, titles, picks_ayz, scores)

    print_results(WSB)
    print_sentiment_analysis(WSB)
    return WSB

def reddit_login(user, clientid, clientsecret, usernme, passwrd):
    return praw.Reddit(user_agent=user,
        client_id=clientid,
        client_secret=clientsecret,
        username=usernme,
        password=passwrd)

def configure_reddit_subreddit(reddit):
    return reddit.subreddit('wallstreetbets')

def extract_comments_symbols(hot_python, post_flairs, titles, posts, limit, upvotes, tickers, a_comments, count, c_analyzed):
    # Extracting comments, symbols from subreddit
    for submission in hot_python:
        if submission.link_flair_text in post_flairs:    
            submission.comment_sort = 'new'     
            comments = submission.comments
            titles.append(submission.title)
            posts += 1
            submission.comments.replace_more(limit=limit)   
            for comment in comments:
                c_analyzed += 1
                if comment.score > upvotes:      
                    split = comment.body.split(" ")
                    for word in split:
                        word = word.replace("$", "")        
                        # upper = ticker, length of ticker <= 5, excluded words,                     
                        if word.isupper() and len(word) <= 5 and word not in blacklist and word in us:   
                            if word in tickers:
                                tickers[word] += 1
                                a_comments[word].append(comment.body)
                                count += 1
                            else:                               
                                tickers[word] = 1
                                a_comments[word] = [comment.body]
                                count += 1    
    
def apply_sentiment_analysis(symbols, picks_ayz, a_comments):
    # Applying Sentiment Analysis
    scores = {}
    vader = SentimentIntensityAnalyzer()
    picks_sentiment = list(symbols.keys())[0:picks_ayz]
    for symbol in picks_sentiment:
        stock_comments = a_comments[symbol]
        for cmnt in stock_comments:
            score = vader.polarity_scores(cmnt)
            if symbol in scores:
                for key, values in score.items():
                    scores[symbol][key] += score[key]
            else:
                scores[symbol] = score
        # calculating avg.
        for key in score:
            scores[symbol][key] = scores[symbol][key] / symbols[symbol]
            scores[symbol][key]  = "{pol:.3f}".format(pol=scores[symbol][key] )
    return scores

def print_results(WSB):
    # print top picks
    print("It took {t:.2f} seconds to analyze {c} comments in {p} posts.\n".format(t=WSB.current_time, c=WSB.c_analyzed, p=WSB.posts))
    print("Posts analyzed:")
    for i in WSB.titles: print(i)
    print(f"\n{WSB.picks} most mentioned picks: ")
    times = []
    top = []
    for i in WSB.top_picks:
        print(f"{i}: {WSB.symbols[i]}")
        times.append(WSB.symbols[i])
        top.append(f"{i}: {WSB.symbols[i]}")

def print_sentiment_analysis(WSB):
    # printing sentiment analysis 
    print(f"\nSentiment analysis of top {WSB.picks_ayz} picks:")
    df = pd.DataFrame(WSB.scores)
    df.index = ['Bearish', 'Neutral', 'Bullish', 'Total/Compound']
    df = df.T
    print(df)

# Date Visualization
# most mentioned picks    
# squarify.plot(sizes=times, label=top, alpha=.7 )
# plt.axis('off')
# plt.title(f"{picks} most mentioned picks")
# plt.show()

# Sentiment analysis
# df = df.astype(float)
# colors = ['red', 'springgreen', 'forestgreen', 'coral']
# df.plot(kind = 'bar', color=colors, title=f"Sentiment analysis of top {picks_ayz} picks:")
# plt.show()
