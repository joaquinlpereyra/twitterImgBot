twitterImgBot
===============

Python script wich main function is tweeting pictures from a given folder.

It can easily be used together with cron or another task scheduler to create a Twitter bot. All you need is a computer with internet connection and a folder with images.

Features
==============
* **Separate config file.** You don't have to touch a line of code. Of course can also do that if you wish <3.
* **Delete tweets upon command:** The bot listens to a master account for an specified command to delete the last tweet. It will also ban the image posted in the deleted tweet, never uploading it again. 
* **Handles requests:** The bot will also listen to tweets containing a custom string from any user and will post a random picture for them. A list of possible text answers to be posted along with the image can be given and the bot will choose one them at random. If a tweet from user A with the custom string is found and the tweet also has a "to @(user B)" the bot will interpret that the user A is gifting an image to user B. A list of possible text answers to such "gifts" can also be given.
* **No repeat:** The bot won't repeat images until a custom amount of pictures have been posted in between. 
* **Tweets at random intervals:** The bot can tweet at random intervals, behaving more like a human, instead of tweeting at totally predictable times.
* ** Pretty fast:** The bot checks requests, commands from the master account and checks if it needs to upload a picture in less than a second. Of course, if the bot actually needs to upload something, it will probably take more time.
* **Logs**: This actually needs to be improved to use Python's standard logging module, but it is good as it is and it gets the job done. The log contains date, image posted and the twitt that was being replied (if any).
* **Doesn't need much:** Really, you're all set with python, tweepy, a task scheduler like cron and a bunch of images in a folder. Of course, you'll also need [to create a Twitter app to get your API key and such](https://dev.twitter.com/oauth/overview/application-owner-access-tokens). 

Setup
===============

**In short**: You'll need python3, tweepy and the [twitter tokens](https://dev.twitter.com/oauth/overview/application-owner-access-token). You need to fill the settings file inside the 'settings' folder with the appropiate information *(every option is expalined below in detail)*. You'll probably want a task scheduler too (to fully [automate the bot](
#Live-example-and-full-automation-idea)). 

**Longish explanation**:

Python3 comes with pretty much every modern distro, but you probably don't have tweepy installed. Then you should install pip.
```sudo apt-get install python3-pip```

Then you should install tweepy. 

```pip install tweepy```

Make sure **all** settings are filled correctly. Double check paths. Do use full paths (not ~/bot/ but /home/username/bot/). Do end paths with /.The bot **will** fail. There's a detailed explanation of every setting in the 

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
log_file = /home/joaquin/.scripts/bin/log
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

Options
===============
- **[Twitter]**
  - Everything in this section is provided by Twitter. [Check this out.](https://dev.twitter.com/oauth/overview/application-owner-access-tokens)
- **[App]**
  - *image_folder*: source folder for the bot to look up the images to be posted.
  - *execution_chance*: this makes the bot twitt at random intervals. Set it to a low value and have to bot execute very often: most of the time it will not twitt.
  - *allow_repeat_after*: how many images the bot must have posted before it is allowed to repeat a picture.
  - *log_file*: full path to the log file. You probably want to use *BOT_PATH/logs/log*. 
  - *bot_account*: the username for the bot account. **DO** start with @.
  - *master_account*: the username which the bot will listen to for delete commands. **DO** start with @.
  - *dont_tweet_file*: full path to the banned images list file. You probably want to use *BOT_PATH/logs/banned*
- **[Orders]**
  - *ban_command*: if master_account tweets something starting with this, will delete last tweet and ban last image posted.
  - *request_command*: if anybody tweets something starting with this, it will give them a picture. If tweet has a "to @(userB)" in it somewhere *and* starts with the request_command, bot will interpret as a gift from user posting to userB.  
- **[Texts]**
  -*requests_answers*: bot will choose randomly from here when complying to request from a request_command with no "to @". the reply will look like "@user request_answer"
  -*requests_to_third_answers*: bot will choose ramdonly from here when complying to requests from a request_command with "to @" in it. the reply will look like "@userB request_to_third_answers @requester"


Usage
===============

**Execute it.** That's it.

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
