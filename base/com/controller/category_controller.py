from flask import Flask, render_template, request, redirect
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO
from werkzeug.utils import secure_filename
from base.com.controller.login_controller import login_required

import os
from base import app

CATEGORY_FOLDER = 'base/static/adminResources/category/'
app.config['CATEGORY_FOLDER'] = CATEGORY_FOLDER


#this function use to load add category page from Admin side
@app.route('/admin/add_category')
@login_required('admin')
def addCategory():
    try:
        return render_template('admin/addCategory.html')
    except Exception as ex:
        print("admin_load_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)

#this function is use to insert category info into database insert by Admin
@app.route('/admin/insert_category',methods=['POST'])
@login_required('admin')
def insertCategory():
    try:
        category_dao = CategoryDAO()
        category_vo = CategoryVO()

        category_image = request.files.get('category_img')

        category_image_name = secure_filename(category_image.filename)
        category_image_path = os.path.join(app.config['CATEGORY_FOLDER'])
        category_image.save(os.path.join(category_image_path, category_image_name))

        category_vo.category_name = request.form.get('category_name')
        category_vo.category_description = request.form.get('category_description')
        category_vo.category_image_name = category_image_name
        category_vo.category_image_path = category_image_path.replace("base",
                                                                   "..")
        category_dao.insert_category(category_vo)
        return redirect('/admin/add_category')

    except Exception as ex:
        print("admin_insert_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html',ex=ex)


#this function is use to view category which is inserted by Admin
@app.route('/admin/view_category')
@login_required('admin')
def viewCategory():
    try:
        category_dao = CategoryDAO()
        category_vo_list=category_dao.view_category()
        return render_template('admin/viewCategory.html',category_vo_list=category_vo_list)
    except Exception as ex:
        print("view_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html',ex=ex)

#this function is use to delete category by category_id from Admin side
@app.route('/admin/delete_category')
@login_required('admin')
def deleteCategory():
    try:
        category_dao = CategoryDAO()
        category_vo = CategoryVO()

        category_id = request.args.get('category_id')
        category_vo.category_id = category_id

        category_dao.delete_category(category_vo)
        return redirect('/admin/view_category')
    except Exception as ex:
        print("delete_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html',ex=ex)

#this function is use to load edit category page from Admin side
@app.route('/admin/edit_category')
@login_required('admin')
def editCategory():
    try:
        category_dao = CategoryDAO()
        category_vo = CategoryVO()
        category_id = request.args.get('category_id')
        category_vo.category_id = category_id
        category_vo_list = category_dao.edit_category(category_vo)
        return render_template('admin/editCategory.html',category_vo_list=category_vo_list)

    except Exception as ex:
        print("edit_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html',ex=ex)

#this function use to update category data and save in database byAdmin
@app.route('/admin/update_category',methods=['POST'])
@login_required('admin')
def updateCategory():
    try:
        category_dao = CategoryDAO()
        category_vo = CategoryVO()

        category_image = request.files.get('category_img')

        category_image_name = secure_filename(category_image.filename)
        category_image_path = os.path.join(app.config['CATEGORY_FOLDER'])
        category_image.save(os.path.join(category_image_path, category_image_name))

        category_vo.category_id = request.form.get('category_id')
        category_vo.category_name = request.form.get('category_name')
        category_vo.category_description = request.form.get('category_description')
        category_vo.category_image_name = category_image_name
        category_vo.category_image_path = category_image_path.replace("base",
                                                                      "..")

        category_dao.update_category(category_vo)
        return redirect('/admin/view_category')

    except Exception as ex:
        print("update_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html',ex=ex)