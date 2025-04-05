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

    return render_template('admin/viewOrder.html',order_list=order_list)