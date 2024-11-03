from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        input_text = request.form.get("input_text")
        random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
        return render_template("result.html", input_text=input_text, random_number=random_number)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

