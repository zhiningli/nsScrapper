from datetime import datetime
from typing import Dict

from src.commons.classes.games import Game
from src.commons.enumerates import Features, Platforms, Ratings, Regions


PLATFORM = {
    "1_HAC": Platforms.NINTENDO_SWITCH,
}


def build_game(data: dict) -> Game:
    hard = data.get("hard")
    icode = data.get("icode")

    if hard and icode:
        product_code = hard[2:] + icode
    else:
        product_code = None

    game = Game(
        platform=PLATFORM[hard],
        region = Regions.JP,
        title = data["title"],
        nsuid = data.get("nsuid"),
        product_code = product_code,
    )

    game.description = data.get("text")
    game.slug = data.get("icode")
    game.free_to_play = data.get("price") == 0.0

    players = data.get("player") or ["0"]
    game.players = max(map(int, players[0].split("~")))

    try:
        game.release_date = datetime.strptime(data.get("sdate"), "%Y.%m.%d")
    except (ValueError, TypeError):
        game.release_date = None

    game.categories = data.get("genre", [])

    developer = data.get("maker")
    game.developers = [developer] if developer else []

    game.languages = data.get("lang", [])

    publisher = data.get("publisher")
    game.publishers = publisher if publisher else []

    rating = data.get("cero") or ["0"]
    game.rating = (Ratings.CERO, rating[0])

    game.features = {
        Features.AMIIBO: data.get("amiibo", "0") == "1",
        Features.DLC: len(data.get("cnsuid") or []) > 0,
        Features.ONLINE_PLAY: (data.get("nso") or ["0"]) == ["1"],
    }

    return game