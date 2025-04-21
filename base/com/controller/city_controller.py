from flask import render_template,request,redirect
from base import app

from base.com.dao.city_dao import CityDAO
from base.com.vo.city_vo import CityVO
from base.com.controller.login_controller import login_required


#Displays the form to add a new city.
@app.route('/admin/add_city')
@login_required('admin')
def addcity():
    try:
        return render_template('/admin/addCity.html')
    except:
        return render_template('admin/viewError.html')

#Handles form submission and inserts a new city record into the database.
@app.route('/admin/insert_city',methods=['POST'])
@login_required('admin')
def insert_city():
    try:
        city_vo = CityVO()
        city_dao = CityDAO()

        city_vo.city_name = request.form['city_name']
        city_dao.insert_city(city_vo)
        return redirect('/admin/add_city')
    except:
        return render_template('admin/viewError.html')


#Displays a list of all cities.
@app.route('/admin/view_city')
@login_required('admin')
def view_city():
    try:
        city_dao = CityDAO()
        city_list = city_dao.view_city()
        return render_template('/admin/viewCity.html',city_list=city_list)
    except:
        return render_template('admin/viewError.html')

#Deletes a city record from the database based on city ID passed via query string.
@app.route('/admin/delete_city')
@login_required('admin')
def delete_city():
    try:
        city_vo = CityVO()
        city_dao = CityDAO()

        city_vo.city_id = request.args['city_id']
        city_dao.delete_city(city_vo)
        return redirect('/admin/view_city')
    except:
        return render_template('admin/viewError.html')


#Loads the current city data into an edit form for modifications.
@app.route('/admin/edit_city')
@login_required('admin')
def edit_city():
    try:
        city_vo = CityVO()
        city_dao = CityDAO()
        city_vo.city_id = request.args['city_id']
        city_list = city_dao.edit_city(city_vo)

        return render_template('/admin/editCity.html',city_list=city_list)
    except:
        return render_template('admin/viewError.html')

#Updates an existing city record in the database using form data.
@app.route('/admin/update_city',methods=['POST'])
@login_required('admin')
def update_city():
    try:
        city_vo = CityVO()
        city_dao = CityDAO()
        city_vo.city_id = request.form['city_id']
        city_vo.city_name = request.form['city_name']

        city_dao.update_city(city_vo)
        return redirect('/admin/view_city')
    except:
        return render_template('admin/viewError.html')