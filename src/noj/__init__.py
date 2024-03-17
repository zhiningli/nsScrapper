from src.commons.classes.node import Node

from .info import game_info
from .listing import list_switch_games
from .search import search_switch_game

class Noj:
    def __init__(self):
        super.__init__(Node)
        
Noj.game_info = staticmethod(game_info)
Noj.list_switch_games = staticmethod(list_switch_games)
Noj.search_switch_game = staticmethod(search_switch_game)