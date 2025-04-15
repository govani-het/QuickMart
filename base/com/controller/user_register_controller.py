from flask import Flask, render_template, request, redirect, url_for,session


from base.com.dao.user_register_dao import UserRegisterDAO
from base.com.dao.category_dao import CategoryDAO

from base.com.vo.user_register_vo import UserRegisterVO

import os
import bcrypt
from base import app

app.secret_key = 'qazwsxedcrfvtgbyhnujmiklop123456'
@app.route('/user/register')
def register_page():
    return render_template('user/register.html')
@app.route('/user/addUserdata', methods=['POST'])
def addUserdata():
    user_vo = UserRegisterVO()
    user_dao = UserRegisterDAO()

    user_vo.username = request.form.get('username')
    password = request.form.get('password')
    user_vo.email = request.form.get('email')
    user_vo.phone = request.form.get('phone')

    salt = bcrypt.gensalt(rounds=12)
    hashed_login_password = bcrypt.hashpw(password.encode("utf-8"),
                                          salt)

    user_vo.password = hashed_login_password
    user_dao.insertUserData(user_vo)
    return render_template('user/login.html')

@app.route('/user/login', methods=['POST'])
def login_page():
    email = request.form.get('email')
    password = request.form.get('password')

    user_dao = UserRegisterDAO()
    user = user_dao.getUserData(email, password)

    if email == 'admin@gmail' and password == '1234':

        return render_template('admin/index.html')
    elif user:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        session['user_id'] = user.id
        session['username'] = user.username
        session['user_email'] = user.email
        session['user_phone'] = user.phone
        return render_template('user/index.html',category_list=category_vo_list)
    else:

        return render_template('user/login.html', error="Invalid email or password")