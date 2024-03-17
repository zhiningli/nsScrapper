from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

from src.api.prices import get_price
from src.commons.classes.eshops import EUeShop, JPeShop, NAeShop, HKeShop
from src.commons.classes.prices import Price
from src.commons.enumerates import(
    Features,
    Platforms,
    Ratings,
    Regions,
)

ESHOPS = {
    Regions.EU : EUeShop,
    Regions.JP : JPeShop,
    Regions.NA : NAeShop,
    Regions.HK : HKeShop,
}


class Game:
    def __init__(
        self, 
        platform: Platforms,
        region: Regions,
        title: str,
        nsuid: str = None,
        product_code: str = None,
    ):
        self.platform: Platforms = platform
        self.region: Regions = region
        self.title: str = title
        self.nsuid: str = nsuid
        self.product_code: str = product_code


        self.description: Optional[str] = None
        self.slug: Optional[str] = None

        self.players: int = 0

        self.free_to_play: Optional[bool] = None

        self.release_date: Optional[datetime] = None

        self.categories: List[str] = []
        self.developers: List[str] = []
        self.languages: List[str] = []
        self.publishers: List[str] = []

        self.rating: Optional[Tuple[Ratings, Any]] = None

        self.features: Dict[Features, Any] = {}


    @property
    def unique_id(self) -> Optional[str]:
        if not self.product_code:
            return None
        if self.region == Regions.JP:
            return self.product_code[0][3:-1]
        elif self.region == Regions.EU:
            return self.product_code[0][4:-1]
        elif self.region == Regions.NA:
            return self.product_code[4:-1]
        else:
            pass

    @property
    def eshop(self) -> Union[EUeShop, JPeShop, NAeShop, HKeShop]:
        return ESHOPS[self.region](self)
    
    def price(self, country: str) -> Price:
        return get_price(country = country, game=self)
    
    def __repr__(self):
        return self.title