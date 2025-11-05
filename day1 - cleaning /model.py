import joblib
import numpy as np


# Later (or in another file), load them back
model = joblib.load("logistic_diabetes_model.joblib")
scaler = joblib.load("scaler.joblib")


# Example new data (must have 8 features like training data)
new_data = np.array([[6, 148, 72, 35, 0, 33.6, 0.627, 50]])  # one patient data
new_data_scaled = scaler.transform(new_data)

# Predict
prediction = model.predict(new_data_scaled)
probability = model.predict_proba(new_data_scaled)[0, 1]

print("Prediction (0 = No diabetes, 1 = Diabetes):", prediction[0])
print("Probability of having diabetes:", round(probability, 3))