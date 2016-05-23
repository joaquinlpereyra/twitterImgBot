twitterImgBot
===============

There are way too many pretty pictures in the world to tweet all of them. twitterImgBot tries to solve just that.

The primary objective of this script is to tweet a random picture from a given folder. But it does some other things too and has some pretty nice things built in as well. See [the features](#features).

It can easily be used together with cron or another task scheduler to create a twitter bot. All you need is a computer with internet connection, python, tweepy and folder with a bunch of images.

Features
==============
* **Separate config file.** You don't have to touch a line of code. Of course can also do that if you wish <3.
* **Deletes and bans tweets upon command:** The bot listens to a master account for a tweet with a specified command to delete the tweet that was indicated by the reply id of the master command. In simple terms, that means you can delete a tweet by replying to it with a custom command from your master account. It will also ban the image posted in the deleted tweet, never uploading it again. 
* **Handles requests:** The bot will also listen to tweets containing a custom string from any user and will post a random picture for them. A list of possible text answers to be posted along with the image can be given and the bot will choose one them at random. If a tweet from user A with the custom string is found and the tweet also has a "to @(user B)" the bot will interpret that the user A is gifting an image to user B. A list of possible text answers to such "gifts" can also be given.
* **No repeat:** The bot won't repeat images until a custom amount of pictures have been posted in between. 
* **Tweets at random intervals:** The bot can tweet at random intervals, behaving more like a human, instead of tweeting at totally predictable times.
* **Can post tweet number and an user defined text with each tweet:** You can make your bot tweet only the images, you can add the post number to your tweets and you can add a custom text also.  
* **Pretty fast:** The bot checks requests, commands from the master account and checks if it needs to upload a picture in less than a second. Of course, if the bot actually needs to upload something, it will probably take more time.
* **Logs**: This actually needs to be improved to use Python's standard logging module, but it is good as it is and it gets the job done. The log contains date, image posted and the twitt that was being replied (if any).
* **Doesn't need much:** Really, you're all set with python, tweepy, a task scheduler like cron and a bunch of images in a folder. Of course, you'll also need [to create a Twitter app to get your API key and such](https://dev.twitter.com/oauth/overview/application-owner-access-tokens). 

Setup
===============
You need:
* python3
* tweepy
* [Twitter tokens](https://dev.twitter.com/oauth/overview/application-owner-access-token)

You'll probably also want a task scheduler like cron to [fully automate the bot](#live-example-and-full-automation-idea). 

Python3 comes with pretty much every modern distro, but you probably don't have tweepy installed. You should install pip.

```sudo apt-get install python3-pip```

and then tweepy 

```pip install tweepy```


You should then complete the settings file inside the settings folder. There's a [detailed explanation](#explanation) of every setting and also an [example config file](#example) in the [Options](#options) section. Please:

* Make sure **all** settings are filled correctly.
* Double check paths.
* Do use full paths *(not ~/bot/ but /home/username/bot/)*.}
* Do end paths with **/** (*forward slash*).

The bot **WILL** ~~probably~~ fail if these conditions are not met. 

Options
===============

### Explanation
- **[Twitter]**
  - Everything in this section is provided by Twitter. [Check this out.](https://dev.twitter.com/oauth/overview/application-owner-access-tokens)
- **[App]**
  - *image_folder*: source folder for the bot to look up the images to be posted.
  - *execution_chance*: this makes the bot tweet at random intervals. Set it to a low value and have to bot execute very often: most of the time it will not tweet. I find that 1 per cent execution_chance works well if the script runs every minute.
  - *allow_repeat_after*: how many images the bot must have posted before it is allowed to repeat a picture.
  - *log_file*: full path to the log file. You probably want to use *BOT_PATH/logs/log*. 
  - *bot_account*: the username for the bot account. **DO** start with @.
  - *master_account*: the username which the bot will listen to for delete commands. **DO** start with @.
  - *dont_tweet_file*: full path to the banned images list file. You probably want to use *BOT_PATH/logs/banned*
- **[Orders]**
  - *ban_command*: if master_account tweets something starting with this, will delete last tweet and ban last image posted.
  - *request_command*: if anybody tweets something starting with this, it will give them a picture. If tweet has a "to @(userB)" in it somewhere *and* starts with the request_command, bot will interpret as a gift from user posting to userB.
  - *time_tolerance*: How old should a request be for it to be ignored? Do not set this to be less than the frequency with which you'll set the bot on cron.
- **[Texts]**
  - *tweet_post_number*: True/False. This will prepend your tweets with a text looking like "Nr. X" where X is your post number. Do read the [Backwards Compatibility](#backwards-compatibilty) section if you were using a previous version of the bot or if you will start using this bot in non empty twitter account. 
  - *tweet_this_text*: Just write whatever you want to be tweeted with your image. This will come after the post number, if you set tweet_post_number to True. This would most probably be a URL asociated with your bot, but you can set it to whatever you want. If you want nothing to customized text to be tweeted, just leave it blank 
  - *requests_answers*: bot will choose randomly from here when complying to request from a request_command with no "to @". the reply will look like "@user request_answer"
  - *requests_to_third_answers*: bot will choose ramdonly from here when complying to requests from a request_command with "to @" in it. the reply will look like "@userB request_to_third_answers @requester"


### Example
```
# Replace where appropriate with your own settings.

[Twitter]
api_key = your_api_key
secret_key = your_secret_key
token = your_token
secret_token = your_secret_token

[App]
image_folder = /home/botImages/
execution_chance = 1
allow_repeat_after = 50
log_file = /home/bot/logs/log
bot_account = @gentelindaOK
master_account = @amemulo
dont_tweet_file = /home/bot/logs/banned

[Orders]
#caps agnostic
ban_command = @gentelindaOK don't
request_command = dear @gentelindaOK
time_tolerance = 5

[Texts]
# Respect indentation: it is TWO spaces
# tweet_post_number is either True or False, nothing else
# tweet this text doesn't requiere "" or '', just write the text
tweet_post_number = True
tweet_this_text = 
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

Backwards Compatibilty
===============

Please note that if you were using a previous version of the bot you'll **have** to execute the bot once (and only once!) like this from the terminal after enabling the option. This is *specially* important if you want to use the tweet_post_number option.  

```python twitterbot.py --tweet --tweetnumber X```


Where X is the number of the tweet you'll post right now (that is, the
number of posts the bot has tweeted plus one, you can see the number so far
on tweeter). 

This will log that tweet in a way so that the bot can read
the post number from the log, so it will know now how many posts there
have been. The --tweet option is there just to force the bot to tweet
and ignore the execution chance.

If you don't do this, your log will register the bot's post_number wrongly, starting from one since you updated. Of course, if you use the tweet_post_number function, this'll mean the post numbers the bot tweetes will make no sense. 


Usage
===============

**Execute it.** That's it.

You also have a couple of useful arguments:

```
optional arguments:
  -h, --help  show this help message and exit
  --tweet     Ignores execution chance, always run
  --test      Wont't tweet, just write to log
  --postnumber Sets the post number to be posted if tweet_post_number is true. 
```

Live example and full automation idea
==============
You can check out [gentelindaOK](http://twitter.com/gentelindaOK) **(NSFW)** to see
a working account using this twitter bot.

@gentelindaOK is a fully automatic bot. My modified version of [RedditImageGrab
](https://github.com/joaquinlpereyra/RedditImageGrab)
downloads new images to my PC from a multireddit every morning. Then, a silly
one line bash command removes any image that is smaller than 50kb (to filter
glitches and very small pictures). This twitter bot is set up on cron
on my PC to execute every minute with a 1 percent execution chance set on the script's config file.
