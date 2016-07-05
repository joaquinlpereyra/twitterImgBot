import datetime

"""Handles all type of twitter mentions to the bot.
With the functions here you can filter mentions,
identify orders, identify requesters, see if a request
was already answered or if it's recent.
"""


def mentions(bot_account, api):
    "All the mentions to the bot, one list"
    mentions = []
    for tweet in api.search(bot_account):
        mentions.append(tweet)
    return mentions


def master_mentions(mention_list, log, master):
    "All the mentions to the bot from the master account"
    master_mentions = []
    for tweet in mention_list:
        if is_from_master(tweet, master) and not already_answered(tweet, log):
            master_mentions.append(tweet)
    return master_mentions


def relevant_mentions(mentions, log, time):
    "Returns a filtered list of mentions by time and already-answered-ness."""
    relevant_mentions = []
    for tweet in mentions:
        if is_recent(tweet, time) and not already_answered(tweet, log):
            relevant_mentions.append(tweet)
    return relevant_mentions


def is_recent(tweet, time_in_minutes):
    """Return True if a tweet is considered recent within the context of
    time_in_minutes (ie: if it was posted less than time_in_minutes ago).
    """
    expiration_time = datetime.timedelta(minutes=time_in_minutes)
    tweet_date = tweet.created_at
    time_since_order = datetime.datetime.utcnow() - tweet_date
    return time_since_order < expiration_time


def is_delete_order(mention, master_account, ban_command):
    """Check if mention is a valid (ie: from the master acount) delete order
    (ie: starts with the ban_command).
    """
    mention = mention.text.lower()
    ban_command = ban_command.lower()
    return mention.startswith(ban_command)


def is_img_request(mention, request_command):
    """Return True if mention start with the request_command."""
    return mention.text.lower().startswith(request_command.lower())


def who_asks(mention):
    """Return the username (@username, with the at and all) of the
    poster of the mention.
    """
    user_name = "@" + mention.user.screen_name
    return user_name


def is_from_master(mention, master_account):
    """Return True if the mention was tweeted from master_account, False
    otherwise.
    """
    return who_asks(mention) == master_account


def already_answered(tweet, log_file):
    """Return True if the tweet id is found in a line of the log_file, False
    otherwise."""
    with open(log_file, 'r') as log:
        for line in log:
            if str(tweet.id) in line:
                return True
        else:
            return False


def mentions_third_user(tweet):
    """Return True if the tweet mentions a third user (that is, has a "to @"
    somewhere in the tweet text) False otherwise.
    """
    return "to @" in tweet.text.lower()


def request_to_whom(tweet):
    """Return the user to whom a tweet should be sent. Intended for gifts."""
    tweet = tweet.text
    divide_tweet = tweet.partition("to @")[2]  # ["send", "to @", "amemulo!. and also friends"]
    whom = divide_tweet.partition(" ")[0]  # ["amemulo!.", "and", "friends"]
    # requests to "@fri_end!" should be given to "@fri_end" not "@fri_end!"
    realWhom = ""
    for letter in whom:
        if letter.isalpha() or letter == "_":
            realWhom = realWhom+letter
    return realWhom
