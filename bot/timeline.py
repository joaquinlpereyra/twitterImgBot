"""Handles everything which modifies the twitter timeline of the bot"""


def delete_last_tweet(api):
    last_tweet = api.user_timeline()[0].id
    api.destroy_status(last_tweet)

def delete_tweet_by_id(id_to_delete, api):
    tweet_to_delete = api.get_status[id_to_delete]
    api.destroy_status(tweet_to_delete)
