from flask import Flask, render_template, request
import joblib
import numpy as np
import os
import traceback

app = Flask(__name__)

# Load saved model and scaler (robust to where the app is started from)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "logistic_diabetes_model.joblib")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.joblib")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values from the form in the exact order used during training
        field_order = [
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age",
        ]

        features = []
        for field_name in field_order:
            raw_value = request.form.get(field_name, None)
            if raw_value is None or raw_value == "":
                raise ValueError(f"Missing required field: {field_name}")
            features.append(float(raw_value))

        print("Input features:", features)

        # Scale the input using the same scaler used during training
        scaled_features = scaler.transform([features])
        print("Scaled features:", scaled_features)

        # Make prediction
        prediction = model.predict(scaled_features)[0]
        print("Prediction:", prediction)

        # Prepare result message 
        if prediction == 1:
            result_text = "✅ You do not have diabetes. Stay healthy!"
        else:
            result_text = "⚠️ You have diabetes — it’s advisable to visit your doctor."

        return render_template('index.html', result=result_text)
    
    except Exception as e:
        # Print any error in the terminal
        print("❌ Error occurred:", e)
        traceback.print_exc()
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)