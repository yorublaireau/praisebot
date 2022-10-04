import tweepy
import os
import sys
import logging
import random

from search import does_text_says_praise_me, get_mentions

LOG_LEVEL = os.environ.get("LOG_LEVEL") or logging.INFO
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ACCESS_KEY_TOKEN = os.environ["ACCESS_KEY_TOKEN"]
ACCESS_KEY_SECRET = os.environ["ACCESS_KEY_SECRET"]

logging.basicConfig(stream=sys.stderr, level=LOG_LEVEL)

logger = logging.getLogger(__name__)

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_KEY_TOKEN, ACCESS_KEY_SECRET)

api = tweepy.API(auth)

logger.info("Connecting to Twitter API...")
bot_user = api.verify_credentials()

praises = [
    "you're the best 👏👏👏",
    "you are incredible! 😇",
    "you are majestic ✨✨✨",
    "please continue to be fantastic ✨",
    "your presence brings us joy ⭐️",
    "don't you need a license for that level of awesomeness? ✨",
    "you light up the room 💡",
    "you are way cool",
    "you were cool before cool was a thing",
    "you are appreciated! 🌟",
    "you're better than a triple-scoop ice cream. 🍦 (with sprinkles)",
]


def praise(target):
    praise_text = random.sample(praises, 1)[0]

    praise_tweet = f"@{target} {praise_text}"
    logger.info("praising: %s", praise_tweet)
    api.update_status(praise_tweet)


class PraiseStream(tweepy.Stream):
    def on_status(self, status):
        logger.info("@%s >> %s", status.user.screen_name, status.text)
        api.create_favorite(status.id)

        has_praised = False

        if does_text_says_praise_me(status.text):
            praise(status.user.screen_name)
            has_praised = True

        for mention in get_mentions(status.text, bot_user.screen_name):
            praise(mention)
            has_praised = True

        if not has_praised:
            api.update_status(
                status="Oops, I don't know who to praise here! 👀 Tweet me with a list of names or the words 'praise me'",
                in_reply_to_status_id=status.id_str,
                auto_populate_reply_metadata=True,
            )


logger.info(f"Connected as @{bot_user.screen_name}")

mention_streams = PraiseStream(API_KEY, API_SECRET, ACCESS_KEY_TOKEN, ACCESS_KEY_SECRET)
mention_streams.filter(track=[f"@{bot_user.screen_name}"])
