from typing import Iterator

from src.commons.classes.games import Game
from src.commons.enumerates import Platforms
from src.noe.api import nintendo
from src.noe.util import build_game


def list_games(platform: Platforms) -> Iterator[Game]:
    for data in nintendo.search_by_platform(platform):
        yield build_game(data)


def list_switch_games() -> Iterator[Game]:
    """
    Get a list of Nintendo Switch games for the EU region.

    Available Features
    ------------------
        * AMIIBO
        * DEMO
        * DLC
        * GAME_VOUCHER
        * ONLINE_PLAY
        * SAVE_DATA_CLOUD
        * VOICE_CHAT

    Yields
    -------
    nintendeals.classes.common.Game:
        Information of a game.
    """
    yield from list_games(Platforms.NINTENDO_SWITCH)