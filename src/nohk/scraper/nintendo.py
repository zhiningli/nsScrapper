from typing import Iterator, Optional
import requests

from src.commons.enumerates import Platforms

SEARCH_URL = "https://ec.nintendo.com/HK/zh/titles/70010000009367"

HARDNAMES = {
    Platforms.NINTENDO_SWITCH: "1_HAC",
}


def _search(query: str = "", nsuid: str = None, platform: Platforms = None) -> Iterator[dict]:
    params = {"q": query, "limit": 150, "page": 0 ,"opt_hard": HARDNAMES.get(platform)}

    if nsuid:
        params["fq"] = f"id:{nsuid}"

    while True:
        params["page"] += 1
        response = requests.get(url=SEARCH_URL, params=params)

        if response.status_code != 200:
            break

        items = response.json()["result"]["items"]

        if not items:
            break

        yield from filter(
            lambda item: "_" not in item["id"],
            items,
        )

def search_by_nsuid(nsuid: str) -> Optional[dict]:
    try:
        return next(_search(nsuid = nsuid))
    except StopIteration:
        return None


def search_by_platform(platform: Platforms) -> Iterator[dict]:
    yield from _search(platform=platform)


def search_by_query(query: str, platform: Platforms = None) -> Iterator[dict]:
    yield from _search(query=query, platform=platform)
