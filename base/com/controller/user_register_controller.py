from flask import Flask, render_template, request, redirect, url_for
from base.com.dao.user_register_dao import UserRegisterDAO
from base.com.vo.user_register_vo import UserRegisterVO

import os
from base import app

@app.route('/user/register')
def register_page():
    return render_template('user/register.html')
@app.route('/user/addUserdata', methods=['POST'])
def addUserdata():
    user_vo = UserRegisterVO()
    user_dao = UserRegisterDAO()

    user_vo.username = request.form.get('username')
    user_vo.password = request.form.get('password')
    user_vo.email = request.form.get('email')
    user_vo.phone = request.form.get('phone')

    user_dao.insertUserData(user_vo)
    return render_template('user/login.html')