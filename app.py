from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)


@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form["name_input"]) + ", great to meet you!")
    return render_template("index.html")
