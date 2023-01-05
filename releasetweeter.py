import datetime
import tweepy
from calender import calender_conversion
import configparser
import csv
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
date = datetime.datetime.now()
today_month=date.strftime("%m")
today_day=date.strftime("%d")


def date_checker(month,day): #function that will be used when iterating through shoes.csv to check if the release date is today. 
    calender_conversion(month,day)
    if today_month==month:
        if int(today_day)==int(day)-1: #need a case in which if its the first of the month, it che
            return True
    else:
        return False

def tweeter(model,color):
    api.update_status(f"The {model} {color} is releasing tomorrow!")



with open ('shoes.csv','r') as csvfile: #main function
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)
