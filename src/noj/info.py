from typing import Optional

from src.commons.classes.games import Game
from src.noj.api import nintendo
from src.noj.util import build_game


def game_info(nsuid: str) -> Optional[Game]:
    """
    Given a game's `nsuid` for the JP region, it will retrieve its information
    from Nintendo of Japan.

    Available Features
    ------------------
        * Nintendo Switch
            - AMIIBO
            - DLC
            - ONLINE_PLAY

    Parameters
    ----------
    nsuid: str
        Valid nsuid of a nintendo game.

    Returns
    -------
    nintendeals.classes.common.Game:
        Information of the game.
    """

    data = nintendo.search_by_nsuid(nsuid)
    return build_game(data) if data else None