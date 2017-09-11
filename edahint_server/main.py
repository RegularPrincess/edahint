import model
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


@app.route('/get_short_hint', methods=['POST'])
def get_short_hint():
    # TODO: переделать (метод заглушка)
    json_dict = request.get_json()
    return jsonify(json_dict)


@app.route('/get_hint', methods=['POST'])
def get_hint():
    # TODO: спарсить полученный жсоооон
    prods = model.compute_hint([], 'low')
    # TODO: превратить в жсооон и вернуть
    return jsonify()


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')


