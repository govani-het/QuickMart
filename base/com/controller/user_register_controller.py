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

