"""Handles everything having to do with banning images.
Someone's got to do the job you know."""


def ban_last_image(banned_file, log_file):
    last_image = open(log_file, 'r').readlines()[-1]
    last_image = last_image.split('\t')[1]
    with open(banned_file, 'a') as banned:
        banned.write(last_image + '\n')
