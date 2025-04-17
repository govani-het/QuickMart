from flask import Flask, render_template, request, redirect, url_for,session

from base.com.vo.user_address_vo import UserAddressVO

from base.com.dao.user_address_dao import UserAddressDAO
from base.com.dao.user_order_dao import OrderDAO
from base.com.dao.area_dao import AreaDAO
from base.com.dao.city_dao import CityDAO

from base import app
from base.com.controller.login_controller import login_required

@app.route('/user/profile')
@login_required('user')
def user_profile():
    return render_template('user/userDashboard.html')

@app.route('/user/order')
@login_required('user')
def user_order():
    order_dao = OrderDAO()

    user_id = session.get('user_id')
    order_data = order_dao.view_order(user_id)
    print(order_data)
    return render_template('user/order.html',order_data=order_data)

@app.route('/user/change_password')
@login_required('user')
def user_change_password():

    return render_template('user/changePassword.html')

