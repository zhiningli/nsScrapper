from unittest import TestCase

from src import noe
from src.api import prices

class TestPrices(TestCase):
    def testGetOnePrice(self):

        botw = noe.game_info("70010000000023")
        self.assertEqual(botw.title,"The Legend of Zelda: Breath of the Wild")

        price = prices.get_price(botw, country="GB")
        self.assertEqual(price.nsuid, "70010000000023")
        self.assertEqual(price.value,59.99)
        self.assertEqual(price.sale_value, None)


    def testGetMultiplePrice(self):
        botw = noe.game_info("70010000000023")
        self.assertEqual(botw.title, "The Legend of Zelda: Breath of the Wild")
        totk = noe.game_info("70010000063715")
        self.assertEqual(totk.title, "The Legend of Zelda: Tears of the Kingdom")

        both_prices = prices.get_prices([botw, totk], country="GB")


        expected_info = [            
            ("70010000000023", 59.99, None),
            ("70010000063715", 59.99, None),
        ]
        count = 0
        for expected, (nsuid, price) in zip(expected_info, both_prices):
            expected_nsuid, expected_value, expected_sale_value = expected
            self.assertEqual(nsuid, expected_nsuid)
            self.assertEqual(price.value, expected_value)
            self.assertEqual(price.sale_value, expected_sale_value)

    



