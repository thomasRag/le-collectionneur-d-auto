import unittest
import json
from api import CarModel
from api import app
from api import CarValidator
from unittest.mock import patch


class CarModelTestCase(unittest.TestCase):

    def test_list(self):
        app.CARS = [1, 2, 3]
        self.assertEqual(CarModel.list(), [1,2,3])

    def test_get(self):
        app.CARS = [1, 2, 3]
        self.assertEqual(CarModel.get(1), 1)
        self.assertEqual(CarModel.get(4), False)

    def test_CarValidator(self):
        carValidator = CarValidator({'make':3})
        self.assertFalse(carValidator.is_valid)

    @patch('api.CarValidator.get_is_valid')
    def test_save(self, mock_is_valid):
        mock_is_valid.return_value = True
        app.CARS = []

        car = CarModel.save({'key': 'value1'})
        self.assertEqual(1, car['id'])
        self.assertEqual(app.CARS, [{'id': 1, 'key': 'value1'}])

        car = CarModel.save({'key': 'value2'})
        self.assertEqual(2, car['id'])

        app.CARS = [{'id': 3, 'key': 'value2'},{'id': 16, 'key': 'value2'}]

        car = CarModel.save({'key': 'value'})
        self.assertEqual(17, car['id'])


if __name__ == '__main__':
    unittest.main()