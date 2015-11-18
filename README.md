twitterImgBot
===============

Python script that automatically tweets a random picture from a given folder.
It can easily be used together with cron or another task scheduler to create a working
twitter bot.
It started pretty simple but now it has quite a few features:

Features:
* Separate config file. You don't have to touch a line of code.
* Commands: set up a 'master account' and 'ban command' and ban images so the
bot deletes them from twitter and never posts them again. 
* Request: any user can request an image with a request_command. they can also
request an image for another user as a gift.
* Custom answers: a list of possible text answers to requests can be given.
* No repeat: bot will not repeat images! you can set the tolerance in the
allow_repeat_after setting in the config file.
* Execution chance makes it possible to run the script every minute to check
for requests and commands while not posting. This way the script doesn't have
to run on the background. Make it higher if you want your bot to tweet more
often!
* Ideal for setting up a bot at home: you don't need a server; just python
and a bunch of images in a folder.

v2 of the bot (realesead 18-nov-2015) was a complete rewrite of the script to 
make it more scalable. I doesn't add a lot of new features for the user though,
apart from some new log warnings. **BUT** it is twice as fast.

v2:
```
>>> test.measureTime()
0.7329306602478027
```
v1:
```
>>> test.measureTime()
1.5387952327728271
```

Set up
===============
You'll need tweepy. If you don't have it, run:

```pip install tweepy```

You should also fill the settings file in the 'settings' folder with the appropriate information. 

Make sure **all** settings are filled correctly and that paths are written
correctly. Do use full paths.

This is an example of the config file used for @gentelindaOK, minus sensible information. 

```
# Replace where appropriate with your own settings.

[Twitter]
api_key =
secret_key =
token =
secret_token =

[App]
image_folder = /home/REDACTED/.twitter-bot/gentelindaok/
execution_chance = 1
allow_repeat_after = 50
log_file = /home/joaquin/.scripts/bin/log.log
bot_account = @gentelindaOK
master_account = @amemulo
dont_tweet_file = /home/REDACTED/.scripts/bin/dont_tweet

[Orders]
#caps agnostic
ban_command = @gentelindaOK don't
request_command = dear @gentelindaOK

[Texts]
#Respect indentation
request_answers = specially for you. xoxo
  only because you asked nicely. xoxo
  this is one of my best. be grateful. xoxo
  when you see your human partner, think of me. xoxo
  remember: if you like it put a password on it. xoxo
  humans are warmer. but what if you like the cold?. xoxo
  can you feel your species deprecation?. xoxo
request_to_third_answers = you just got a nice gift from
  apparently this person likes you
```

Usage
===============

**Execute it.** That's it.

You probably want to set it up on your crontab (or your favorite task scheduler).
This way, you'll have a twitter bot of your own.

You also have a couple of optional arguments:

```
optional arguments:
  -h, --help  show this help message and exit
  --tweet     Ignores execution chance, always run
  --test      Wont't tweet, just write to log
```

Live example and full automation idea
==============
You can check out [gentelindaOK](http://twitter.com/gentelindaOK) to see
a working account using this twitter bot.

@gentelindaOK is a fully automatic bot. My modified version of [RedditImageGrab
](https://github.com/joaquinlpereyra/RedditImageGrab)
downloads new images to my PC from a multireddit every morning. Then, a silly
one line bash command removes any image that is smaller than 50kb (to filter
glitches and very small pictures). This twitter bot is set up on cron
on my PC to execute every minute with a 1 percent execution chance.

Known bugs 
===============
There has been some bugs reports about the repetition of images. These were
reported for the old version of the bot and I'm pretty sure they are solved now.
But anyhow, if the bot twitts two images in a row (or you're experiencing any other kind
of malfunction having to do with allow_repeat_after), you should try the
[fork by johnnykernel](https://github.com/johnnykernel/twitterImgBot).

This fork doesn't have the ability to respond to request or ban images though,
and uses a way simpler method: it moves images which were alreday tweeted to 
a different folder.

