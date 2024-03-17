from unittest import TestCase

from src import noj
from src.commons.enumerates import Platforms, Regions

LIMIT = 20


class TestListing(TestCase):
    def test_list_switch_games(self):
        index = 0

        for index, game in enumerate(noj.search_switch_game("ゼルダ")):
            if index > LIMIT:
                break

            self.assertEqual(game.platform, Platforms.NINTENDO_SWITCH)
            self.assertEqual(game.region, Regions.JP)

            if game.nsuid:
                self.assertTrue(game.nsuid.startswith("700"))

        self.assertNotEqual(index, 0)