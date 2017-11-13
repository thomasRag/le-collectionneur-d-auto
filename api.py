from flask import Flask, jsonify, make_response

app = Flask(__name__);

app.CARS = ['car1', 'car2']


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
        return result;

    def save(self, car):
        pass

    def remove(self, id):
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


@app.route("/cars/<int:id>", methods=['POST'])
def create_car():
    pass


@app.route("/cars/<int:id>", methods=['PUT'])
def update_car():
    pass


@app.route("/cars", methods=['DELETE'])
def remove_car():
    pass

if __name__ == '__main__':
    app.run(debug=True)
