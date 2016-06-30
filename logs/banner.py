"""Handles everything having to do with banning images.
Someone's got to do the job you know."""


def ban_last_image(banned_file, log_file):
    """Bans the last image posted."""
    last_image = open(log_file, 'r').readlines()[-1]
    last_image = last_image.split('\t')[2]
    with open(banned_file, 'a') as banned:
        banned.write(last_image + '\n')

def ban_image_by_tweet_id(tweet_id, banned_file, log_file):
    """Bans the image posted in tweet_id."""
    for line in reversed(list(open(log_file, 'r').readlines())):
        line = line.split()
        if line[1] == str(tweet_id):
            with open(banned_file, 'a') as banned_file:
                banned_file.write(line[4] + '\n')
            break
