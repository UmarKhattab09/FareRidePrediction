from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load trained model
with open("models/xgboost.pkl", "rb") as f:
    model = joblib.load(f)

# Columns in the exact order as your X_train
feature_columns = [
    'distance', 'surge_multiplier', 'cab_type_encoded',
    'name_Black', 'name_Black SUV', 'name_Lux', 'name_Lux Black',
    'name_Lux Black XL', 'name_Lyft', 'name_Lyft XL', 'name_Shared',
    'name_Taxi', 'name_UberPool', 'name_UberX', 'name_UberXL', 'name_WAV'
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # --- Step 1: Get inputs from form ---
    distance = float(request.form["distance"])
    surge_multiplier = float(request.form["surge_multiplier"])
    cab_type_encoded = int(request.form["cab_type_encoded"])   # 0 = Uber, 1 = Lyft
    # surge_encoded = float(request.form["surge_encoded"])         # 0 = No, 1 = Yes
    ride_type = request.form["ride_name"]                      # one of the name_* columns

    # --- Step 2: Build one-hot for ride types ---
    ride_features = {col: 0 for col in feature_columns if col.startswith("name_")}
    if ride_type in ride_features:
        ride_features[ride_type] = 1

    # --- Step 3: Build feature row in same order ---
    input_data = {
        'distance': distance,
        'surge_multiplier': surge_multiplier,
        'cab_type_encoded': cab_type_encoded,
        **ride_features
    }
    input_df = pd.DataFrame([input_data], columns=feature_columns)
    print(input_df)
    # --- Step 4: Predict ---
    prediction = model.predict(input_df)[0]

    return render_template("result.html", prediction=f"{prediction:.2f}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=True)
