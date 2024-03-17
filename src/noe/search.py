from typing import Iterator

from src.commons.classes.games import Game
from src.commons.enumerates import Platforms
from src.noe.api import nintendo
from src.noe.util import build_game

def search_game(query: str, platform: Platforms) -> Iterator[Game]:
    for data in nintendo.search_by_query(query, platform):
        yield build_game(data)


def search_switch_game(query: str) -> Iterator[Game]:
    """
    Search for Nintendo Switch Game in the EU region

    Available Features
    ----------------------------
        * AMIIBO
        * DEMO
        * DLC
        * GAME_VOUCHER
        * ONLINE_PLAY
        * SAVE_DATA_CLOUD
        * VOICE_CHAT


    Parameters
    -----------------------------
    query: str
        Text to search

    Yields
    ------------------------------
    Information of a game in format commons.Game
    """


    yield from search_game(query, Platforms.NINTENDO_SWITCH)


