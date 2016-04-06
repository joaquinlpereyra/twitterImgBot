#!/usr/bin/python

from settings import config
from bot import status
from bot import requests
from bot import timeline
from logs import logger
from logs import banner
import random
import argparse
import sys

"""The glue that holds it all together: uses all the other modules
to handle requests, post tweets if chance is met, calls the logger
and parses the CLI arguments"""


def post_tweet(text, reply_id, test=False):
    """Actually sends a tweet to twitter"""
    tweet = status.Tweet()
    media = tweet.media(config.source_folder)
    tweet_text = tweet.text(text)
    log = config.log_file
    tolerance = config.tolerance
    banned_list = config.banned_file
    already_tweeted = status.is_already_tweeted(log, media, tolerance)
    banned = status.is_banned(banned_list, media)
    if already_tweeted or banned:
        return post_tweet(text, reply_id)  # just try again
    if not test:
        status.tweet(media, tweet_text, reply_id, api)
        log_line = logger.logLine(post_number, media, reply_id)
        logger.addLineToLog(log_line, log)
    if test:
        log_line = logger.logLine(post_number, "TEST", reply_id)
        logger.addLineToLog(log_line, log)


def respond_to_simple_request(tweet):
    reply_id = tweet.id
    user_name = tweet.user.screen_name
    answer = random.choice(config.request_answers)
    text = '@' + user_name + ' ' + answer
    return post_tweet(text, reply_id)


def respond_to_gift_request(tweet):
    reply_id = tweet.id
    user_giver = tweet.user.screen_name
    user_gifted = ('@' + requests.request_to_whom(tweet))
    answer = random.choice(config.request_to_third_answers)
    text = (user_gifted + ' ' + answer + ' @' + user_giver)
    return post_tweet(text, reply_id)


def orders():
    """Handle orders given to the bot via replies"""
    log = config.log_file
    time = config.time_tolerance
    master = config.master_account
    ban_command = config.ban_command
    master_account = config.master_account

    mentions = requests.mentions(config.bot_account, config.api)
    master_mentions = requests.master_mentions(mentions, log, master_account)
    relevant_mentions = requests.relevant_mentions(mentions, log, time)

    for tweet in relevant_mentions:
        if requests.is_img_request(tweet, config.request_command):
            if requests.mentions_third_user(tweet):
                responde_to_gift_request(tweet)
            else:
                respond_to_simple_request(tweet)

    for tweet in master_mentions:
        if requests.is_delete_order(tweet, master, ban_command):
            timeline.delete_last_tweet(api)
            banner.ban_last_image(config.banned_file, config.log_file)
            logger.addBanned(post_number, tweet.id, config.log_file)


def parse_args(args):
    """Parses arguments from command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--tweet", help="Ignores execution chance, always run",
                        action="store_true")
    parser.add_argument("--test", help="Wont't tweet, just write to log",
                        action="store_true")
    parser.add_argument("--tweetnumber", help="If you were already using this "
                        "bot and you want to start using the post_tweet_number"
                        " function you'll need to tell the bot where to "
                        "start. Use this option ONLY ONCE ")
    return parser.parse_args(args)


def getPostNumber(log_file):
    try:
        post_number = open(log_file, 'r').readlines()[-1]
        post_number = post_number.split('\t')[0]
        return str(int(post_number)+1)
    except (IndexError, ValueError):
        return "1"

def main():
    """Runs the whole program, the function of all functions"""
    global post_number  # it's needed both here and in post_tweet()
    global api  # it's used absolutely everywhere, so might as well be global

    args = parse_args(sys.argv[1:])
    test = args.test
    forceTweet = args.tweet
    manual_post_number = args.tweetnumber
    api = config.api

    tweet_text = config.tweet_this_text
    if config.tweet_post_number and manual_post_number is None:
         post_number = getPostNumber(config.log_file)
         tweet_text = "No. " + post_number + tweet_text
    if manual_post_number is not None:
        post_number = manual_post_number
        tweet_text = "No. " + manual_post_number + tweet_text

    orders()

    if random.randint(0, 99) < config.chance or test or forceTweet:
        try:
            post_tweet(tweet_text, None, test)
        except RuntimeError:
            warning = "!CRITICAL! No non-repeated or non-banned images found"
            logger.addWarning(post_number, warning, config.log_file)

if __name__ == "__main__":
    main()
