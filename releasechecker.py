import tweepy
import configparser
import pandas as pd
from datetime import datetime, time, timedelta



# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
count=0
user="SOLELINKS"
limit=3200
tweets = tweepy.Cursor(api.user_timeline,screen_name=user, count=200, tweet_mode= 'extended').items(limit)

desired_date = datetime.today().date() - timedelta(days=1)

# Set the start and end times for the desired date
start_time = time(hour=0, minute=0, second=0)
end_time = time(hour=23, minute=59, second=59)

# Create a list to store the tweets for the desired date
tweets_for_date = []

# Iterate through the tweets and add the ones from the desired date to the list
for tweet in tweets:
    tweet_date = tweet.created_at.date()
    tweet_time = tweet.created_at.time()
    if tweet_date == desired_date and start_time <= tweet_time <= end_time:
        tweets_for_date.append(tweet)

for x in tweets_for_date:
    text=x.full_text
    text=text.lower()
    if "jordan" in text:
        if "kids" in text:
            continue
        if "women's" in text:
            continue
        if "preschool" in text:
            continue
        if "releases" not in text:
            continue
        color="None"
        tweetlist=text.split()
        color=""
        colorwayindex=0
        for word in tweetlist:
            if(word.startswith("‘") or word.endswith("’")):
                if(word.startswith("‘")):
                    colorwayindex=tweetlist.index(word)
                color+=word
                color+=" "
        modelindex=colorwayindex-tweetlist.index("jordan")
        model=""
        for x in range(modelindex):
            model+=tweetlist[tweetlist.index("jordan")+x]
            model+=" "
        Month=tweetlist.index("releases")+1
        Day=tweetlist.index("releases")+2
        print(f"Jordan {model} {color} {tweetlist[Month]} {tweetlist[Day]}")

        
    if "dunk" in text:
        if "releases" not in text:
            continue
        tweetlist=text.split()
        model=tweetlist.index("dunk")+1
        color=""
        for word in tweetlist:
            if(word.startswith("'") or word.endswith("'")):
                color+=word
                color+=" "
        Month=tweetlist.index("releases")+1
        Day=tweetlist.index("releases")+2
        print(tweetlist[model], color, tweetlist[Month], tweetlist[Day])
    tweets_for_date=[]