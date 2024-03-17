from src.commons.classes.node import Node

from .info import game_info
from .listing import list_switch_games
from .search import search_switch_game

class Noa:
    def __init__(self) -> None:
        super.__init__(Node)


Noa.game_info = staticmethod(game_info)
Noa.list_switch_games = staticmethod(list_switch_games)
Noa.search_switch_game = staticmethod(search_switch_game)

