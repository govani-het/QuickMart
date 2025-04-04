from flask import Flask, render_template, request, redirect, url_for,jsonify
from base.com.dao.user_subcategory_dao import UserSubcategoryDao

from base import app

@app.route('/user/subcategory')
def load_user_subcategory():
    subcategory_dao = UserSubcategoryDao()

    category_id = request.args.get('category_id')

    subcategory_list = subcategory_dao.loadSubcategoryData(category_id)

    default_product_id = subcategory_list[0].subcategory_id
    product_list = subcategory_dao.loadProductlist(default_product_id)
    return render_template('user/subCategoryList.html', subcategory_list=subcategory_list, product_list=product_list)

@app.route('/user/ajax_product_list')
def load_user_ajax_product():
    subcategory_dao = UserSubcategoryDao()
    subcategory_id = request.args.get('subcategory_id')

    product_list = subcategory_dao.loadProductlist(subcategory_id)

    json_product_list = [i.as_dict() for i in product_list]

    return jsonify(json_product_list)

@app.route('/user/view_product')
def load_user_view_product():
    subcategory_dao = UserSubcategoryDao()

    product_id = request.args.get('product_id')

    product_list = subcategory_dao.loadProduct(product_id)

    return render_template('user/productDetail.html', product_list=product_list)