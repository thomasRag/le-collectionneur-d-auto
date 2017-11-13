import unittest
import json
from api import app
from unittest.mock import patch

class GetTestCase(unittest.TestCase):

    """
    test get_cars method:
        - get data from model
        - return code 200 whatever return by the model
        - response stream contains a json encoded value of what is return by the model
    """

    @patch('api.CarModel.list')
    def test_get_cars(self, mock_cars):

        def test_get_cars_base(mock_cars_return):
            mock_cars.return_value = mock_cars_return
            response = app.test_client(self).get('/cars')
            mock_cars.assert_called_with()
            self.assertEqual(response.status_code, 200)
            responseString = response.data.decode("utf-8");
            self.assertEqual( json.loads(responseString), mock_cars_return)

        test_get_cars_base([])
        test_get_cars_base(['toto'])
        test_get_cars_base('')
        test_get_cars_base([{}])


if __name__ == '__main__':
    unittest.main()