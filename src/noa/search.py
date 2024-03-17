from typing import Iterator

from src.commons.classes.games import Game
from src.commons.enumerates import Platforms
from src.noa.api import algolia
from src.noa.util import build_game


def search_games(query: str, platform: Platforms) -> Iterator[Game]:
    for data in algolia.search_by_query(query, platform):
        yield build_game(data)


def search_switch_game(query: str) -> Iterator[Game]:
    """
    Search for Nintendo Switch games in the NA region.

    Note: game.product_code is unavailable with this method, to get it use the
    method noa.game_info(nsuid).

    Available Features
    ------------------
        * DEMO
        * GAME_VOUCHER
        * ONLINE_PLAY
        * SAVE_DATA_CLOUD

    Parameters
    ----------
    query: str
        Text to search.

    Yields
    -------
    nintendeals.classes.common.Game:
        Information of a game.
    """

    yield from search_games(query, Platforms.NINTENDO_SWITCH)