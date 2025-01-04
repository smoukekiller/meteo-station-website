from flask import Flask, render_template
from get_data import get_data
app = Flask(__name__)

@app.route("/")
def home():
    temperature, humidity = get_data()
    return render_template("index.html", temperature=temperature, humidity=humidity)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)