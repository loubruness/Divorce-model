from flask import Flask, request
import joblib
import json

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/")
def hello_world():
    predictions = predict()
    return f'Prediction : {predictions}'

def load_model():
    return joblib.load('divorceclassification.joblib')

def load_model_reduced():
    return joblib.load('divorceclassificationreduced.joblib')

model = load_model()
model_reduced = load_model_reduced()

@app.route("/predict", methods=['POST'])
def predict():
    X = request.get_json()['X']
    y_pred = model.predict(X)
    return json.dumps({'prediction':y_pred.tolist()})

@app.route("/predict_reduced", methods=['POST'])
def predict_reduced():
    X = request.get_json()['X']
    y_pred = model_reduced.predict(X)
    return json.dumps({'prediction':y_pred.tolist()})