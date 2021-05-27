# test here: https://www.dcode.fr/base-n-convert

from flask import Flask, request
from roman2decimal import r2d
from base_convert import bc
from flask_cors import CORS
from flask import send_from_directory

app = Flask(__name__)
CORS(app)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        app.root_path,
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/<roman>", methods=["GET"])
def hello_world(roman):
    if request.method == "GET":
        decimal = r2d(roman)

        rebased_dict = {
            "decimal": str(decimal),
            "binary": bc(2, decimal),
            "ternary": bc(3, decimal),
            "vigesimal": bc(20, decimal),
            "sexagesimal": bc(60, decimal),
        }
        return rebased_dict
