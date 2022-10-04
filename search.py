import re
import logging

logger = logging.getLogger(__name__)


def does_text_says_praise_me(text):
    if re.search(r"\s+praise\s+me\s*$", text) is not None:
        return True
    return False


def get_mentions(text, bot_name):
    for mention in re.finditer(r"\s@(\w+)\b", text):
        target = mention.group(1)
        if target == bot_name:
            logger.debug("skipping self mention")
            continue
        yield target
