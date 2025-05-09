from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.vo.category_vo import CategoryVO
from base import db

class SubcategoryDAO:

    def category_data(self):
        category_vo_list = CategoryVO.query.all()
        return category_vo_list

    def insert_subcategory(self, subcategory_vo):
        db.session.add(subcategory_vo)
        db.session.commit()

    def view_subcategory(self):
        subcategory_vo_list = db.session.query(CategoryVO,SubCategoryVO).join(CategoryVO,SubCategoryVO.subcategory_category_id==CategoryVO.category_id).all()
        return subcategory_vo_list

    def delete_subcategory(self, subcategory_id):
        subcategory_vo = SubCategoryVO.query.get(subcategory_id)
        db.session.delete(subcategory_vo)
        db.session.commit()

    def edit_subcategory(self, subcategory_vo):
        subcategory_vo_list = SubCategoryVO.query.filter_by(subcategory_id=subcategory_vo.subcategory_id)
        return subcategory_vo_list

    def update_subcategory(self, subcategory_vo):
        db.session.merge(subcategory_vo)
        db.session.commit()

    def ajax_subcategory(self, subcategory_vo):
        ajax_subcategory_vo_list = SubCategoryVO.query.filter_by(subcategory_category_id=subcategory_vo.subcategory_category_id).all()
        return ajax_subcategory_vo_list