from base import app
from flask import render_template,redirect,request

from base.com.dao.city_dao import CityDAO
from base.com.dao.area_dao import AreaDAO

from base.com.vo.area_vo import AreaVO
from base.com.vo.city_vo import CityVO

@app.route('/admin/add_area')
def add_area():
    area_dao = AreaDAO()
    city_list = area_dao.city_data()
    return render_template('/admin/addArea.html',city_list=city_list)

@app.route('/admin/insert_area',methods=['POST'])
def insert_area():
    area_dao = AreaDAO()
    area_vo = AreaVO()

    area_vo.area_city_id = request.form.get('area_city_id')
    area_vo.area_name = request.form.get('area_name')

    area_dao.add_area(area_vo)
    return redirect('/admin/add_area')

@app.route('/admin/view_area')
def view_area():
    area_dao = AreaDAO()

    area_list = area_dao.view_area()
    return render_template('/admin/viewArea.html',area_list=area_list)

@app.route('/admin/delete_area')
def delete_area():
    area_dao = AreaDAO()

    area_id = request.args.get('area_id')
    print(area_id)
    area_dao.delete_area(area_id)
    return redirect('/admin/view_area')

@app.route('/admin/edit_area')
def edit_area():
    area_dao = AreaDAO()
    area_vo = AreaVO()
    city_dao = CityDAO()

    area_vo.area_id = request.args.get('area_id')
    area_list = area_dao.edit_area(area_vo)

    city_list = city_dao.view_city()
    return render_template('/admin/editArea.html',area_list=area_list,city_list=city_list)

@app.route('/admin/update_area',methods=['POST'])
def update_area():
    area_dao = AreaDAO()
    area_vo = AreaVO()

    area_vo.area_id = request.form.get('area_id')
    area_vo.area_name = request.form.get('area_name')
    area_vo.area_city_id = request.form.get('area_city_id')

    area_dao.update_area(area_vo)
    return redirect('/admin/view_area')