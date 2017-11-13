import unittest
import json
from api import CarModel
from api import app


class CarModelTestCase(unittest.TestCase):

    def test_list(self):
        app.CARS = [1, 2, 3]
        self.assertEqual(CarModel.list(self), [1,2,3])


if __name__ == '__main__':
    unittest.main()