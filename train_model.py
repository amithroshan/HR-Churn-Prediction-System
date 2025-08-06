# train_model.py

import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load processed data
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("y_train.csv").values.ravel()  # flatten to 1D
y_test = pd.read_csv("y_test.csv").values.ravel()

# Step 2: Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 3: Predict on test set
y_pred = model.predict(X_test)

# Step 4: Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ Accuracy: {accuracy:.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Step 5: Save model and feature names
with open("model/model.pkl", "wb") as f:
    pickle.dump((model, list(X_train.columns)), f)

print("\n✅ Model training complete. Model saved to 'model/model.pkl'.")
