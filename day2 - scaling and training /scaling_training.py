import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

# Load your cleaned data
train_df = pd.read_csv("diabetes_cleaned_test.csv")
test_df = pd.read_csv("diabetes_cleaned_train.csv")

print("Train shape:", train_df.shape)
print("Test shape:", test_df.shape)

# Features and labels
X_train = train_df.drop("Outcome", axis=1)
y_train = train_df["Outcome"]

X_test = test_df.drop("Outcome", axis=1)
y_test = test_df["Outcome"]


# scaling -
scaler = StandardScaler()

# Fit the scaler on the training data and transform it
X_train_scaled = scaler.fit_transform(X_train)

# Only transform the test data (don't fit again)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(solver='liblinear', max_iter=500,class_weight='balanced',random_state=42)
model.fit(X_train_scaled, y_train)

# Predict labels and probabilities
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_proba))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# Visualize performance

fpr, tpr, _ = roc_curve(y_test, y_proba)
plt.plot(fpr, tpr, label=f"AUC = {roc_auc_score(y_test, y_proba):.3f}")
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Diabetes Prediction")
plt.legend()
plt.show()

# Save the model for later use
import joblib
joblib.dump(model, "logistic_diabetes_model.joblib")
print("✅ Model saved as logistic_diabetes_model.joblib")



# Save both model and scaler after training
joblib.dump(model, "logistic_diabetes_model.joblib")
joblib.dump(scaler, "scaler.joblib")

print("✅ Model and scaler saved!")