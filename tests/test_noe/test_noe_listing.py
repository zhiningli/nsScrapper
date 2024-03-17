from unittest import TestCase

from src import noe
from src.commons.enumerates import Features, Ratings, Regions, Platforms


LIMIT = 20

class TestNoeListing(TestCase):

    def test_list_switch_games(self):
        for index, game in enumerate(noe.list_switch_games()):
            if index > LIMIT:
                break

            self.assertEqual(game.platform, Platforms.NINTENDO_SWITCH)
            self.assertEqual(game.region, Regions.EU)

            if game.nsuid:
                self.assertTrue(game.nsuid.startswith("700"))
