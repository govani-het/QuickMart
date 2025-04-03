import os
from base import app

from flask import Flask, render_template, request, redirect, url_for,session,jsonify

from base.com.vo.user_register_vo import UserRegisterVO

from base.com.dao.user_address_dao import UserAddressDAO
from base.com.vo.user_address_vo import UserAddressVO

from base.com.vo.area_vo import AreaVO
from base.com.dao.user_address_dao import UserAddressDAO

from base.com.dao.cart_dao import CartDAO
from base.com.vo.cart_vo import CartVO

@app.route('/user/checkout_order')
def checkout_order():
    userDAO = UserAddressDAO()
    user_id = session['user_id']
    cart_dao = CartDAO()
    final_price = 0

    userinfo = userDAO.getUserinfo(user_id)
    city = userDAO.getCity()

    user_id = session.get('user_id')
    user_cart_data = cart_dao.get_cart_data(user_id)
    for i in user_cart_data:
        final_price = final_price + i[1].total_price
    return render_template('/user/checkout.html',userinfo=userinfo,city=city,user_cart_data=user_cart_data,final_price=final_price)

@app.route('/user/ajax_city')
def ajax_city():
    areaDAO = UserAddressDAO()
    areaVO = AreaVO()

    areaVO.area_city_id = request.args.get('city_id')
    area_list = areaDAO.getArea(areaVO)

    ajax_area = [i.as_dict() for i in area_list]

    return jsonify(ajax_area)

