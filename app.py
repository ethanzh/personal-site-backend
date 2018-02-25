from flask import Flask, jsonify
from flask.ext.cors import CORS, cross_origin
from sklearn import datasets, metrics
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Load Dataset from scikit-learn.
dataset = datasets.load_iris()


@app.route('/')
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def hello_world():
    return 'Hello World!'


@app.route('/test')
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def hello():
    model = DecisionTreeClassifier()
    model.fit(dataset.data, dataset.target)
    # make predictions
    expected = dataset.target
    predicted = model.predict(dataset.data)
    # summarize the fit of the model

    return jsonify(predicted.tolist())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
