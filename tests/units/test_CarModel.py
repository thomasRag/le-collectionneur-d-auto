import unittest
from api import CarModel
from api import app
from api import CarValidator
from unittest.mock import patch


class CarModelTestCase(unittest.TestCase):

    def test_list(self):
        app.CARS = [{'id': 3, 'key': 'value3'}, {'id': 2, 'key': 'value2'}, {'id': 1, 'key': 'value1'}]
        self.assertEqual(CarModel.list(), app.CARS)

    def test_get(self):
        app.CARS = [{'id': 3, 'key': 'value3'}, {'id': 2, 'key': 'value2'}, {'id': 1, 'key': 'value1'}]
        self.assertEqual(CarModel.get(3), {'id': 3, 'key': 'value3'})
        self.assertEqual(CarModel.get(4), False)

    def test_CarValidator(self):
        car_validator = CarValidator({'make':3})
        self.assertFalse(car_validator.get_is_valid())

    @patch('api.CarValidator.get_is_valid')
    def test_save(self, mock_is_valid):
        mock_is_valid.return_value = True
        app.CARS = []

        car = CarModel.save({'key': 'value1'})
        self.assertEqual(1, car['id'])
        self.assertEqual(app.CARS, [{'id': 1, 'key': 'value1'}])

        car = CarModel.save({'key': 'value2'})
        self.assertEqual(2, car['id'])

        app.CARS = [{'id': 3, 'key': 'value3'},{'id': 16, 'key': 'value2'}]

        car = CarModel.save({'key': 'value'})
        self.assertEqual(17, car['id'])

    def test_delete(self):
        app.CARS = [{'id': 1, 'key': 'value'}]

        self.assertEqual(False, CarModel.delete(2))
        self.assertEqual([{'id': 1, 'key': 'value'}], app.CARS)

        self.assertEqual(True, CarModel.delete(1))
        self.assertEqual([], app.CARS)


    @patch('api.CarValidator.get_is_valid')
    def test_update(self, mock_is_valid):

        app.CARS = [{'id': 1, 'key': 'old_value'},{'id': 3, 'key': 'old_value'}]
        car = CarModel.update(2, {'key': 'new_value'})
        self.assertEqual(False, car)
        self.assertEqual(app.CARS, [{'id': 1, 'key': 'old_value'},{'id': 3, 'key': 'old_value'}])

        mock_is_valid.return_value = True
        app.CARS = [{'id': 1, 'key': 'old_value'},{'id': 3, 'key': 'old_value'}]
        car = CarModel.update(1, {'key': 'new_value'})
        self.assertEqual(1, car['id'])
        self.assertEqual('new_value', car['key'])
        self.assertEqual(app.CARS, [{'id': 3, 'key': 'old_value'},{'id': 1, 'key': 'new_value'}])

        app.CARS = [{'id': 1, 'key': 'old_value'}]
        car = CarModel.update(2, {'key': 'new_value'})
        self.assertEqual(False, car)
        self.assertEqual(app.CARS, [{'id': 1, 'key': 'old_value'}])


if __name__ == '__main__':
    unittest.main()