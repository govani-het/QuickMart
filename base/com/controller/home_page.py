from flask import Flask, render_template, request, redirect, url_for
from base.com.dao.category_dao import CategoryDAO
from base import app

@app.route("/")
def home_page():  # put application's code here
    # category_dao = CategoryDAO()
    # category_vo_list = category_dao.view_category()
    return render_template('user/login.html')