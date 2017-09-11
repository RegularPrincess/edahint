import model
import json
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
    json_dict = request.get_json()
    prods = model.compute_hint(json_dict['products'], json_dict['price_level'])
    print(prods)
    return json.dumps([inst.__dict__ for inst in prods])


@app.route('/')
def hello_world():
    return 'I work!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')


