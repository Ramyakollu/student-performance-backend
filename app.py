from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os
import numpy as np

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "Student Performance Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    study_hours = data.get("study_hours")
    attendance = data.get("attendance")
    previous_score = data.get("previous_score")

    input_data = np.array([[study_hours, attendance, previous_score]])
    prediction = model.predict(input_data)[0]

    return jsonify({
        "prediction": float(prediction)
    })

if __name__ == "__main__":
    app.run(debug=True)
