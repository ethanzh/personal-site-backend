from flask import Flask

from sklearn import svm
from sklearn import datasets

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test/')
def test():

    clf = svm.SVC()
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    clf.fit(X, y)
    return clf.predict(4)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
