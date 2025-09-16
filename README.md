# 🚖 Uber & Lyft Fare Prediction

## 📌 Project Overview
This project predicts ride fares for Uber and Lyft services using regression models.  
It demonstrates **EDA, feature engineering, regression modeling, and model evaluation** on real-world ride data.  

Additionally, the model has been deployed using **Flask** and hosted on **Render**, allowing users to input ride details through a web interface and get real-time fare predictions.

🌐 **Live Demo:** [Uber & Lyft Fare Predictor on Render](https://farerideprediction.onrender.com/)   

---

## 📊 Dataset
- Source: Kaggle – Uber/Lyft Ride Fare dataset  
- Features include:
  - `distance`: Trip distance (miles)  
  - `surge_multiplier`: Surge pricing factor  
  - `cab_type`: Uber/Lyft  
  - `name`: Service type (UberX, UberXL, Lyft XL, etc.)  
  - `price`: Target variable  

---

## 🧹 Data Preprocessing
- Missing value handling  
- Encoding categorical variables:
  - `cab_type` → Label Encoding  
  - `name` → One-Hot Encoding  
  - `surge_multiplier` → Ordinal Encoding  
- Standardization of numeric features  

---

## 📈 Models Implemented
- **Linear Regression**  
- **Ridge Regression**  
- **Lasso Regression**  
- **Random Forest Regressor**  
- **XGBoost Regressor**  

**Evaluation Metrics:** R², MSE, RMSE, MAE  

### ✅ Sample Results

| Model              | R²    | RMSE  | MAE  |
|-------------------|-------|-------|------|
| Linear Regression  | 0.928 | 2.51  | 1.78 |
| Ridge Regression   | 0.928 | 2.51  | 1.78 |
| Lasso Regression   | 0.913 | 2.76  | 1.90 |
| Random Forest      | 0.966 | 1.73  | 1.13 |
| XGBoost            | 0.965 | 1.75  | 1.16 |

---

## 🌐 Deployment
- Built a **Flask backend** for model inference  
- Designed a simple **HTML + CSS frontend** for user input  
- Deployed on **Render Cloud** for public access  

---

## ⚡ Tech Stack
- **Python**: Pandas, NumPy, Scikit-learn, XGBoost  
- **Visualization**: Matplotlib, Seaborn  
- **Backend**: Flask  
- **Deployment**: Render (cloud hosting)  
- **Frontend**: HTML, CSS  

---

## 🚀 How to Run Locally
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/uber-lyft-fare-prediction.git
   cd uber-lyft-fare-prediction
