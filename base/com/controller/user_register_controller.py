from flask import render_template, request,flash,redirect

from base.com.dao.user_register_dao import UserRegisterDAO

from base.com.vo.user_register_vo import UserRegisterVO

import bcrypt
from base import app

app.secret_key = 'qazwsxedcrfvtgbyhnujmiklop123456'
@app.route('/user/register')
def register_page():
    try:
        return render_template('user/register.html')
    except:
        return render_template('user/viewError.html')
@app.route('/user/register_user_info', methods=['POST'])
def add_user_data():
    try:
        user_vo = UserRegisterVO()
        user_dao = UserRegisterDAO()

        user_vo.username = request.form.get('username')
        password = request.form.get('password')
        user_vo.email = request.form.get('email')
        user_vo.phone = request.form.get('phone')

        salt = bcrypt.gensalt(rounds=12)
        hashed_login_password = bcrypt.hashpw(password.encode("utf-8"),
                                              salt)
        user_data = user_dao.user_info()
        user_vo.password = hashed_login_password
        for data in user_data:
            if data.email == user_vo.email:
                flash('Email already registered', 'error')
                return redirect('/user/register')
            elif data.phone == user_vo.phone:
                flash('Phone number already registered', 'error')
                return redirect('/user/register')

        user_dao.insert_user_data(user_vo)
        return render_template('user/login.html')

    except:
        return render_template('user/viewError.html')