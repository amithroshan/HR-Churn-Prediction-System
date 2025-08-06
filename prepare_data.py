# prepare_data.py

import pandas as pd
from sklearn.model_selection import train_test_split

# Step 1: Load dataset
df = pd.read_csv("HR_comma_sep.csv")

# Step 2: Explore
print("First 5 rows:\n", df.head())
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())

# Step 3: Drop unused or problematic columns
df.drop(columns=['EmpID', 'AgeGroup', 'Over18'], inplace=True)

# Step 4: Drop rows with missing values (e.g. YearsWithCurrManager)
df.dropna(inplace=True)

# Step 5: Encode categorical columns
categorical_cols = [
    'Attrition', 'BusinessTravel', 'Department', 'EducationField',
    'Gender', 'JobRole', 'MaritalStatus', 'OverTime', 'SalarySlab'
]
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Step 6: Define features (X) and target (y)
if 'Attrition_Yes' in df_encoded.columns:
    y = df_encoded['Attrition_Yes']
else:
    y = df_encoded['Attrition']
X = df_encoded.drop(['Attrition_Yes'], axis=1, errors='ignore')

# Step 7: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 8: Save to CSV
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("\n✅ Data preparation complete!")
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
