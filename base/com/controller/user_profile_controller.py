from flask import render_template,session,request
import bcrypt

from base.com.dao.user_order_dao import OrderDAO
from base.com.dao.login_dao import LoginDAO

from base.com.vo.user_register_vo import UserRegisterVO

from base import app,db
from base.com.controller.login_controller import login_required


#Displays the user's dashboard or profile page.
@app.route('/user/profile')
@login_required('user')
def user_profile():
    try:
        return render_template('user/userDashboard.html')
    except:
        return render_template('user/viewError.html')


#Displays the user's order history.
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

#Renders the change password page for the user.
@app.route('/user/change_password')
@login_required('user')
def user_change_password():
    try:
        return render_template('user/changePassword.html')
    except:
        return render_template('user/viewError.html')

@app.route('/user/update_password', methods=['POST'])
@login_required('user')
def user_update_password():
    try:
        login_dao = LoginDAO()
        login_vo = UserRegisterVO()

        email = session.get('email')
        current_password = request.form.get('current_password')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        login_vo.email = email

        user_data = login_dao.check_login_username(login_vo)
        if password != confirm_password:
            return render_template('user/changePassword.html',error='Passwords and Confirm Password do not match')

        elif user_data:
            hashed_login_password = user_data.password.encode("utf-8")
            if bcrypt.checkpw(current_password.encode('utf-8'), hashed_login_password):

                salt = bcrypt.gensalt(rounds=12)
                hashed_password = bcrypt.hashpw(password.encode("utf-8"),
                                                      salt)
                user_data.password = hashed_password
                db.session.commit()
                return render_template('user/changePassword.html',success="Password is changed")

            else:
                return render_template('user/changePassword.html', error="Your Current Password is incorrect")

    except Exception as ex:
        print(ex)
        return render_template("user/viewError.html")
