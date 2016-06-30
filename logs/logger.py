import datetime
"""These functions log everything. To-do: actually use the standar logger
module."""

date = str(datetime.datetime.now())


def log_line(post_number, tweet_id, img_path, reply_id):
    """Returns a string fit for the log from a post_number, tweet_id,
    img_path and reply_id.
    """
    log_line = post_number + '\t'
    log_line += str(tweet_id) + '\t'
    log_line += date + '\t'
    log_line += img_path + '\t'
    log_line += str(reply_id) + '\n'
    return log_line


def add_line_to_log(line, log_file):
    """Appends line to the log_file."""
    with open(log_file, 'a') as log:
        log.write(line)


def add_banned_to_log(post_number, reply_id, log_file):
    """Appends a banned message to the log_file from a post_number, reply_id"""
    ban_message = "AN IMAGE WAS BANNED!"
    log_ban_line = (post_number + '\t' + date + '\t' +
                   ban_message + '\t' + str(reply_id) + '\n')
    add_line_to_log(log_ban_line, log_file)


def add_warning_to_log(last_post_number, warning, log_file):
    """Appends a warning message to the log_file from a last_post_number and
    warning string.
    """
    log_warning_line = last_post_number + '\t' + date + '\t' + warning + '\n'
    add_line_to_log(log_warning_line, log_file)

