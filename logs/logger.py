import datetime
"""These functions log everything. To-do: actually use the standar logger
module."""

date = str(datetime.datetime.now())


def addPost(img_path, reply_id, log):
    with open(log, 'a') as log:
        log.write(date + '\t' + str(img_path) + '\t' + str(reply_id) + '\n')


def addBanned(reply_id, log):
    ban_message = "ABOVE IMAGE WAS BANNED!"
    with open(log, 'a') as log:
        log.write(date + '\t' + ban_message + '\t' + str(reply_id) + '\n')


def addWarning(warning, log):
    with open(log, 'a') as log:
        log.write(date + '\t' + warning + '\n')
