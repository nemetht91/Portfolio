from flask import Flask, render_template, redirect, url_for, request, flash, abort
from os import environ

app = Flask(__name__)
app.secret_key = environ.get("SECRET_KEY")
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/')
def get_home():
    return render_template("index.html")


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/portfolio')
def get_portfolio():
    return render_template("projects.html")


@app.route('/contact')
def get_contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)