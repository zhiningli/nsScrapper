from src.commons.classes.node import Node

from .info import game_info
from .listing import list_switch_games
from .search import search_switch_game

class Nohk:
    def __init__(self) -> None:
        super.__init__(Node)

Nohk.game_info = staticmethod(game_info)
Nohk.list_switch_games = staticmethod(list_switch_games)
Nohk.search_switch_game = staticmethod(search_switch_game)
