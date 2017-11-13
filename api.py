from flask import Flask, jsonify, make_response, request
from cerberus import Validator
import json

app = Flask(__name__)

app.CARS = []

class CarValidator:
    schema = {}
    def __init__(self, car_object):
        if not self.schema:
            self.schema = {
                "description": {
                    "type": 'string',
                    "required": True
                },
                "make": {
                    "type": 'string',
                    "required": True
                },
                "displacement": {
                    "type": 'float',
                    "required": True
                },
                "year": {
                    "type": 'integer',
                    "required": True
                },
                "owner": {
                    "type": 'string',
                    "required": True
                },
                "media": {
                    "type": 'string',
                    "required": True
                }
            }

            self.schema = {
                "description": {
                    "type": 'string',
                    "required": True
                }
            }

        v = Validator(self.schema)
        try:
            self.is_valid = v.validate(car_object);
        except Exception:
            print(Exception)
        if not self.is_valid:
            self.errors = v._errors
        else:
            self.errors = None
    def get_is_valid(self):
        return self.is_valid
class CarModel:

    @staticmethod
    def list():
        return app.CARS

    @staticmethod
    def get(id):
        try:
            result = app.CARS[id - 1]
        except IndexError:
            result = False
        return result

    @staticmethod
    def save(car):
        validator = CarValidator(car)
        if not validator.get_is_valid():
            return {'errors': ['unprocessable entity']}
        existing_ids =  [CAR['id'] for CAR in app.CARS]
        if existing_ids:
            new_id = max(existing_ids) + 1
        else:
            new_id = 1
        car['id'] = new_id
        app.CARS.append(car)
        return car

    @staticmethod
    def remove(id):
        pass



@app.route("/cars", methods=['GET'])
def get_cars():
    cars = CarModel.list()
    return make_response(jsonify(cars), 200)


@app.route("/cars/<int:id>", methods=['GET'])
def get_car(id):
    car = CarModel.get(id)
    if not car:
        return make_response(jsonify({'error':'not found'}), 404)
    return make_response(jsonify(car), 200)


@app.route("/cars", methods=['POST'])
def create_car():
    request_body = request.data.decode("utf-8")
    data = json.loads(request_body)
    result = CarModel.save(data)
    if "errors" in result:
        return make_response(jsonify({'errors': result["errors"]}), 422)
    return make_response(jsonify(data), 201)


@app.route("/cars/<int:id>", methods=['PUT'])
def update_car():
    pass


@app.route("/cars/<int:id>", methods=['DELETE'])
def remove_car():
    pass

if __name__ == '__main__':
    app.run(debug=True)
