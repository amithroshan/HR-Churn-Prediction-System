# app.py

from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and feature names
with open("model/model.pkl", "rb") as f:
    model, feature_names = pickle.load(f)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form.to_dict()

        input_data = {
            "Age": float(form_data.get("Age", 0)),
            "MonthlyIncome": float(form_data.get("MonthlyIncome", 0)),
            "DistanceFromHome": float(form_data.get("DistanceFromHome", 0)),
            "OverTime_Yes": float(form_data.get("OverTime_Yes", 0)),
            "YearsAtCompany": float(form_data.get("YearsAtCompany", 0)),
            "JobSatisfaction": float(form_data.get("JobSatisfaction", 0))
        }

        encoded_fields = [
            f"Department_{form_data.get('Department')}",
            f"EducationField_{form_data.get('EducationField')}",
            f"JobRole_{form_data.get('JobRole')}",
            f"MaritalStatus_{form_data.get('MaritalStatus')}"
        ]

        for field in encoded_fields:
            input_data[field] = 1

        for feature in feature_names:
            if feature not in input_data:
                input_data[feature] = 0

        input_df = pd.DataFrame([[input_data[feature] for feature in feature_names]], columns=feature_names)

        prob = model.predict_proba(input_df)[0][1]
        result = round(prob * 100, 2)

        return render_template(
            'result.html', 
            prediction=result, 
            form_data=form_data
        )

    except Exception as e:
        return render_template('form.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
