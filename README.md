# FareRidePrediction

🚖 Project Overview

This project predicts ride fares for Uber and Lyft services using historical ride data. It demonstrates data preprocessing, feature engineering, and regression modeling (Linear Regression, Ridge, Lasso, Random Forest, XGBoost). The project also includes a Flask-based web interface for real-time fare predictions.

📊 Dataset

Source: Kaggle “Uber and Lyft Ride Fare Prediction” dataset

Features include:

distance: Trip distance in miles

surge_multiplier: Surge pricing factor

cab_type: UberX, UberXL, Lyft, etc.

name: Service type (Uber, Lyft, Black, Shared, etc.)

price: Target variable

🧹 Data Preprocessing

Handle missing values

Encode categorical features:

cab_type → Label Encoding

name → One-Hot Encoding

Encode ordinal features:

surge_multiplier → OrdinalEncoder

Standardize numeric features using StandardScaler

🛠 Features

Distance, surge multiplier, cab type, and service type

Optional feature engineering: time of day, weekday/weekend

📈 Models

Linear Regression

Ridge Regression

Lasso Regression

Random Forest Regressor

XGBoost Regressor

Evaluation Metrics: R², MSE, RMSE, MAE

Sample Results:

Model	R²	RMSE	MAE
Linear Regression	0.928	2.51	1.78
Ridge Regression	0.928	2.51	1.78
Lasso Regression	0.913	2.76	1.90
Random Forest	0.966	1.73	1.13
XGBoost	0.965	1.75	1.16
