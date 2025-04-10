import os
from base import app

from flask import Flask, render_template, request, redirect, url_for,session,jsonify

#here all vo
from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.user_address_vo import UserAddressVO
from base.com.vo.user_order_item_vo import OrderItemVO
from base.com.vo.user_order_vo import OrderVO

#here all DAO

from base.com.dao.admin_order_dao import AdminOrderDAO

@app.route('/admin/view_order')
def view_order():
    admin_order_dao = AdminOrderDAO()

    order_list = admin_order_dao.viewOrder()
    print(">>>>>>>>>>>>>>>>",order_list)
    return render_template('admin/viewOrder.html',order_list=order_list)

@app.route('/admin/view_order_list')
def view_order_list():
    admin_order_dao = AdminOrderDAO()
    order_id = request.args.get('order_id')

    order_item_list = admin_order_dao.viewOrderItem(order_id)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>",order_item_list)
    return render_template('admin/viewOrderItem.html',order_item_list=order_item_list)