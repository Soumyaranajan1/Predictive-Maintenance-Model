<img width="275" height="183" alt="image" src="https://github.com/user-attachments/assets/e11a8d25-fc79-4101-bc5e-d1fdba46bb9e" />

# 🛠️ Predictive Maintenance Web App for Manufacturing Machines

A machine learning–powered web application to predict potential failures in manufacturing machines based on real-time sensor data. This project aims to reduce unplanned downtime and optimize maintenance schedules using predictive analytics.

---

## 🔍 Project Overview

Unplanned machine failures in manufacturing can result in massive production losses. This project addresses this issue by implementing a **Random Forest Classifier** trained on historical machine data to forecast equipment failures.

A **Flask web application** allows users to input machine parameters and get instant predictions on whether the machine is likely to fail.

---

## ⚙️ Features

- 🧠 Machine learning model for binary failure prediction (0 = No Failure, 1 = Failure)
- 🖥️ Web interface built with Flask and HTML/CSS
- 📦 MySQL database for storing input data and prediction results
- 📈 Dashboard-ready structure for future analytics integration

---

## 📊 Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **ML Model**: Random Forest (via scikit-learn)
- **Database**: MySQL
- **Deployment**: Localhost (can be deployed on Render, Heroku, or AWS)

---

## 🧪 How It Works

1. **User Input**: Machine parameters such as temperature, torque, tool wear, rotational speed, etc.
2. **Prediction**: Model returns a 0 or 1 prediction.
3. **Storage**: Input and result are saved in MySQL for analysis and logs.

---

## 🚀 Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/predictive-maintenance-app.git
   cd predictive-maintenance-app
