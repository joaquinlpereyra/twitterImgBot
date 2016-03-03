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
    "Filters mentions by time and checks if they've already been answered"
    relevant_mentions = []
    for tweet in mentions:
        if is_recent(tweet, time) and not already_answered(tweet, log):
            relevant_mentions.append(tweet)
    return relevant_mentions

def is_recent(tweet, time_in_minutes):
    expiration_time = datetime.timedelta(minutes=time_in_minutes)
    tweet_date = tweet.created_at
    time_since_order = datetime.datetime.utcnow() - tweet_date
    if time_since_order < expiration_time:
        return True

def is_delete_order(mention, master_account, ban_command):
    "Check if is a valid delete order"
    mention = mention.text.lower()
    ban_command = ban_command.lower()
    if mention.startswith(ban_command):
        return True

def is_img_request(mention, request_command):
    if mention.text.lower().startswith(request_command.lower()):
        return True
    else:
        return False

def who_asks(mention):
    user_name = "@" + mention.user.screen_name
    return user_name

def is_from_master(mention, master_account):
    if who_asks(mention) == master_account:
        return True

def already_answered(tweet, log_file):
    "Open logs file to see if the request has already been answered"
    with open(log_file, 'r') as log:
        for line in log:
            if str(tweet.id) in line:
                return True

def mentions_third_user(tweet):
    if "to @" in tweet.text.lower():
        return True

def request_to_whom(tweet):
    "Returns the user to whom the gift shall be sent"
    tweet = tweet.text
    divide_tweet = tweet.partition("to @")[2]
    whom = divide_tweet.partition(" ")[0]
    # requests to "@fri_end!" should be given to "@fri_end" not "@fri_end!"
    realWhom = ""
    for letter in whom:
        if letter.isalpha() or letter == "_":
            realWhom = realWhom+letter
    return realWhom
