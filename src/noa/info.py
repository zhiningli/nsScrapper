from typing import Optional

from src.commons.classes.games import Game
from src.noa.api import algolia
from src.noa.scraper import nintendo
from src.noa.util import build_game


def game_info_by_nsuid(nsuid: str) -> Optional[Game]:
    data = algolia.search_by_nsuid(nsuid)

    if not data:
        return None

    data["extra"] = nintendo.scrap(data["urlKey"])

    return build_game(data)


def game_info_by_slug(slug: str) -> Optional[Game]:
    extra = nintendo.scrap(slug)
    nsuid = extra.get("nsuid")

    if not nsuid:
        return None

    data = algolia.search_by_nsuid(nsuid)

    if not data:
        return None

    data["extra"] = extra

    return build_game(data)


def game_info(nsuid: str = None, slug: str = None) -> Optional[Game]:
    """
    Given a game's `nsuid` or url `slug` for the NA region, it will retrieve
    its information from Nintendo of America.

    Available Features
    ------------------
        * Nintendo Switch
            - DEMO
            - DLC
            - GAME_VOUCHER
            - ONLINE_PLAY
            - SAVE_DATA_CLOUD

    Parameters
    ----------
    nsuid: str
        Valid nsuid of a nintendo game.
    slug: str
        Valid slug from NA's eShop.

    Returns
    -------
    nintendeals.classes.common.Game:
        Information of the game.
    """

    if nsuid:
        return game_info_by_nsuid(nsuid)

    if slug:
        return game_info_by_slug(slug)

    return None