import os

"""Handles statuses from the bot.
Makes sure it doesn't post anything repeated or banned"""


class Tweet():
    """A tweet only has two things: an image and text"""

    def __init__(self, tweet_media, tweet_text, reply_id=None):
        self.text = tweet_text
        self.media = tweet_media
        self.reply_id = reply_id

    def getMedia(self):
        return self.media

    def getText(self):
        return self.text

    def post_to_twitter(self, api):
        status = api.update_with_media(filename=self.media,
                                       status=self.text,
                                       in_reply_to_status_id=self.reply_id)
        return status.id

    def is_already_tweeted(self, log_file, tolerance):
        tolerance = -1*(tolerance)
        if not os.path.isfile(log_file):
            # if the file doesn't exist just don't bother
            return False
        try:
            already_tweeted = open(log_file, 'r').readlines()[tolerance:]
        except IndexError:
            already_tweeted = open(log_file, 'r').readlines()
        for line in already_tweeted:
            if line.strip() and line.split('\t')[2] == self.media:
                # if element.strip() checks if line not blank
                return True
        return False

    def is_banned(self, banned_list):
        if not os.path.isfile(banned_list):
            # if file doesn't exist just don't bother
            return False
        with open(banned_list, 'r') as banned:
            if (self.media + "\n") in banned:
                return True

    def change_media(self, new_media):
        self.media = new_media
