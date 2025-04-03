from flask import Flask, render_template, request, redirect, url_for
from base.com.dao.category_dao import CategoryDAO
from base import app

@app.route("/")
def home_page():  # put application's code here
    return render_template('user/login.html')

@app.route("/user/home")
def user_home_page():
    category_dao = CategoryDAO()
    category_vo_list = category_dao.view_category()
    return render_template('user/index.html', category_list=category_vo_list)

@app.route("/admin/home")
def admin_home_page():
    return render_template('admin/index.html')