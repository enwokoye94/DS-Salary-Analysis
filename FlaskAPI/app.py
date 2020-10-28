import flask
from flask import Flask, jsonify, request
import json
import pickle
from test_data import test_data
import numpy as np


# load fucntion for our saved model
def load_models():
    file_name = 'models/lasso_model.p'
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model


app = Flask(__name__)


# sets the page predict to get information from server
@app.route('/predict', methods=['GET'])
def predict():
    x = test_data.iloc[5, :].values.reshape(1, -1)
    model = load_models()
    prediction = model.predict(x)[0]

    response = json.dumps({'response': prediction})
    return response, 200


if __name__ == '__main__':
    application.run(debug=True)
