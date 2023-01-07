import datetime
import tweepy
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
today_month=int(date.strftime("%m"))
today_day=int(date.strftime("%d"))

calender={'january':'1', 'february':'2','march':'3','april':'4', 'may':'5','june':'6','july': '7','august':'8','september':'9','october':'10','november':'11','december':'12'}

def calender_conversion(month,day):
    month=calender[month]
    r_day=''
    for x in day:
        if x.isdigit():
            r_day=r_day+x
    return(int(month),int(r_day))

def date_checker(month,day): #function that will be used when iterating through shoes.csv to check if the release date is today. 
    if today_month==month:
        if int(today_day)==int(day)-1: #need a case in which if its the first of the month, if checks if today is the 29th, 30th, or 31st
            return True
    else:
        return False

def tweeter(model,color):
    api.update_status(f"The {model} {color} is releasing tomorrow!")


with open ('shoes.csv','r') as csvfile: #main function
    reader=csv.DictReader(csvfile)
    for row in reader:
        shoe=row
        shoe_month,shoe_day=calender_conversion(shoe['Month'],shoe['Day'])
        model=shoe['Model']
        color=shoe['Color']
        if date_checker(shoe_month,shoe_day) is True:
            tweeter(model,color)
        else:
            continue

