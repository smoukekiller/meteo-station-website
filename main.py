from flask import Flask, render_template, jsonify
from flask_talisman import Talisman
import config
from get_data import get_data
from compile_data import compile_data



app = Flask(__name__)

csp = {
    'default-src': [
        "'self'"
    ],
    'script-src': [
        "'self'",
        'https://cdn.jsdelivr.net'
    ],
    'style-src': [
        "'self'",
        'https://cdn.jsdelivr.net'
    ],
}
Talisman(app, content_security_policy=csp)
@app.route("/")
def home():
    temperature, humidity, last_updated = get_data()
    
    return render_template("index.html", temperature=temperature, humidity=humidity, last_updated=last_updated)

@app.route('/data')
def fetch_data():
    labels, temp, humid = compile_data()
    data = {"temperature": temp,
            "labels": labels,
            "humidity": humid
            }
    return jsonify(data)

if __name__ == "__main__":
   app.run(
    host='0.0.0.0',
     port=config.PORT,
    ssl_context=(config.PATH_TO_FULLCHAIN_PEM, config.PATH_TO_PRIVKEY_PEM)
)