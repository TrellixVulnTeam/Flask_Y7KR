from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/ASDA")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
    )


@app.route("/ASDA2")
def index2():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                Celsius2 temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
    )


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)