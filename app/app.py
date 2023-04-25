from flask import Flask, render_template, redirect, url_for, request
import utils

app = Flask(__name__)

app.enable = True

@app.route("/")
def index():
    items = utils.get_items()
    return render_template("index.html", items = items) 


@app.route("/add_item", methods = ["POST"])
def add_item():
    item_name: str = request.form["item_name"]
    price: str = request.form["price"]
    utils.add_item(item_name, price)
    return redirect(url_for("index"))


@app.route("/remove_item", methods = ["POST"])
def remove_item():
    item_name: str = request.form["item_name"]
    utils.remove_item(item_name)
    return redirect(url_for("index"))


if __name__ == '__main__':
   app.run(debug = True, host = "0.0.0.0")