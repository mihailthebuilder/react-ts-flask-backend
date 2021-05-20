# test here: https://www.dcode.fr/base-n-convert

from flask import Flask, request
from roman2decimal import r2d
from base_convert import bc

app = Flask(__name__)


@app.route("/<roman>", methods=["GET"])
def hello_world(roman):
    if request.method == "GET":
        decimal = r2d(roman)

        rebased_dict = {
            "decimal": decimal,
            "binary": bc(2, decimal),
            "ternary": bc(3, decimal),
            "vigesimal": bc(20, decimal),
            "sexagesimal": bc(60, decimal),
        }
        return rebased_dict
