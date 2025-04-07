import os
from base import app
from base import db

from flask import Flask, render_template, request, redirect, url_for,session,jsonify

#here all vo
from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.user_address_vo import UserAddressVO
from base.com.vo.user_order_item_vo import OrderItemVO
from base.com.vo.user_order_vo import OrderVO
from base.com.vo.cart_vo import CartVO
from base.com.vo.area_vo import AreaVO


#here all dao

from base.com.dao.user_address_dao import UserAddressDAO
from base.com.dao.area_dao import AreaDAO
from base.com.dao.city_dao import CityDAO
from base.com.dao.cart_dao import CartDAO

@app.route('/user/checkout_order')
def checkout_order():
    user_dao = UserAddressDAO()
    area_dao = AreaDAO()
    city_dao = CityDAO()
    cart_dao = CartDAO()

    user_id = session.get('user_id')

    final_price = 0

    userAddressInfo = user_dao.view_address(user_id)

    city = city_dao.view_city()
    area = area_dao.view_area()

    user_cart_data = cart_dao.get_cart_data(user_id)
    for i in user_cart_data:
        final_price = final_price + i[1].total_price
    return render_template('/user/checkout.html',city=city,area=area,user_cart_data=user_cart_data,final_price=final_price,userAddressInfo=userAddressInfo)

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

    order_item_vo = OrderItemVO()
    order_vo = OrderVO()

    cart_dao = CartDAO()

    user_id = session.get('user_id')

# here user can add address or if user has already added address user can update it if user want
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

# here create new order

    address = UserAddressVO.query.filter_by(user_id=user_id).first()

    order_vo.address_id = address.address_id
    order_vo.user_id = user_id
    order_vo.final_price = request.form.get('final_price')
    order_vo.status = 'Pending'
    order_vo.payment_method = request.form.get('payment_type')

    db.session.add(order_vo)
    db.session.commit()

# now we move cart item to order item table


    cart_data = cart_dao.get_cart_data(user_id)

    for item in cart_data:
        order_item_vo = OrderItemVO()
        order_item_vo.order_id = order_vo.order_id
        order_item_vo.user_id = user_id
        order_item_vo.product_id = item[1].product_id
        order_item_vo.quantity = item[1].quantity
        order_item_vo.price = item[1].price
        order_item_vo.total_price = item[1].total_price

        db.session.add(order_item_vo)
        db.session.commit()
    cart_dao.delete_cart_all_item(user_id)

    return redirect('/user/view_cart')


