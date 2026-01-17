from flask import Flask, request, jsonify
import pickle
import os
import numpy as np

app = Flask(__name__)

# ================================
# LOAD MODEL SAFELY (RENDER FIX)
# ================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ================================
# HOME ROUTE (TEST)
# ================================
@app.route("/")
def home():
    return "Student Performance Prediction API is running!"

# ================================
# PREDICTION ROUTE
# ================================
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Example input fields (adjust if your model uses different ones)
    hours_studied = data.get("hours_studied")
    previous_score = data.get("previous_score")

    # Convert input to model format
    input_data = np.array([[hours_studied, previous_score]])

    prediction = model.predict(input_data)

    return jsonify({
        "prediction": prediction[0]
    })

# ================================
# RUN APP
# ================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
