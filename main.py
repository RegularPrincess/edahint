from flask import Flask
from flask import jsonify
from flask import request
import model


app = Flask(__name__)


@app.route('/get_hint', methods=['POST'])
def get_hint():
    json_dict = request.get_json()
    return jsonify(json_dict)


@app.route('/')
def hello_world():
    model.compute_hint(['e'], 'low')
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')


