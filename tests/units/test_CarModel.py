import unittest
import json
from api import CarModel
from api import app


class CarModelTestCase(unittest.TestCase):

    def test_list(self):
        app.CARS = [1, 2, 3]
        self.assertEqual(CarModel.list(), [1,2,3])

    def test_get(self):
        app.CARS = [1, 2, 3]
        self.assertEqual(CarModel.get(1), 1)
        self.assertEqual(CarModel.get(4), False)

if __name__ == '__main__':
    unittest.main()