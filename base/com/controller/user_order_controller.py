import os
from base import app

from flask import Flask, render_template, request, redirect, url_for,session,jsonify

from base.com.vo.user_register_vo import UserRegisterVO

from base.com.dao.user_address_dao import UserAddressDAO
from base.com.vo.user_address_vo import UserAddressVO

from base.com.vo.user_order_vo import OrderVO
# from base.com.dao.user_order_dao import

from base.com.vo.area_vo import AreaVO
from base.com.dao.area_dao import AreaDAO
from base.com.dao.city_dao import CityDAO

from base.com.dao.cart_dao import CartDAO
from base.com.vo.cart_vo import CartVO

@app.route('/user/checkout_order')
def checkout_order():
    user_dao = UserAddressDAO()
    area_dao = AreaDAO()
    city_dao = CityDAO()

    user_id = session.get('user_id')
    cart_dao = CartDAO()
    final_price = 0

    userAddressInfo = user_dao.view_address(user_id)
    userinfo = user_dao.getUserinfo(user_id)
    city = city_dao.view_city()
    area = area_dao.view_area()


    user_cart_data = cart_dao.get_cart_data(user_id)
    for i in user_cart_data:
        final_price = final_price + i[1].total_price
    return render_template('/user/checkout.html',userinfo=userinfo,city=city,area=area,user_cart_data=user_cart_data,final_price=final_price,userAddressInfo=userAddressInfo)

@app.route('/user/ajax_city')
def ajax_city():
    area_dao = UserAddressDAO()
    area_vo = AreaVO()

    area_vo.area_city_id = request.args.get('city_id')
    area_list = area_dao.getArea(area_vo)

    ajax_area = [i.as_dict() for i in area_list]

    return jsonify(ajax_area)

@app.route('/user/place_order',methods=['POST'])
def place_order():

    userAddressDAO = UserAddressDAO()
    userAddressVO = UserAddressVO()

    order_vo = OrderVO


    user_id = session.get('user_id')

    cart_dao = CartDAO()
    cart_vo = CartVO()

    address_id = request.form.get('address_id')

    userAddressVO.user_id = user_id
    userAddressVO.address_id = address_id
    userAddressVO.username = request.form.get('username')
    userAddressVO.email = request.form.get('email')
    userAddressVO.phone = request.form.get('phone')
    userAddressVO.address = request.form.get('address')
    userAddressVO.city = request.form.get('city')
    userAddressVO.area = request.form.get('area')
    userAddressVO.pincode = request.form.get('pincode')

    if address_id:
        userAddressDAO.update_address(userAddressVO)
    else:
        userAddressDAO.add_address(userAddressVO)

    user_cart_data = cart_dao.get_cart_data(user_id)

    for i in user_cart_data:
        pass

    return redirect('/user/view_cart')


