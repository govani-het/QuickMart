from flask import render_template,request,redirect

from base.com.dao.category_dao import CategoryDAO
from base.com.dao.subcategory_dao import SubcategoryDAO


from base.com.vo.subcategory_vo import SubCategoryVO

from base.com.controller.login_controller import login_required
from base import app


#Displays the form to add a new subcategory with the list of available categories.
@app.route('/admin/add_subcategory')
@login_required('admin')
def add_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()
        subcategory_category_list = subcategory_dao.category_data()
        print(subcategory_category_list)
        return render_template('admin/addSubcategory.html', subcategory_category_list=subcategory_category_list)
    except Exception as ex:
        print("admin_load_subcategory route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html',ex=ex)

#Handles the insertion of a new subcategory into the database using form data.
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
    except Exception as ex:
        print("insert_subcategory route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html',ex=ex)


#Displays the list of all subcategories for the admin.
@app.route('/admin/view_subcategory')
@login_required('admin')
def view_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()
        subcategory_list = subcategory_dao.view_subcategory()
        return render_template('admin/viewSubcategory.html',subcategory_list=subcategory_list)
    except Exception as ex:
        print("admin_view_subcategory route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html',ex=ex)


#Deletes a subcategory from the database based on the provided subcategory ID.
@app.route('/admin/delete_subcategory')
@login_required('admin')
def delete_subcategory():
    try:
        subcategory_dao = SubcategoryDAO()

        subcategory_id = request.args.get('subcategory_id')

        subcategory_dao.delete_subcategory(subcategory_id)
        return redirect('/admin/view_subcategory')
    except Exception as ex:
        print("admin_load_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html',ex=ex)


#Loads the subcategory's current data into a form for editing, along with the category list.
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
    except Exception as ex:
        print("edit_subcategory route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html')


#Updates the subcategory information in the database using form data.
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
    except Exception as ex:
        print("admin_update_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html')