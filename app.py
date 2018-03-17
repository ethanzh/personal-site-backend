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
        data = request.get_json()
        print(data)
        return 'OK'

    elif request.method == 'GET':
        return "this is a get"


@app.route('/email', methods=['GET', 'POST'])
def email():

    return 'OK'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
