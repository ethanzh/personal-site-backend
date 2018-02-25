from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn import datasets

app = Flask(__name__)
CORS(app)

# Load Dataset from scikit-learn.
dataset = datasets.load_iris()


@app.route('/',  methods=['GET', 'POST'])
def hello_world():
    return 'Hello World!'


@app.route('/test',  methods=['GET', 'POST'])
def hello():

    if request.method == 'POST':
        return jsonify(request.get_json(force=True))
    elif request.method == 'GET':
        return "this is a get"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
