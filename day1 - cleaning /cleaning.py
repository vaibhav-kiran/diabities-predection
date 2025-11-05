# pima_cleaning.py
import numpy as np
import pandas as pd

# 1) Load data
df = pd.read_csv("pima_train.csv")  # change path if needed
print("✅ Data loaded successfully!")
print("Shape:", df.shape)
print("\nFirst 5 rows:\n", df.tail())

# 2) Quick summary
print("\nOutcome ̀distribution:\n", df['Outcome'].value_counts(normalize=True))
print("\nColumn summary:\n", df.describe())

# 3) Check for zeros in features that cannot be zero in practice
zero_features = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for col in zero_features:
    n_zero = (df[col] == 0).sum()
    print(f"{col}: zeros = {n_zero}")

# 4) Replace zeros with NaN (since zeros here mean missing values)
df[zero_features] = df[zero_features].replace(0, np.nan)

# 5) Show how many missing values each column has now
print("\nMissing value counts after replacement:\n", df.isna().sum())

# # 6) Handle missing values using median imputation
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
df[zero_features] = imputer.fit_transform(df[zero_features])

print("\n✅ Missing values handled (imputed with median).")
print("\nAfter cleaning summary:\n", df.describe())

# 7) Save cleaned data (optional)
df.to_csv("diabetes_cleaned_train.csv", index=False)
print("\n💾 Cleaned dataset saved as 'diabetes_cleaned_train.csv'")