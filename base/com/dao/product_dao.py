from base import db
from base.com.vo.product_vo import ProductVO
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.vo.category_vo import CategoryVO


class ProductDAO:

    def add_product(self, product_vo):
        db.session.add(product_vo)
        db.session.commit()

    def view_product(self):
        product_vo_list = db.session.query(CategoryVO, SubCategoryVO, ProductVO).filter(CategoryVO.category_id == ProductVO.product_category_id).filter(SubCategoryVO.subcategory_id == ProductVO.product_subcategory_id).all()
        return product_vo_list

    def delete_product(self, product_id):
        product_vo = ProductVO.query.get(product_id)
        db.session.delete(product_vo)
        db.session.commit()

    def edit_product(self, product_vo):
        product_list = ProductVO.query.filter_by(product_id=product_vo.product_id)
        return product_list

    def update_product(self, product_vo):
        db.session.merge(product_vo)
        db.session.commit()