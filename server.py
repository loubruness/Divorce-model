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

model = load_model()

@app.route("/predict", methods=['POST'])
def predict():
    X = request.get_json()['X']
    y_pred = model.predict(X)
    return json.dumps({'prediction':y_pred.tolist()})