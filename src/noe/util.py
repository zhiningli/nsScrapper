from datetime import datetime
from typing import Dict

from src.commons.classes.games import Game
from src.commons.enumerates import Features, Platforms, Ratings, Regions

NSUIDS = {
    "700": Platforms.NINTENDO_SWITCH,
}

PLATFORMS = {
    "HAC": Platforms.NINTENDO_SWITCH,
}


def build_game(data:Dict) -> Game:
    nsuid = data.get("nsuid_txt")
    product_code = data.get("product_code_txt")

    if not product_code:
        product_code = None

    if nsuid:
        platform = NSUIDS[nsuid[:3]]
    elif product_code:
        platform = PLATFORMS[product_code[0][:3]]
    else:
        platform = PLATFORMS[data["playable_on_txt"][0]]

    game = Game(
        platform=platform,
        region = Regions.EU,
        title = data["title"],
        nsuid = nsuid,
        product_code = product_code,
    )


    game.description = data.get("excerpt")
    game.slug = data.get("url")
    game.players = data.get("players_to", 0)
    game.free_to_play = data.get("price_regular_f") == 0.0

    try:
        game.release_date = datetime.strptime(data.get("pretty_date_s"), "%d/%m/%Y")
    except (ValueError, TypeError):
        game.release_date = None

    game.categories = data.get("game_categories_txt", [])
    
    developer = data.get("developer")
    game.developers = [developer] if developer else []

    languages = data.get("language_availability")
    game.languages = list(map(str.title, languages[0].split(","))) if languages else []

    publisher = data.get("publisher")
    game.publishers = [publisher] if publisher else []

    game.rating = (Ratings.PEGI, data.get("age_rating_sorting_i"))

    game.features = {
        Features.AMIIBO: data.get("near_field_comm_b", False),
        Features.DEMO: data.get("demo_availability", False),
        Features.DLC: data.get("add_on_content_b", False),
        Features.GAME_VOUCHER: data.get("switch_game_voucher_b", False),
        Features.ONLINE_PLAY: data.get("paid_subscription_required_b", False),
        Features.SAVE_DATA_CLOUD: data.get("cloud_saves_b", False),
        Features.VOICE_CHAT: data.get("voice_chat_b", False),
    }


    return game

