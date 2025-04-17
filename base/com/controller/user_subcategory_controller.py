from flask import render_template, request,jsonify

from base.com.dao.user_subcategory_dao import UserSubcategoryDao

from base import app

from base.com.controller.login_controller import login_required
@app.route('/user/subcategory')
@login_required('user')
def load_user_subcategory():
    subcategory_dao = UserSubcategoryDao()

    category_id = request.args.get('category_id')

    subcategory_list = subcategory_dao.load_subcategory_data(category_id)

    default_product_id = subcategory_list[0].subcategory_id
    product_list = subcategory_dao.load_product_list(default_product_id)
    return render_template('user/subCategoryList.html', subcategory_list=subcategory_list, product_list=product_list)

@app.route('/user/ajax_product_list')
@login_required('user')
def load_user_ajax_product():
    subcategory_dao = UserSubcategoryDao()
    subcategory_id = request.args.get('subcategory_id')

    product_list = subcategory_dao.load_product_list(subcategory_id)

    json_product_list = [i.as_dict() for i in product_list]

    return jsonify(json_product_list)

@app.route('/user/view_product')
@login_required('user')
def load_user_view_product():
    subcategory_dao = UserSubcategoryDao()

    product_id = request.args.get('product_id')

    product_list = subcategory_dao.load_product(product_id)

    return render_template('user/productDetail.html', product_list=product_list)