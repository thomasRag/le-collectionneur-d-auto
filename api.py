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

        v = Validator(self.schema)
        self.is_valid = v.validate(car_object)

    def get_is_valid(self):
        return self.is_valid


class CarModel:

    @staticmethod
    def list():
        return app.CARS

    @staticmethod
    def get(id):
        items = list(filter(lambda x: x['id'] == id, app.CARS))
        try:
            result = items.pop()
        except IndexError:
            result = False
        return result

    @staticmethod
    def save(car, id = False):
        validator = CarValidator(car)
        if not validator.get_is_valid():
            return {'errors': ['unprocessable entity']}
        if not id:
            existing_ids = [CAR['id'] for CAR in app.CARS]
            if existing_ids:
                id = max(existing_ids) + 1
            else:
                id = 1
        car['id'] = id
        app.CARS.append(car)
        return car

    @staticmethod
    def update(id, car):
        old_car = CarModel.get(id)
        if not old_car:
            return False
        CarModel.delete(id)
        return CarModel.save(car, id)

    @staticmethod
    def delete(id):

        def has_id(item_tuple, id):
            return item_tuple[1]['id'] == id

        if not CarModel.get(id):
            return False

        [index, item] = next(filter(lambda CAR: has_id(CAR, id), enumerate(app.CARS)))
        del app.CARS[index]
        return True


@app.route("/cars", methods=['GET'])
def get_cars():
    cars = CarModel.list()
    return make_response(jsonify(cars), 200)


@app.route("/cars/<int:id>", methods=['GET'])
def get_car(id):
    car = CarModel.get(id)
    if not car:
        return make_response(jsonify({'error': 'not found'}), 404)
    return make_response(jsonify(car), 200)


@app.route("/cars", methods=['POST'])
def create_car():
    request_body = request.data.decode("utf-8")
    data = json.loads(request_body)
    result = CarModel.save(data)
    if "errors" in result:
        return make_response(jsonify({'errors': result["errors"]}), 422)
    return make_response(jsonify(result), 201)


@app.route("/cars/<int:id>", methods=['PUT'])
def update_car(id):
    request_body = request.data.decode("utf-8")
    data = json.loads(request_body)
    result = CarModel.update(id, data)
    if not result:
        return make_response(jsonify({'error':'not found'}), 404)
    if "errors" in result:
        return make_response(jsonify({'errors': result["errors"]}), 422)
    return make_response(jsonify(result), 200)


@app.route("/cars/<int:id>", methods=['DELETE'])
def remove_car(id):
    result = CarModel.delete(id)
    if not result:
        return make_response(jsonify({'error': 'not found'}), 404)
    return make_response('', 204)


if __name__ == '__main__':
    app.run(debug=True)
