from flask import render_template,session


from base.com.dao.user_order_dao import OrderDAO


from base import app
from base.com.controller.login_controller import login_required

@app.route('/user/profile')
@login_required('user')
def user_profile():
    try:
        return render_template('user/userDashboard.html')
    except:
        return render_template('user/viewError.html')

@app.route('/user/order')
@login_required('user')
def user_order():
    try:
        order_dao = OrderDAO()

        user_id = session.get('user_id')
        order_data = order_dao.view_order(user_id)
        print(order_data)
        return render_template('user/order.html',order_data=order_data)
    except:
        return render_template('user/viewError.html')
@app.route('/user/change_password')
@login_required('user')
def user_change_password():
    try:
        return render_template('user/changePassword.html')
    except:
        return render_template('user/viewError.html')
