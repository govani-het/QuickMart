from flask import render_template
from base.com.dao.category_dao import CategoryDAO
from base import app

@app.route("/")
def home_page():
    try:
        return render_template('user/login.html')
    except:
        return render_template('user/viewError.html')


#Displays the home page for users after they log in. It shows a list of categories for the user to browse.
@app.route("/user/home")
def user_home_page():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        return render_template('user/index.html', category_list=category_vo_list)
    except:
        return render_template('user/viewError.html')

#Displays the home page for administrators after they log in.
@app.route("/admin/home")
def admin_home_page():
    try:
        return render_template('admin/index.html')
    except:
        return render_template('Admin/viewError.html')