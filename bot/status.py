import os

"""Handles statuses from the bot.
Makes sure it doesn't post anything repeated or banned"""


class Tweet():
    """A tweet with its text, media and reply_id. You can tell it to
    be posted to twitter with the API and to change its media.
    You can ask it if it was already tweeted or if it is banned.
    """

    def __init__(self, tweet_media, tweet_text, reply_id=None):
        """Initializes a tweet with a media, a text and reply_id"""
        self.text = tweet_text
        self.media = tweet_media
        self.reply_id = reply_id

    def post_to_twitter(self, api):
        """Posts the tweet to twitter via the api. Returns the ID of
        the tweet posted.
        """
        status = api.update_with_media(filename=self.media,
                                       status=self.text,
                                       in_reply_to_status_id=self.reply_id)
        return status.id

    def is_already_tweeted(self, log_file, tolerance):
        """Returns True if the twitt was already tweeted withing the last
        tolerance tweets and False if log_file isn't a file or if it wasn't
        tweeted.
        """
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
        """Returns True if the tweet media was banned or False if the
        banned_list don't exist or wasn't banned."""
        if not os.path.isfile(banned_list):
            # if file doesn't exist just don't bother
            return False
        with open(banned_list, 'r') as banned:
            if (self.media + "\n") in banned:
                return True
        return False

    def change_media(self, new_media):
        """Changes the tweet media to new_media."""
        self.media = new_media
