from flask import Flask, render_template
import datetime
app= Flask(__name__)





@app.route("/")


def index():
    headline="hello"
    lista=["primero","segundo","tercero"]
    now=datetime.datetime.now()
    new_year=now.month==1 and now.day==1
    return render_template("index.html",lista=lista,headline=headline)
@app.route("/bye")
def bye():
    headline="GoodBye"
    return render_template("index.html",headline=headline)
@app.route("/more")
def more():
    headline="more"
    return render_template("index.html",headline=headline)
