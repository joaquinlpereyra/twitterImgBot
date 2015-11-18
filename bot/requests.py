import datetime

"""Handles all type of twitter mentions to the bot.
With the functions here you can filter mentions,
identify orders, identify requesters, see if a request
was already answered or if it's recent.
"""


def mentions(bot_account, api):
    mentions = []
    for tweet in api.search(bot_account):
        mentions.append(tweet)
    return mentions


def relevant_mentions(mentions, log_file):
    relevant_mentions = []
    for tweet in mentions:
        if is_recent(tweet, 5) and not already_answered(tweet, log_file):
            relevant_mentions.append(tweet)
    return relevant_mentions


def is_order_from_master(mention, master_account):
    if who_asks(mention) == master_account:
        return True


def wants_to_delete(mention, ban_command):
    mention = mention.text.lower()
    ban_command = ban_command.lower()
    if mention.startswith(ban_command):
        return True


def is_delete_order(mention, master_account, ban_command):
    from_master = is_order_from_master(mention, master_account)
    delete_intention = wants_to_delete(mention, ban_command)
    if from_master and delete_intention:
        return True


def is_img_request(mention, request_command):
    if mention.text.lower().startswith(request_command.lower()):
        return True
    else:
        return False


def who_asks(mention):
    user_name = "@" + mention.user.screen_name
    return user_name


def already_answered(tweet, log_file):
    with open(log_file, 'r') as log:
        for line in log:
            if str(tweet.id) in line:
                return True


def is_recent(tweet, time_in_minutes):
    expiration_time = datetime.timedelta(minutes=time_in_minutes)
    tweet_date = tweet.created_at
    time_since_order = datetime.datetime.utcnow() - tweet_date
    if time_since_order < expiration_time:
        return True


def mentions_third_user(tweet):
    if "to @" in tweet.text.lower():
        return True


def request_to_whom(tweet):
    tweet = tweet.text
    divide_tweet = tweet.partition("to @")[2]
    whom = divide_tweet.partition(" ")[0]
    # if request is "send img to @friend!" bot should say @friend not @friend!
    if whom.isalpha():
        return whom
    else:
        realWhom = ""
        for letter in whom:
            if letter.isalpha():
                realWhom = realWhom+letter
        return realWhom
