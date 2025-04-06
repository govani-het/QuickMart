from flask import Flask, render_template, request, redirect, url_for,session

from base.com.dao.user_address_dao import UserAddressDAO
from base.com.dao.user_order_dao import OrderDAO
from base.com.dao.area_dao import AreaDAO
from base.com.dao.city_dao import CityDAO

from base import app

@app.route('/user/profile')
def user_profile():
    user_dao = UserAddressDAO()

    user_id = session.get('user_id')

    user_data = user_dao.getUserinfo(user_id)
    return render_template('user/userDashboard.html',user_data=user_data)


@app.route('/user/userInfo')
def user_parsonalInfo():

    user_dao = UserAddressDAO()
    city_dao = CityDAO()
    area_dao = AreaDAO()

    user_id = session.get('user_id')


    city = city_dao.view_city()
    area = area_dao.view_area()
    user_address_info = user_dao.view_address(user_id)
    user_info = user_dao.getUserinfo(user_id)
    return render_template('user/userInfo.html',user_info=user_info,user_address_info=user_address_info,city=city,area=area)

@app.route('/user/order')
def user_order():
    order_dao = OrderDAO()

    user_id = session.get('user_id')
    order_data = order_dao.view_order(user_id)
    print(order_data)
    return render_template('user/order.html',order_data=order_data)

@app.route('/user/address')
def user_address():

    return render_template('user/address.html')

@app.route('/user/changePassword')
def user_changePassword():

    return render_template('user/changePassword.html')