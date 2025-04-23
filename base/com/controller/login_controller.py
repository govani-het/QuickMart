from functools import wraps
from base import app
import bcrypt
import httpagentparser
import jwt
from datetime import timedelta, datetime
from flask import render_template, redirect, request, url_for, make_response, \
    flash, session


from base.com.dao.category_dao import CategoryDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.device_info_dao import DeviceInfoDAO

from base.com.vo.device_info_vo import DeviceInfoVO
from base.com.vo.user_register_vo import UserRegisterVO


app.permanent_session_lifetime = timedelta(minutes=30)
def get_client_identity():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)

    agent = request.environ.get('HTTP_USER_AGENT')
    browser = httpagentparser.detect(agent)
    if not browser:
        browser = agent.split('/')[0]
    else:
        browser = browser['browser']['name']
    return "{}:{}".format(ip_addr, browser)

def insert_client_identity(login_id):
    login_vo = UserRegisterVO
    login_vo.id = login_id

    device_info_dao = DeviceInfoDAO()
    device_info_vo = DeviceInfoVO()

    device_list = device_info_dao.search_device(login_vo)

    for device in device_list:
        if bcrypt.checkpw(get_client_identity().encode("utf-8"),
                          device.device_identity.encode("utf-8")):
            device_info_vo = device
            break

    hashed_client_identity = bcrypt.hashpw(
        get_client_identity().encode("utf-8"),
        bcrypt.gensalt(rounds=12))
    device_info_vo.device_identity = hashed_client_identity
    device_info_vo.device_login_id = login_id

    device_info_dao.insert_device_info(device_info_vo)

def refresh_token(fn):
    try:
        refreshtoken = request.cookies.get('refreshtoken')

        if refreshtoken is not None:
            data = jwt.decode(refreshtoken, app.config['SECRET_KEY'], algorithms=['HS256'])

            login_vo = UserRegisterVO()
            login_dao = LoginDAO()

            login_vo.email = data['public_id']
            user = login_dao.check_login_username(login_vo)

            device_info_dao = DeviceInfoDAO()
            device_list = device_info_dao.search_device(user)

            for device in device_list:
                print('In Token Refresh')
                if bcrypt.checkpw(get_client_identity().encode("utf-8"),
                                  device.device_identity.encode("utf-8")):
                    print('Device Matched')
                    response = make_response(fn())
                    response.set_cookie('accesstoken',
                                        value=jwt.encode({
                                            'public_id': user.email,
                                            'role': user.login_role,
                                            'exp': datetime.utcnow() + timedelta(seconds=30)
                                        }, app.config['SECRET_KEY'],
                                            algorithm='HS256'),
                                        max_age=30)
                    refresh = jwt.encode({
                        'public_id': user.email,
                        'exp': datetime.utcnow() + timedelta(hours=1)
                    }, app.config['SECRET_KEY'], algorithm='HS256')

                    print('Token Refreshed Successfully')
                    response.set_cookie('refreshtoken',
                                        value=refresh,
                                        max_age=3600)
                    return response
                else:
                    flash('We encountered malicious activity. Please re-login.')
                    return admin_logout_session(login_vo.email) or redirect('/')
            else:
                flash('Unauthorized Access')
                return admin_logout_session() or redirect('/')

        # If refresh token is not found
        flash('No refresh token found. Please log in again.')
        return redirect('/')

    except Exception as ex:
        print('Exception in Refreshing Token >>>', ex)
        flash('Session expired. Please log in again.')
        return redirect('/')


def login_required(role):
    def inner(fn):
        @wraps(fn)
        def decorator():
            try:
                accesstoken = request.cookies.get('accesstoken')

                if accesstoken is None:
                    return refresh_token(fn)
                else:
                    data = jwt.decode(accesstoken, app.config['SECRET_KEY'],
                                      'HS256')
                    login_vo = UserRegisterVO()
                    login_dao = LoginDAO()

                    login_vo.email = data['public_id']

                    login_list = login_dao.check_login_username(login_vo)

                    if login_list.login_status == 1 and data['role'] == role:
                        return fn()
                    else:
                        return redirect('/')

            except Exception as ex:
                print(ex)
                return refresh_token(fn)

        return decorator

    return inner



