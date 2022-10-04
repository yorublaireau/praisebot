import pytest

import search

praise_data = [
    "@praiserbot praise me",
    "@praiserbot praise     me",
    "@praiserbot praise me    ",
    "@praiserbot    praise     me    ",
    "what if I didn't take you to praise me",
]


@pytest.mark.parametrize("text", praise_data)
def test_text_says_praise_me(text):
    assert search.does_text_says_praise_me(text) is True


not_praise_data = [
    "something different",
    "@praiserbot what's up my guy praise the shit out of me",
    "@praiserbot praise me and my family"
]


@pytest.mark.parametrize("text", not_praise_data)
def test_text_doesnt_say_praise_me(text):
    assert search.does_text_says_praise_me(text) is False


def test_mentions_dont_return_bot_name():
    mentions = list(search.get_mentions("@praiserbot", "praisebot"))
    assert len(mentions) is 0


praise_others_data = [
    ("@praiserbot praise @rwnx", ["rwnx"]),
    ("@praiserbot praise @yorublaireau and @rwnx", ["yorublaireau", "rwnx"])
]


@pytest.mark.parametrize("text,praise_list", praise_others_data)
def test_text_praise_others(text, praise_list):
    mentions = list(search.get_mentions(text, "praisebot"))
    assert mentions == praise_list
