import tweepy
import glob
import random
import os

#Personal, every user should complete.
api_key = "your api key"
api_secret = "your api key sec"
oauth_token = "your access token" # Access Token
oauth_token_secret = "your access token secret" # Access Token Secret

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(oauth_token, oauth_token_secret)
api = tweepy.API(auth)

#Changes directory to where the script is located (easier cron scheduling, allows you to work with relative paths)
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def randomimagetwitt(folder):
    #Takes the folder where your images are as the input and twitts one random file.
    images = glob.glob(folder + "*")
    image_open = images[random.randint(0,len(images))-1]
    api.update_with_media(image_open)

#Twitts
randomimagetwitt("source images folder")
