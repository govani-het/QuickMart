from flask import render_template, request,jsonify

from base.com.dao.user_subcategory_dao import UserSubcategoryDao

from base import app

from base.com.controller.login_controller import login_required

#Displays the list of subcategories and the corresponding products for a specific category.
@app.route('/user/subcategory')
@login_required('user')
def load_user_subcategory():
    try:
        subcategory_dao = UserSubcategoryDao()

        category_id = request.args.get('category_id')

        subcategory_list = subcategory_dao.load_subcategory_data(category_id)

        default_product_id = subcategory_list[0].subcategory_id
        product_list = subcategory_dao.load_product_list(default_product_id)
        return render_template('user/subCategoryList.html', subcategory_list=subcategory_list, product_list=product_list)
    except:
        return render_template('user/viewError.html')

#Loads the list of products dynamically using AJAX for a given subcategory.
@app.route('/user/ajax_product_list')
@login_required('user')
def load_user_ajax_product():
    try:
        subcategory_dao = UserSubcategoryDao()
        subcategory_id = request.args.get('subcategory_id')

        product_list = subcategory_dao.load_product_list(subcategory_id)

        json_product_list = [i.as_dict() for i in product_list]

        return jsonify(json_product_list)
    except:
        return render_template('user/viewError.html')

#Displays detailed information about a specific product.
@app.route('/user/view_product')
@login_required('user')
def load_user_view_product():
    try:
        subcategory_dao = UserSubcategoryDao()

        product_id = request.args.get('product_id')

        product_list = subcategory_dao.load_product(product_id)

        return render_template('user/productDetail.html', product_list=product_list)
    except:
        return render_template('user/viewError.html')