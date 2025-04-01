from flask import Flask, render_template, request, redirect, url_for,jsonify
from base.com.dao.user_subcategory_dao import UserSubcategoryDao

from base import app

@app.route('/user/subcategory')
def load_user_subcategory():
    subcategory_dao = UserSubcategoryDao()

    category_id = request.args.get('category_id')

    subcategory_list = subcategory_dao.loadSubcategoryData(category_id)

    default_product_id = subcategory_list[0].subcategory_id
    product_list = subcategory_dao.loadProduct(default_product_id)
    return render_template('user/subCategoryList.html', subcategory_list=subcategory_list, product_list=product_list)

# @app.route('/user/loadProduct')
# def load_user_product():
#     subcategory_dao = UserSubcategoryDao()
#
#     subcategory_id = request.args.get('subcategory_id')
#     category_id = request.form.get('category_id')
#
#     product_list = subcategory_dao.loadProduct(subcategory_id)
#     subcategory_list = subcategory_dao.loadSubcategoryData(category_id)
#
#     return render_template('user/subCategoryList.html',subcategory_list=subcategory_list,product_list=product_list)

@app.route('/user/ajax_product')
def load_user_ajax_product():
    subcategory_dao = UserSubcategoryDao()
    subcategory_id = request.args.get('subcategory_id')

    product_list = subcategory_dao.loadProduct(subcategory_id)

    json_product_list = [i.as_dict() for i in product_list]

    return jsonify(json_product_list)
