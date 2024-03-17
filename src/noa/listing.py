from typing import Iterator

from src.commons.classes.games import Game
from src.commons.enumerates import Platforms
from src.noa.api import algolia
from src.noa.util import build_game


def list_games(platform: Platforms) -> Iterator[Game]:
    for data in algolia.search_by_platform(platform):
        yield build_game(data)


def list_switch_games() -> Iterator[Game]:
    """
    Get a list of Nintendo Switch games for the NA region.

    Note: game.product_code is unavailable with this method, to get it use the
    method noa.game_info(nsuid).

    Available Features
    ------------------
        * DEMO
        * GAME_VOUCHER
        * ONLINE_PLAY
        * SAVE_DATA_CLOUD

    Yields
    -------
    nintendeals.classes.common.Game:
        Information of a game.
    """
    yield from list_games(Platforms.NINTENDO_SWITCH)