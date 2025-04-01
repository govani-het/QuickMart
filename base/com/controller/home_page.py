from flask import Flask, render_template, request, redirect, url_for

from base import app

@app.route("/")
def home_page():  # put application's code here
    return render_template('user/login.html')