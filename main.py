from flask import Flask
from flask import jsonify
from flask import request
import model


app = Flask(__name__)


@app.route('/get_hint', methods=['POST'])
def get_hint():
    json_dict = request.get_json()
    return jsonify(json_dict)


if __name__ == '__main__':
    # hint = model.compute_hint([' грудк', ' хле', ' яблок', ' сыр ', 'сырок '], 'low')
    # print(hint)
    app.run()


