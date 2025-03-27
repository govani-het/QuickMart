from flask import Flask, render_template, request, redirect, url_for
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO
from werkzeug.utils import secure_filename

import os
from base import app

CATEGORY_FOLDER = 'base/static/adminResources/category/'
app.config['CATEGORY_FOLDER'] = CATEGORY_FOLDER

@app.route('/admin/add_category')
def addCategory():  # put application's code here
    return render_template('admin/addCategory.html')

@app.route('/admin/insert_category',methods=['POST'])
def insertCategory():
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

@app.route('/admin/view_category')
def viewCategory():  # put application's code here
    category_dao = CategoryDAO()
    category_vo_list=category_dao.view_category()
    return render_template('admin/viewCategory.html',category_vo_list=category_vo_list)

@app.route('/admin/delete_category')
def deleteCategory():
    category_dao = CategoryDAO()
    category_vo = CategoryVO()

    category_id = request.args.get('category_id')
    category_vo.category_id = category_id

    category_dao.delete_category(category_vo)
    return redirect('/admin/view_category')

@app.route('/admin/edit_category')
def editCategory():
    category_dao = CategoryDAO()
    category_vo = CategoryVO()
    category_id = request.args.get('category_id')
    category_vo.category_id = category_id
    category_vo_list = category_dao.edit_category(category_vo)
    return render_template('admin/editCategory.html',category_vo_list=category_vo_list)

@app.route('/admin/update_category',methods=['POST'])
def updateCategory():
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