@app.route("/admin/validate_login", methods=['POST'])
def admin_validate_login():
    try:
        email = request.form.get('email')
        password = request.form.get('password').encode("utf-8")

        login_vo = UserRegisterVO()
        login_dao = LoginDAO()

        login_vo.email = email

        user_data = login_dao.check_login_username(login_vo)

        if not user_data:

            flash('username is incorrect !','error')
            return redirect('/')
        elif user_data.login_status != 1:

            flash('You have been temporarily blocked by website admin !', 'error')
            return redirect('/')
        else:
            email = user_data.email
            login_role = user_data.login_role
            hashed_login_password = user_data.password.encode(
                "utf-8")
            if bcrypt.checkpw(password, hashed_login_password):

                insert_client_identity(user_data.id)

                if login_role == 'admin':
                    response = make_response(
                        redirect(url_for('admin_load_dashboard')))
                    response.set_cookie('accesstoken',
                                        value=jwt.encode({
                                            'public_id': email,
                                            'role': login_role,
                                            'exp': datetime.utcnow() + timedelta(
                                                seconds=30)
                                        }, app.config['SECRET_KEY'], 'HS256'),
                                        max_age=timedelta(seconds=30))
                    refresh = jwt.encode({
                        'public_id': email,
                        'exp': datetime.utcnow() + timedelta(hours=1)
                    }, app.config['SECRET_KEY'], 'HS256')

                    response.set_cookie('refreshtoken',
                                        value=refresh,
                                        max_age=timedelta(hours=1))
                    return response

                elif login_role == 'user':
                    response = make_response(
                        redirect(url_for('user_load_dashboard')))
                    response.set_cookie('accesstoken',
                                        value=jwt.encode({
                                            'public_id': email,
                                            'role': login_role,
                                            'exp': datetime.utcnow() + timedelta(
                                                seconds=30)
                                        }, app.config['SECRET_KEY'], 'HS256'),
                                        max_age=timedelta(seconds=30))
                    refresh = jwt.encode({
                        'public_id': email,
                        'exp': datetime.utcnow() + timedelta(hours=1)
                    }, app.config['SECRET_KEY'], 'HS256')
                    response.set_cookie('refreshtoken',
                                        value=refresh,
                                        max_age=timedelta(hours=1))

                    session['user_id'] = user_data.id
                    session['username'] = user_data.username
                    session['email'] = user_data.email
                    session['phone'] = user_data.phone
                    return response

                else:
                    return admin_logout_session()
            else:

                flash('password is incorrect !','error')
                return redirect('/')
    except Exception as ex:
        print("admin_validate_login route exception occured>>>>>>>>>>", ex)
        return redirect(url_for('admin_logout_session'))


@app.route('/admin/load_dashboard', methods=['GET'])
@login_required('admin')
def admin_load_dashboard():
    try:
        return render_template('admin/index.html')
    except Exception as ex:
        print("admin_load_dashboard route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/user/load_dashboard', methods=['GET'])
@login_required('user')
def user_load_dashboard():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        return render_template('user/index.html',category_list=category_vo_list)
    except Exception as ex:
        print("user_load_dashboard route exception occured>>>>>>>>>>", ex)
        return render_template('user/viewError.html', ex=ex)

@app.route("/admin/logout_session", methods=['GET'])
def admin_logout_session(*user_name):
    session.clear()
    if len(user_name) != 0 and user_name[0] is not None:
        login_vo = UserRegisterVO()
        login_dao = LoginDAO()
        device_info_dao = DeviceInfoDAO()

        login_vo.email = user_name[0]

        user_data = login_dao.check_login_username(login_vo)

        login_id = user_data.id
        device_info_dao.delete_all_device(login_id)

        response = make_response(redirect('/'))
        response.set_cookie('accesstoken', max_age=0)
        response.set_cookie('refreshtoken', max_age=0)
        return response
    elif request.cookies.get('refreshtoken') is not None:
        refreshtoken = request.cookies.get('refreshtoken')

        data = jwt.decode(refreshtoken, app.config['SECRET_KEY'], 'HS256')

        login_vo = UserRegisterVO()
        login_dao = LoginDAO()
        device_info_dao = DeviceInfoDAO()
        device_info_vo = DeviceInfoVO()

        login_vo.email = data['public_id']

        user_data = login_dao.check_login_username(login_vo)
        login_vo = user_data

        device_list = device_info_dao.search_device(login_vo)

        if len(device_list) != 0:
            for device in device_list:
                if bcrypt.checkpw(get_client_identity().encode("utf-8"),
                                  device.device_identity.encode("utf-8")):
                    device_info_vo = device
                    break

            device_info_dao.delete_device(device_info_vo)

        response = make_response(redirect('/'))
        response.set_cookie('accesstoken', max_age=0)
        response.set_cookie('refreshtoken', max_age=0)
        return response
    else:
        response = make_response(redirect('/'))
        response.set_cookie('accesstoken', max_age=0)
        response.set_cookie('refreshtoken', max_age=0)

        return response


