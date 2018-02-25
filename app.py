from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sklearn import datasets, metrics
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
CORS(app)

# Load Dataset from scikit-learn.
dataset = datasets.load_iris()


@app.route('/',  methods=['GET', 'POST'])
def hello_world():
    return 'Hello World!'


@app.route('/test',  methods=['GET', 'POST'])
def hello():
    return str(request.args)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
