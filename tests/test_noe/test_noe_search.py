from unittest import TestCase

from src import noe
from src.commons.enumerates import Features, Ratings, Regions, Platforms


LIMIT = 20


class TestNoeSearch(TestCase):

    'Testing noe.search.py'
    def test_seasrh_switch_games(self):
        index = 0

        for index, game in enumerate(noe.search_switch_game("Zelda")):
            if index > LIMIT:
                break

            self.assertEqual(game.platform, Platforms.NINTENDO_SWITCH)
            self.assertEqual(game.region, Regions.EU)

            if game.nsuid:
                self.assertTrue(game.nsuid.startswith("700"))

        self.assertNotEqual(index, 0)