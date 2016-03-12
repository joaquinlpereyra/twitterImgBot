import datetime
"""These functions log everything. To-do: actually use the standar logger
module."""

date = str(datetime.datetime.now())


def logLine(post_number, img_path, reply_id):
    log_line = post_number + '\t'
    log_line += date + '\t'
    log_line += img_path + '\t'
    log_line += str(reply_id) + '\n'
    return(log_line)


def addLineToLog(line, log_file):
    with open(log_file, 'a') as log:
        log.write(line)


def addBanned(reply_id, log):
    ban_message = "ABOVE IMAGE WAS BANNED!"
    with open(log, 'a') as log:
        log.write(date + '\t' + ban_message + '\t' + str(reply_id) + '\n')


def addWarning(warning, log):
    with open(log, 'a') as log:
        log.write(date + '\t' + warning + '\n')
