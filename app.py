from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    distance = float(request.form["distance"])
    surge = float(request.form["surge"])
    cab_type = request.form["cab_type"]

    # Example fake model logic
    price = distance * 2 + surge * 3
    return f"Predicted Fare: ${price:.2f}"

if __name__ == "__main__":
    app.run(debug=True)
