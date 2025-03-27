import os
from flask import render_template,request,redirect,jsonify
from werkzeug.utils import secure_filename

from base.com.dao.subcategory_dao import SubcategoryDAO
from base.com.vo import product_vo
from base.com.vo.subcategory_vo import SubCategoryVO

from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO

from base.com.dao.product_dao import ProductDAO
from base.com.vo.product_vo import ProductVO

from base import app

PRODUCT_FOLDER = 'base/static/adminResources/product/'
app.config['PRODUCT_FOLDER'] = PRODUCT_FOLDER

@app.route('/admin/add_product')
def add_product():
    category_dao = CategoryDAO()
    category_list = category_dao.view_category()
    return render_template('admin/addProduct.html',category_list=category_list)

@app.route('/ajax_subcategory_product')
def add_subcategory_product():
    subcategory_dao = SubcategoryDAO()
    subcategory_vo = SubCategoryVO()

    subcategory_vo.subcategory_category_id = request.args.get('product_category_id')
    subcategory_vo_list = subcategory_dao.ajax_subcategory(subcategory_vo)

    ajax_product_subcategory = [i.as_dict() for i in subcategory_vo_list]

    return jsonify(ajax_product_subcategory)

@app.route('/admin/insert_product', methods=['POST'])
def insert_product():
    product_vo = ProductVO()
    product_dao = ProductDAO()

    product_category_id = request.form.get('product_category_id')
    product_subcategory_id = request.form.get('product_subcategory_id')
    product_name = request.form.get('product_name')
    product_description = request.form.get('product_description')
    product_price = request.form.get('product_price')
    product_quantity = request.form.get('product_quantity')
    product_image = request.files.get('product_img')

    product_image_name = secure_filename(product_image.filename)
    product_image_path = os.path.join(app.config['PRODUCT_FOLDER'])
    product_image.save(os.path.join(product_image_path,product_image_name))

    product_vo.product_name = product_name
    product_vo.product_description = product_description
    product_vo.product_price = product_price
    product_vo.product_quantity = product_quantity
    product_vo.product_image_name = product_image_name
    product_vo.product_image_path = product_image_path.replace("base",
                                                               "..")
    product_vo.product_category_id = product_category_id
    product_vo.product_subcategory_id = product_subcategory_id

    product_dao.add_product(product_vo)

    return redirect('/admin/add_product')

@app.route('/admin/view_product')
def view_product():
    product_dao = ProductDAO()
    product_list = product_dao.view_product()
    return render_template('/admin/viewProduct.html',product_list=product_list)

@app.route('/admin/delete_product')
def delete_product():
    product_dao = ProductDAO()

    product_id = request.args.get('product_id')
    product_dao.delete_product(product_id)
    return redirect('/admin/view_product')

@app.route('/admin/edit_product')
def edit_product():
    product_vo = ProductVO()
    product_dao = ProductDAO()
    subcategory_dao = SubcategoryDAO()
    subcategory_vo = SubCategoryVO()
    category_dao = CategoryDAO()

    product_vo.product_id = request.args.get('product_id')
    product_list = product_dao.edit_product(product_vo)

    product_vo_dict = product_list[0].as_dict()
    product_category_id = product_vo_dict.get('product_category_id')
    subcategory_vo.subcategory_category_id = product_category_id

    category_list = category_dao.view_category()
    subcategory_list = subcategory_dao.ajax_subcategory(subcategory_vo)

    return render_template('/admin/editProduct.html',product_list=product_list,subcategory_list=subcategory_list,category_list=category_list)

@app.route('/admin/update_product',methods=['POST'])
def update_product():
    product_vo = ProductVO()
    product_dao = ProductDAO()

    product_id = request.form.get('product_id')
    product_category_id = request.form.get('product_category_id')
    product_subcategory_id = request.form.get('product_subcategory_id')
    product_name = request.form.get('product_name')
    product_description = request.form.get('product_description')
    product_price = request.form.get('product_price')
    product_quantity = request.form.get('product_quantity')
    product_image = request.files.get('product_img')

    product_image_name = secure_filename(product_image.filename)
    product_image_path = os.path.join(app.config['PRODUCT_FOLDER'])
    product_image.save(os.path.join(product_image_path, product_image_name))

    product_vo.product_id = product_id
    product_vo.product_name = product_name
    product_vo.product_description = product_description
    product_vo.product_price = product_price
    product_vo.product_quantity = product_quantity
    product_vo.product_image_name = product_image_name
    product_vo.product_image_path = product_image_path.replace("base",
                                                               "..")
    product_vo.product_category_id = product_category_id
    product_vo.product_subcategory_id = product_subcategory_id

    product_dao.update_product(product_vo)

    return redirect('/admin/view_product')
