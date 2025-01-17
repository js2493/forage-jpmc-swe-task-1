import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock = quote['stock']
            bid = float(quote['top_bid']['price'])
            ask = float(quote['top_ask']['price'])
            price = (bid + ask) / 2
            self.assertEqual((stock, bid, ask, price), getDataPoint(quote))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock = quote['stock']
            bid = float(quote['top_bid']['price'])
            ask = float(quote['top_ask']['price'])
            price = (bid + ask) / 2
            self.assertEqual((stock, bid, ask, price), getDataPoint(quote))
    """ ------------ Add more unit tests ------------ """

    def test_getRatio(self):
        stock_a = 10
        stock_b = 5
        self.assertEqual(2,getRatio(stock_a, stock_b))

    def test_getRatio_stockBvalue0(self):
        self.assertIsNone(getRatio(10,0))


if __name__ == '__main__':
    unittest.main()
