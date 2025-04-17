from flask import render_template,request,redirect

from base.com.dao.category_dao import CategoryDAO
from base.com.dao.subcategory_dao import SubcategoryDAO


from base.com.vo.subcategory_vo import SubCategoryVO

from base.com.controller.login_controller import login_required
from base import app

@app.route('/admin/add_subcategory')
@login_required('admin')
def add_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()
        subcategory_category_list = subcategory_dao.category_data()
        print(subcategory_category_list)
        return render_template('admin/addSubcategory.html', subcategory_category_list=subcategory_category_list)
    except:
        return render_template('admin/viewError.html')
@app.route('/admin/insert_subcategory', methods=['POST'])
@login_required('admin')
def insert_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()
        subcategory_vo = SubCategoryVO()

        subcategory_vo.subcategory_name = request.form.get('subcategory_name')
        subcategory_vo.subcategory_description = request.form.get('subcategory_description')
        subcategory_vo.subcategory_category_id = request.form.get('subcategory_category')

        subcategory_dao.insert_subcategory(subcategory_vo)
        return redirect('/admin/add_subcategory')
    except:
        return render_template('admin/viewError.html')
@app.route('/admin/view_subcategory')
@login_required('admin')
def view_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()
        subcategory_list = subcategory_dao.view_subcategory()
        return render_template('admin/viewSubcategory.html',subcategory_list=subcategory_list)
    except:
        return render_template('admin/viewError.html')
@app.route('/admin/delete_subcategory')
@login_required('admin')
def delete_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()

        subcategory_id = request.args.get('subcategory_id')

        subcategory_dao.delete_subcategory(subcategory_id)
        return redirect('/admin/view_subcategory')
    except:
        return render_template('admin/viewError.html')
@app.route('/admin/edit_subcategory')
@login_required('admin')
def edit_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()
        subcategory_vo = SubCategoryVO()

        category_dao = CategoryDAO()

        subcategory_id = request.args.get('subcategory_id')
        subcategory_vo.subcategory_id = subcategory_id

        subcategory_vo_list = subcategory_dao.edit_subcategory(subcategory_vo)
        category_vo_list = category_dao.view_category()

        return render_template('/admin/editSubcategory.html', subcategory_vo_list=subcategory_vo_list, category_vo_list=category_vo_list)
    except:
        return render_template('admin/viewError.html')

@app.route('/admin/update_subcategory', methods=['POST'])
@login_required('admin')
def update_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()
        subcategory_vo = SubCategoryVO()

        subcategory_vo.subcategory_id = request.form.get('subcategory_id')
        subcategory_vo.subcategory_name = request.form.get('subcategory_name')
        subcategory_vo.subcategory_description = request.form.get('subcategory_description')
        subcategory_vo.subcategory_category_id = request.form.get('subcategory_category')


        subcategory_dao.update_subcategory(subcategory_vo)
        return redirect('/admin/view_subcategory')
    except:
        return render_template('admin/viewError.html')