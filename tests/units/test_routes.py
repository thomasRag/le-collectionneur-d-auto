import unittest
import json
from api import app
from unittest.mock import patch

class RoutesTestCase(unittest.TestCase):

    """
    test get_cars method:
        - get data from model
        - return code 200
        - response stream contains a json encoded value of what is return by the model
    """

    @patch('api.CarModel.list')
    def test_get_cars(self, mock_cars):

        def test_get_cars_base(mock_cars_return):

            mock_cars.return_value = mock_cars_return
            response = app.test_client(self).get('/cars')

            mock_cars.assert_called_with()
            self.assertEqual(response.status_code, 200)
            response_string = response.data.decode("utf-8")
            self.assertEqual(json.loads(response_string), mock_cars_return)

        test_get_cars_base([])
        test_get_cars_base(['car1', 'car2'])

    """
    test get_cars method:
        - get data from model
        - return code 200 
        - response stream contains a json encoded value of what is return by the model
    """

    @patch('api.CarModel.get')
    def test_get_car(self, mock_car_get):

        mock_car_get.return_value = "car1"
        response = app.test_client(self).get('/cars/3')

        mock_car_get.assert_called_with(3)
        self.assertEqual(response.status_code, 200)
        response_string = response.data.decode("utf-8")
        self.assertEqual(json.loads(response_string), "car1")

        mock_car_get.return_value = False
        response = app.test_client(self).get('/cars/12')

        mock_car_get.assert_called_with(12)
        self.assertEqual(response.status_code, 404)
        response_string = response.data.decode("utf-8")
        self.assertEqual(json.loads(response_string), {"error": "not found"})

    @patch('api.CarModel.save')
    def test_create_car(self, mock_car_save):

        mock_car_save.return_value = {"key":"value"}
        response = app.test_client(self).post('/cars', data='{"key":"value"}')
        self.assertEqual(response.status_code, 201)
        response_string = response.data.decode("utf-8")
        self.assertEqual(json.loads(response_string), {"key":"value"})

        mock_car_save.return_value = {"errors": ["test errors"]}
        response = app.test_client(self).post('/cars', data='{"key":"value"}')
        self.assertEqual(response.status_code, 422)

    @patch('api.CarModel.update')
    def test_update_car(self, mock_car_update):
        mock_car_update.return_value = {"id": 1, "key":"new_value"}

        response = app.test_client(self).put('/cars/1', data='{"key":"new_value"}')
        response_string = response.data.decode("utf-8")
        self.assertEqual(json.loads(response_string), {"id": 1, "key":"new_value"})
        self.assertEqual(response.status_code, 200)

        mock_car_update.return_value = {"errors": ["test errors"]}
        response = app.test_client(self).put('/cars/1', data='{"key":"new_value"}')
        self.assertEqual(response.status_code, 422)

        mock_car_update.return_value = False
        response = app.test_client(self).put('/cars/1', data='{"key":"new_value"}')
        self.assertEqual(response.status_code, 404)

    @patch('api.CarModel.delete')
    def test_delete_car(self, mock_car_delete):
        mock_car_delete.return_value = False
        response = app.test_client(self).delete('/cars/1')
        self.assertEqual(response.status_code, 404)
        response_string = response.data.decode("utf-8")
        self.assertEqual(response_string, '')

        mock_car_delete.return_value = True
        response = app.test_client(self).delete('/cars/1')
        self.assertEqual(response.status_code, 204)
        response_string = response.data.decode("utf-8")
        self.assertEqual(response_string, '')

if __name__ == '__main__':
    unittest.main()