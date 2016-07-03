import twitterbot
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import mock_open

class TestMainFunction(unittest.TestCase):
    """Test the twitterbot.main function"""

    # so many I/O and side efects :( gave up on testing for random
    @patch('sys.argv', ['script_name', '--tweet'])
    @patch('twitterbot.get_post_number', return_value=0)
    @patch('twitterbot.create_tweet_text', return_value='automatic testing')
    @patch('twitterbot.orders', return_value='orders? im a test idiot')
    @patch('twitterbot.config.api', 'whatever')
    @patch('twitterbot.config.chance', 50)  # this one actually matters
    @patch('twitterbot.config.tweet_this_text', 'whatever')
    @patch('twitterbot.config.tweet_post_number', 'whatever')
    def test_tweet_sane_values(self, _, __, ___):
        """Tests if the tweet is sent to twitterbot.create_tweet with
        the values it should.
        """
        mock_create_tweet = MagicMock()
        mock_create_tweet.return_value = True
        with patch('twitterbot.create_tweet', mock_create_tweet):
            twitterbot.main()
        mock_create_tweet.assert_called_once_with('automatic testing', None, False)

    @patch('sys.argv', ['script_name', '--tweet'])
    @patch('twitterbot.get_post_number', return_value=0)
    @patch('twitterbot.create_tweet_text', return_value='automatic testing')
    @patch('twitterbot.orders', return_value='orders? im a test idiot')
    @patch('twitterbot.config.api', 'whatever')
    @patch('twitterbot.config.chance', 50)  # this one actually matters
    @patch('twitterbot.config.tweet_this_text', 'whatever')
    @patch('twitterbot.config.tweet_post_number', 'whatever')
    @patch('twitterbot.config.log_file', 'log_file')
    @patch('twitterbot.logger.add_warning_to_log', return_value=True)
    def test_log_if_tweet_not_successful(self, _, __, ___, _____):
        mock_create_tweet = MagicMock()
        mock_create_tweet.return_value = False
        mock_add_warning_to_log = MagicMock()
        patch_create_tweet = patch('twitterbot.create_tweet', mock_create_tweet)
        patch_add_warning_to_log = patch('twitterbot.logger.add_warning_to_log', mock_add_warning_to_log)
        with patch_add_warning_to_log, patch_create_tweet:
            twitterbot.main()
        mock_create_tweet.assert_called_once_with('automatic testing', None, False)
        warning_string = "!CRITICAL! No non-repeated or non-banned images found"
        mock_add_warning_to_log.assert_called_once_with(0, warning_string, 'log_file')




class TestTweetText(unittest.TestCase):
    """Tests for the twitterbot.create_tweet_text function"""

    def test_without_post_number(self):
        text = twitterbot.create_tweet_text('test text', 0, False)
        self.assertEqual(text, 'test text')

    def test_with_post_number(self):
        text = twitterbot.create_tweet_text('test text', 0, True)
        self.assertEqual(text, 'No. 0 test text')

    def test_empty_tweet_this_text_without_post_number(self):
        text = twitterbot.create_tweet_text('', 0, False)
        self.assertEqual(text, '')

    def test_empty_tweet_this_text_with_post_number(self):
        text = twitterbot.create_tweet_text('', 0, True)
        self.assertEqual(text, 'No. 0')


class TestGetTweetNumber(unittest.TestCase):
    """Tests for the twitterbot.get_post_number function"""

    def test_manual_post_number_is_not_None(self):
        post_number = twitterbot.get_post_number(5)
        self.assertEqual(post_number, 5)

    def test_manual_post_number_is_None(self):
        # avoid dealing with the actual log by patching get_post_number_from_log
        with patch('twitterbot.get_post_number_from_log', return_value=5):
            post_number = twitterbot.get_post_number(None)
            self.assertEqual(post_number, 5)


class TestGetPostNumberFromLog(unittest.TestCase):
    """Tests for the twitterbot.get_post_number_from_log function."""

    def test_log_with_at_least_an_entry(self):
        fake_log = (
            "948\t749421180906536960\t2016-07-02 22:55:02.178206\t/home/u/imgs/3.jpg\tNone\n"
            "949\t749426484322918400\t2016-07-02 23:16:02.080331\t/home/u/imgs/2.jpg\tNone\n"
            "950\t749447858588381184\t2016-07-03 00:41:01.872862\t/home/u/imgs/1.jpg\tNone\n"
        )

        with patch('builtins.open', mock_open(read_data=fake_log)) as fake_log:
            post_number = twitterbot.get_post_number_from_log('whatever_im_mocking')
        self.assertEqual('951', post_number)

    def test_log_with_no_entries(self):
        fake_log = ""
        with patch('builtins.open', mock_open(read_data=fake_log)) as fake_log:
            post_number = twitterbot.get_post_number_from_log('whatever_im_mocking')
        self.assertEqual(post_number, "1")

