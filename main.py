import os

from pybit.unified_trading import HTTP
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

cl = HTTP(
    api_key = os.getenv("API_KEY"),
    api_secret = os.getenv("API_SECRET")
)

@app.route("/")
def hello_world():
    try:
        r = cl.get_positions(
            category="inverse"
        )
        list = r["result"]["list"]
        return render_template('positions.html', positions=list)
    except Exception as ex:
        print(ex)
        return f"<h1>{ex}</h1>"
    