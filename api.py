from flask import Flask, jsonify, make_response

app = Flask(__name__);

CARS = []

class CarModel:
    @staticmethod
    def list(self):
        mycars = CARS
        return mycars


@app.route("/cars", methods=['GET'])
def get_cars():
    cars = CarModel.list()
    return make_response(jsonify(cars), 200)


@app.route("/cars/<int:id>", methods=['GET'])
def get_car(id):
    pass


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
