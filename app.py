from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier
import numpy as np

app = Flask(__name__)

# Sample trained model (you can replace this with a real trained model)
# Example input features: Age, Blood Pressure, Cholesterol, Smoking, etc.
X_train = np.array([[50, 140, 200, 1], [60, 160, 230, 0], [30, 120, 180, 1], [45, 130, 190, 0]])
y_train = np.array([1, 1, 0, 0])  # 1 = Heart Disease, 0 = No Heart Disease

# Train a simple Random Forest model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = int(request.form["age"])
        blood_pressure = int(request.form["blood_pressure"])
        cholesterol = int(request.form["cholesterol"])
        smoking = int(request.form["smoking"])

        input_data = np.array([[age, blood_pressure, cholesterol, smoking]])
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            result = "Uh-oh, you’re at a *High Risk* of heart disease 😟"
            avoidance_message = "Avoid stressing out, smoking, and binge-eating junk food 🍔. Get active, live happy! 💪"
            message = "Get checked out soon, fam! You got this 💥."
        else:
            result = "Good news! You're at a *Low Risk* of heart disease 😎"
            avoidance_message = ""
            message = "You're crushing it! Keep doing what you're doing – healthy vibes only 🌱"
        motivational_message = "Keep exercising! We got this! Let’s keep slaying together 🏃‍♀️💨"

        return render_template("index.html", result=result, message=message, avoidance_message=avoidance_message, motivational_message=motivational_message)
    
    return render_template("index.html", result="", message="", avoidance_message="", motivational_message="")

if __name__ == "__main__":
    app.run(debug=True)
