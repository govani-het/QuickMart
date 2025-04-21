from base import app,db

from flask import render_template, request,jsonify

from base.com.vo.user_order_vo import OrderVO
from base.com.dao.admin_order_dao import AdminOrderDAO
from base.com.controller.login_controller import login_required
@app.route('/admin/view_order')
@login_required('admin')
def view_order():
    try:
        admin_order_dao = AdminOrderDAO()
        order_list = admin_order_dao.view_order()
        return render_template('admin/viewOrder.html',order_list=order_list)
    except:
        return render_template('user/viewError.html')
@app.route('/admin/view_order_list')
@login_required('admin')
def view_order_list():
    try:
        admin_order_dao = AdminOrderDAO()
        order_id = request.args.get('order_id')

        order_item_list = admin_order_dao.view_order_item(order_id)

        return render_template('admin/viewOrderItem.html',order_item_list=order_item_list)
    except:
        return render_template('user/viewError.html')

@app.route('/update_order_status', methods=['POST'])
def update_order_status():
    try:
        data = request.get_json()
        order_id = data['order_id']
        status = data['status']

        order = OrderVO.query.get(order_id)
        if order:
            order.status = status
            db.session.commit()
            return jsonify({'success': True})
        return jsonify({'success': False})
    except:
        return render_template('user/viewError.html')