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


@app.route('/user/userInfo')
@login_required('user')
def user_parsonalInfo():

    user_dao = UserAddressDAO()
    city_dao = CityDAO()
    user_id = session.get('user_id')

    user_address_info = user_dao.view_address(user_id)
    city = city_dao.view_city()
    return render_template('user/addAddress.html',user_address_info=user_address_info,city=city)

@app.route('/user/order')
@login_required('user')
def user_order():
    order_dao = OrderDAO()

    user_id = session.get('user_id')
    order_data = order_dao.view_order(user_id)
    print(order_data)
    return render_template('user/order.html',order_data=order_data)

@app.route('/user/address')
@login_required('user')
def user_address():
    user_dao = UserAddressDAO()

    user_id = session.get('user_id')

    user_address_info = user_dao.view_address(user_id)
    return render_template('user/address.html',user_address_info=user_address_info)

@app.route('/user/changePassword')
@login_required('user')
def user_changePassword():

    return render_template('user/changePassword.html')

@app.route('/user/add_address',methods=['POST'])
@login_required('user')
def user_add_address():
    user_dao = UserAddressDAO()
    user_address_vo = UserAddressVO()
    user_id = session.get('user_id')

    address_id = request.form.get('address_id')
    user_address_vo.address_id = address_id
    user_address_vo.user_id = user_id
    user_address_vo.username = request.form.get('username')
    user_address_vo.email = request.form.get('email')
    user_address_vo.phone = request.form.get('phone')
    user_address_vo.address = request.form.get('address')
    user_address_vo.city = request.form.get('city')
    user_address_vo.area = request.form.get('area')
    user_address_vo.pincode = request.form.get('pincode')

    if address_id:
        user_dao.update_address(user_address_vo)
    else:
        user_dao.add_address(user_address_vo)

    user_address_info = user_dao.view_address(user_id)
    return render_template('user/address.html',user_address_info=user_address_info)