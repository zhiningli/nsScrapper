from datetime import datetime
from typing import Iterable, Iterator, Optional, Tuple, List

import requests
from dateutil.parser import parse 

from src.commons.classes.prices import Price
from src.commons.enumerates import Regions

def _parse_date(string: str) -> datetime:
    return parse(string).replace(tzinfo=None)


def fetch_prices(country: str, nsuids: Iterable[str]) -> Iterator[Tuple[str, Price]]:
    nsuids = set(nsuids)

    if not 51 > len(nsuids) > 0:
        raise ValueError("The amount of nsuids must between 1 and 50.")

    response = requests.get(
        url="https://api.ec.nintendo.com/v1/price",
        params=dict(
            country=country,
            lang="en",
            ids=",".join(nsuids),
        ),
    )

    response.raise_for_status()

    for data in response.json().get("prices", []):
        nsuid = str(data["title_id"])
        regular_price = data.get("regular_price")

        if not regular_price:
            continue

        price = Price(
            nsuid=nsuid,
            country=country,
            currency=regular_price["currency"],
            value=float(regular_price["raw_value"]),
        )

        discount_price = data.get("discount_price")

        if discount_price:
            price.sale_value = float(discount_price["raw_value"])
            price.sale_start = _parse_date(discount_price["start_datetime"])
            price.sale_end = _parse_date(discount_price["end_datetime"])

        yield price.nsuid, price

def get_prices(games, country: str) -> Iterator[Tuple[str, Price]]:
    """
    Parameters
    -------------
    games: Iterable[commons.classes.games.Game]
    country: str

    Yields
    --------------
    Tuple[str, commons.classes.prices.Price]
    """

    prices = {}
    chunk = []


    for game in games:
        chunk.append(game)


        if len(chunk) == 50:
            fetched = {
                nsuid: price
                for nsuid, price in fetch_prices(
                    country = country,
                    nsuids = [game.nsuid for game in chunk]
                )
            }
            prices.update(fetched)

            chunk = []
        
        if chunk:
            fetched = {
                nsuid: price
                for nsuid, price in fetch_prices(
                    country = country,
                    nsuids = [game.nsuid for game in chunk],
                )                
            }
            prices.update(fetched)
    yield from prices.items()
        


def get_price(game, country: str) -> Optional[Price]:
    """
    Parameters
    -------------------
    game: commons.classes.games.Game
    country: str

    Returns
    ---------------
    classes.commons.prices.Price
    """

    fetched = {
        nsuid: price
        for nsuid, price in fetch_prices(
            country=country,
            nsuids=[game.nsuid],
        )
    }

    return fetched.get(game.nsuid)


def get_prices_multiple_regions(gameName: str): 
    """
    Parameters
    -------------
    games: commons.
    country: str

    Yields
    --------------
    Tuple[str, commons.classes.prices.Price]
    """
    from src import noa, noe, noj   
    prices = []

    countries = {
        Regions.NA: ["US", "CA"],
        Regions.EU: ["CZ","GB","DE","RU","ZA", "AU", "NZ", "CH"],
        Regions.JP: ["JP"]
    }


    game_country_pairs = []
    count = 0

    print("Querying to EU server...")

    print("Querying to NA server...")

    for game in noa.search_switch_game(query=gameName):
        count += 1
        if count > 5:
            break
        for country in countries[Regions.NA]:
            game_country_pairs.append((game, country))

    print("Querying to JP server...")
    for game in noj.search_switch_game(query=gameName):
        count += 1
        if count > 10:
            break
        for country in countries[Regions.JP]:
            game_country_pairs.append((game, country))

    for game in noe.search_switch_game(query=gameName):
        count += 1
        if count > 20:
            break
        for country in countries[Regions.EU]:
            game_country_pairs.append((game, country))
            
    print(f"Total {count} games scrapped.")

    prices_info = []

    print("Fetching Prices...")

    for game, country in game_country_pairs:
        if game.nsuid:
            fetched_price = list(fetch_prices(country=country, nsuids=[game.nsuid]))
            if fetched_price:
                game_price_info = [game.title, country, fetched_price[0][0], fetched_price[0][1]]
                prices_info.append(game_price_info)

    return prices_info


def convert_prices_to_USD(prices_info: Optional[List], XR: dict):
    for price_info in prices_info:
        curr = price_info[3]
        USD_equiv = curr.value / XR[curr.currency]
        USD_price = Price(price_info[2], price_info[1], "USD", USD_equiv)
        price_info.append(USD_price)
    return prices_info