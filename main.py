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
            category="inverse",
            symbol="BTCUSD",
        )
        list = r["result"]["list"]
        list[0]['avgPrice'] = "1"
        print(f"Тикет: {list[0]['symbol']}\nНаправление: {list[0]['side']}\nЦена входа: {list[0]['avgPrice']}")
        return render_template('positions.html', positions=list)
    except Exception as ex:
        print(ex)
        return f"<h1>{ex}</h1>"





# API Key: 0zFHX75FgVna96I92H
# API Secret:  mjoStlNqdaA5KWvhWKtw8fhBnYRTmaYMRnmV

# api_key = "IXNWmFaxuAcD4xwTke",
# api_secret = "XIfBM67BlE6nZsSuqTpYcr7gTLVd9wVresnx"