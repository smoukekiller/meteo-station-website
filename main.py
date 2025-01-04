from flask import Flask, render_template
from flask_talisman import Talisman
import config
from get_data import get_data

app = Flask(__name__)
Talisman(app)
@app.route("/")
def home():
    temperature, humidity = get_data()
    return render_template("index.html", temperature=temperature, humidity=humidity)

if __name__ == "__main__":
   app.run(
    host='0.0.0.0',
    port=config.PORT,
    ssl_context=(config.ROUTE_TO_FULLCHAIN_PEM, config.ROUTE_TO_PRIVKEY_PEM)
)