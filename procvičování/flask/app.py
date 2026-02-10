from flask import Flask, render_template, redirect, url_for, request
import json

app = Flask(__name__)

messages = {}
json_file = "data/data.json"


def save_data():
    with open(json_file, "w", encoding="UTF-8") as f:
        json.dump(messages, f, indent=4)

def load_data():
    with open(json_file, "r", encoding="UTF-8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/manual")
def manual():
    return render_template("manual.html")

@app.route("/contact")
def contact():
    email = request.args.get("email")
    message = request.args.get("message")
    if email and message:
        messages[email] = message
        # { email: message }
        print(messages)
        save_data()
    return render_template("contact.html")



if __name__ == "__main__":
    messages = load_data()
    app.run(debug=True)