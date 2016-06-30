"""Handles everything which modifies the twitter timeline of the bot"""


def delete_last_tweet(api):
    """ Deprecated function. Here because it may be useful. It is never
    called"""
    last_tweet = api.user_timeline()[0].id
    api.destroy_status(last_tweet)

def delete_tweet_by_id(id_to_delete, api):
    """Delete tweet with id id_to_delete."""
    api.destroy_status(id_to_delete)
