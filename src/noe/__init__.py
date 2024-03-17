from src.commons.classes.node import Node

from .info import game_info
from .listing import list_switch_games
from .search import search_switch_game

class Noe:
    def __init__(self):
        super.__init__(Node)
        
Noe.game_info = staticmethod(game_info)
Noe.list_switch_games = staticmethod(list_switch_games)
Noe.search_switch_game = staticmethod(search_switch_game)