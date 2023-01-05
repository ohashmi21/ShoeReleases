import tweepy
import configparser
from datetime import datetime, time, timedelta
import csv

releases=[]
with open('Shoes.csv', 'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        releases.append(row)

def releases_adder(model,color,month,day):
    shoe_dict={'Model': model.strip(), 'Color': color.strip(), 'Month': month, 'Day': day}
    releases.append(shoe_dict)


def excel_checker(model,color,month,day):
    shoe_dict={'Model': model, 'Color': color, 'Month': month, 'Day': day}
    with open('Shoes.csv', 'r') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row == shoe_dict:
                return False

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

desired_date = datetime.today().date() - timedelta(days=0)

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
            if(word.startswith("‘") or word.startswith("'") or word.endswith("’" ) or word.endswith("'")):
                if(word.startswith("‘") or word.startswith("'")):
                    colorwayindex=tweetlist.index(word)
                color+=word
                color+=" "
        modelindex=colorwayindex-tweetlist.index("jordan")
        model=""
        for x in range(modelindex):
            model+=tweetlist[tweetlist.index("jordan")+x]
            model+=" "
        month=(tweetlist[tweetlist.index("releases")+1]).strip()
        day=(tweetlist[tweetlist.index("releases")+2]).strip()
        if excel_checker(model.strip(),color.strip(),month,day)==False:
            continue
        releases_adder(model,color,month,day)

        

        
    elif "dunk" in text:
        """if "kids" in text:
            continue
        if "women's" in text:
            continue
        if "preschool" in text:
            continue"""
        if "releases" not in text:
            continue
        color="None"
        tweetlist=text.split()
        color=""
        colorwayindex=0
        for word in tweetlist:
            if(word.startswith("‘") or word.startswith("'") or word.endswith("’" ) or word.endswith("'")):
                if(word.startswith("‘") or word.startswith("'")):
                    colorwayindex=tweetlist.index(word)
                color+=word
                color+=" "
        modelindex=colorwayindex-tweetlist.index("dunk")
        model=""
        for x in range(modelindex):
            model+=tweetlist[tweetlist.index("dunk")+x]
            model+=" "
        month=(tweetlist[tweetlist.index("releases")+1]).strip()
        day=(tweetlist[tweetlist.index("releases")+2]).strip()
        if excel_checker(model.strip(),color.strip(),month,day)==False:
            continue
        releases_adder(model,color,month,day)
    tweets_for_date=[]

with open('Shoes.csv', 'w', newline='') as csvfile:
    fieldnames = ['Model', 'Color', 'Month', 'Day']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    for row in releases:
        csvwriter.writerow(row)


releases.clear()
