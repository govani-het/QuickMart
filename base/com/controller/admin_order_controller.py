from base import app

from flask import render_template, request

from base.com.dao.admin_order_dao import AdminOrderDAO
from base.com.controller.login_controller import login_required
@app.route('/admin/view_order')
@login_required('admin')
def view_order():
    admin_order_dao = AdminOrderDAO()
    order_list = admin_order_dao.view_order()
    return render_template('admin/viewOrder.html',order_list=order_list)

@app.route('/admin/view_order_list')
@login_required('admin')
def view_order_list():
    admin_order_dao = AdminOrderDAO()
    order_id = request.args.get('order_id')

    order_item_list = admin_order_dao.view_order_item(order_id)

    return render_template('admin/viewOrderItem.html',order_item_list=order_item_list)