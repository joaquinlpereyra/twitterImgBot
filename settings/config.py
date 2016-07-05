import os
import configparser
import tweepy
"""Reads configuration file and holds all settings for the bot to function."""

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
# read configs from file
config = configparser.ConfigParser()
config.read(dname + '/settings')
twitter_config = config['Twitter']
api_key = twitter_config['api_key']
secret_key = twitter_config['secret_key']
token = twitter_config['token']
secret_token = twitter_config['secret_token']

app_config = config['App']
source_folder = app_config['image_folder']
master_account = app_config['master_account']
bot_account = app_config['bot_account']
log_file = app_config['log_file']
banned_file = app_config['dont_tweet_file']
tolerance = int(app_config['allow_repeat_after'])
chance = int(app_config['execution_chance'])

orders_config = config['Orders']
ban_command = orders_config['ban_command']
request_command = orders_config['request_command']
time_tolerance = int(orders_config['time_tolerance'])

text_config = config['Texts']
tweet_post_number = text_config.getboolean('tweet_post_number')
tweet_this_text = text_config['tweet_this_text']
request_answers = text_config['request_answers'].split('\n')
request_to_third_answers = text_config['request_to_third_answers']
request_to_third_answers = request_to_third_answers.split('\n')

auth = tweepy.OAuthHandler(api_key, secret_key)
auth.set_access_token(token, secret_token)
api = tweepy.API(auth)
