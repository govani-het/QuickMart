from flask import Flask, render_template, request, redirect, url_for
from base import app

@app.route('/user/profile')
def user_profile():
    return render_template('user/userDashboard.html')


@app.route('/user/userInfo')
def user_parsonalInfo():

    return render_template('user/userInfo.html')

@app.route('/user/order')
def user_order():

    return render_template('user/order.html')

@app.route('/user/address')
def user_address():

    return render_template('user/address.html')

@app.route('/user/changePassword')
def user_changePassword():

    return render_template('user/changePassword.html')