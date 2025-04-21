from flask import Flask, render_template, request, redirect, session
from base.com.vo.user_address_vo import UserAddressVO
from base.com.dao.user_address_dao import UserAddressDAO
from base.com.dao.city_dao import CityDAO
from base.com.dao.area_dao import AreaDAO
from base import app
from base.com.controller.login_controller import login_required

# Route to load the page where the user can add a new address or view existing ones.
@app.route('/user/load_add_address_page')
@login_required('user')
def load_user_add_address_page():
    try:
        user_dao = UserAddressDAO()
        city_dao = CityDAO()
        user_id = session.get('user_id')

        # Get all addresses of the current user and all cities for the dropdown
        user_address_info = user_dao.view_address(user_id)
        city = city_dao.view_city()

        return render_template('user/addAddress.html', user_address_info=user_address_info, city=city)
    except:
        return render_template('user/viewError.html')

# Route to handle the form submission for adding or updating a user's address
@app.route('/user/add_address', methods=['POST'])
@login_required('user')
def user_add_address():
    try:
        user_dao = UserAddressDAO()
        user_address_vo = UserAddressVO()
        user_id = session.get('user_id')

        # Get address details from the form
        address_id = request.form.get('address_id')
        user_address_vo.address_id = address_id
        user_address_vo.user_id = user_id
        user_address_vo.username = request.form.get('username')
        user_address_vo.email = request.form.get('email')
        user_address_vo.phone = request.form.get('phone')
        user_address_vo.address = request.form.get('address')
        user_address_vo.city = request.form.get('city')
        user_address_vo.area = request.form.get('area')
        user_address_vo.pincode = request.form.get('pincode')

        # If address_id exists, update the address. Otherwise, insert a new one.
        if address_id:
            user_dao.update_address(user_address_vo)
        else:
            user_dao.add_address(user_address_vo)

        return redirect('/user/view_address')
    except:
        return render_template('user/viewError.html')

# Route to view all addresses of the currently logged-in user
@app.route('/user/view_address')
@login_required('user')
def user_view_address():
    try:
        user_dao = UserAddressDAO()
        user_id = session.get('user_id')

        # Fetch all addresses for the user
        user_address_info = user_dao.view_address(user_id)
        return render_template('user/address.html', user_address_info=user_address_info)
    except:
        return render_template('user/viewError.html')

# Route to delete a user's address
@app.route('/user/delete_address')
@login_required('user')
def user_delete_address():
    try:
        user_address_dao = UserAddressDAO()
        user_address_vo = UserAddressVO()

        # Get address_id from the query string and delete that address
        user_address_vo.address_id = request.args.get('address_id')
        user_address_dao.delete_address(user_address_vo)
        return redirect('/user/view_address')
    except:
        return render_template('user/viewError.html')

# Route to load the update address form with prefilled data for a specific address
@app.route('/user/update_address')
@login_required('user')
def user_edit_address():
    try:
        city_dao = CityDAO()
        area_dao = AreaDAO()
        user_address_dao = UserAddressDAO()
        user_address_vo = UserAddressVO()

        user_address_vo.address_id = request.args.get('address_id')
        user_address_data = user_address_dao.edit_address(user_address_vo)

        city = city_dao.view_city()
        area = area_dao.view_area()

        return render_template('user/updateAddress.html', city=city, area=area, user_address_info=user_address_data)
    except:
        return render_template('user/viewError.html')
