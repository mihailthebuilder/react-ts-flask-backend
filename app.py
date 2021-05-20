from flask import Flask, request
from roman2decimal import r2d

app = Flask(__name__)


@app.route("/<roman>", methods=["GET"])
def hello_world(roman):
    if request.method == "GET":
        decimal = r2d(roman)

        return f"{r2d(roman)}"
