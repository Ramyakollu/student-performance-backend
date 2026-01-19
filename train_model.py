import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Dummy dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "attendance": [50, 55, 60, 65, 70, 75, 80, 85],
    "previous_score": [40, 45, 50, 55, 60, 65, 70, 75],
    "final_score": [45, 50, 55, 60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance", "previous_score"]]
y = df["final_score"]

model = LinearRegression()
model.fit(X, y)

# Save model in SAME folder
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully")
