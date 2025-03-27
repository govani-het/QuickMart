import os
from flask import render_template,request,redirect
from base import app
from base.com.dao.city_dao import CityDAO
from base.com.vo.city_vo import CityVO

@app.route('/admin/add_city')
def addcity():
    return render_template('/admin/addCity.html')

@app.route('/admin/insert_city',methods=['POST'])
def insert_city():
    city_vo = CityVO()
    city_dao = CityDAO()

    city_vo.city_name = request.form['city_name']
    city_dao.insert_city(city_vo)
    return redirect('/admin/add_city')

@app.route('/admin/view_city')
def view_city():
    city_dao = CityDAO()
    city_list = city_dao.view_city()
    return render_template('/admin/viewCity.html',city_list=city_list)

@app.route('/admin/delete_city')
def delete_city():
    city_vo = CityVO()
    city_dao = CityDAO()

    city_vo.city_id = request.args['city_id']
    city_dao.delete_city(city_vo)
    return redirect('/admin/view_city')

@app.route('/admin/edit_city')
def edit_city():
    city_vo = CityVO()
    city_dao = CityDAO()
    city_vo.city_id = request.args['city_id']
    city_list = city_dao.edit_city(city_vo)

    return render_template('/admin/editCity.html',city_list=city_list)

@app.route('/admin/update_city',methods=['POST'])
def update_city():
    city_vo = CityVO()
    city_dao = CityDAO()
    city_vo.city_id = request.form['city_id']
    city_vo.city_name = request.form['city_name']

    city_dao.update_city(city_vo)
    return redirect('/admin/view_city')