"""Handles everything which modifies the twitter timeline of the bot"""


def delete_last_tweet(api):
    last_tweet = api.user_timeline()[0].id
    api.destroy_status(last_tweet)
