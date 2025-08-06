#  HR Churn Prediction System

This project is a web-based **HR Churn Prediction System** that allows users to input employee details and receive the probability of that employee leaving the organization. It uses a machine learning model (e.g., Logistic Regression, Decision Tree, or XGBoost) and presents predictions in an interactive and visually appealing dashboard.

## 🚀 Features

- 🧠 Machine Learning model to predict employee churn
- 📋 Easy-to-use web form for inputting employee details
- 📊 Dynamic pie chart showing churn vs retention
- ⚠️ Risk level classification (High / Medium / Low)
- 🌐 Built using Flask and Chart.js
- 🎨 Vibrant and responsive UI with modern dark theme
- 📥 Supports Employee ID and Name for easier tracking

---

## 🖥️ Tech Stack

| Technology | Use |
|------------|-----|
| Python     | Backend logic, model loading, Flask API |
| Flask      | Web framework |
| HTML/CSS   | Frontend UI |
| Chart.js   | Pie chart rendering |
| Pandas     | Data handling |
| Pickle     | Model serialization |

---

## 📁 Project Structure

 ``` hr-churn-prediction/
├── model/
│   └── model.pkl
├── templates/
│   ├── form.html
│   └── result.html
├── prepare_data.py
├── train_model.py
├── app.py
└── README.md
```
---


## 🧪 How to Run Locally
### ✅ Step 1: **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/hr-churn-prediction.git
   cd hr-churn-prediction
```
### ✅ Step 2: Install dependencies
 ```bash
pip install pandas scikit-learn flask 
 ```
### ✅ Step 3: Prepare the dataset
 ```bash
python prepare_data.py
 ```
### ✅ Step 4: Train the model
 ```bash
python train_model.py
 ```

### ✅ Step 5: Launch the Flask app
 ```bash
python app.py
 ```
### Then open your browser and go to:
 ```bash
http://127.0.0.1:5000
 ```
---

📝 Future Enhancements

- 🧾 Export prediction as PDF
- 🗃️ Add SQLite/PostgreSQL database for storing history
- 📤 Deploy to AWS
- 🔐 Add login system for HR users
