import os
import random
from glob import glob

"""Handles statuses from the bot.
Makes sure it doesn't post anything repeated or banned"""


class Tweet():
    """A tweet only has two things: an image and text"""

    def media(self, folder):
        media_list = glob(folder + "*")
        media = random.choice(media_list)
        return media

    def text(self, text):
        return text


def tweet(tweet_media, tweet_text, reply_id, api):
    """Posts a tweet"""
    api.update_with_media(
        filename=tweet_media,
        status=tweet_text,
        in_reply_to_status_id=reply_id)


def is_already_tweeted(log_file, image, tolerance):
    tolerance = -1*(tolerance)
    if not os.path.isfile(log_file):
        # if the file doesn't exist just don't bother
        return False
    try:
        already_tweeted = open(log_file, 'r').readlines()[tolerance:]
    except IndexError:
        already_tweeted = open(log_file, 'r').readlines()
    for element in already_tweeted:
        if element.split('\t')[1] == image:
            return True


def is_banned(banned_list, media):
    if not os.path.isfile(banned_list):
        # if file doesn't exist just don't bother
        return False
    with open(banned_list, 'r') as banned:
        if (media + "\n") in banned:
            return True
