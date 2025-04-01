from base import db
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.vo.product_vo import ProductVO
class UserSubcategoryDao:
    def loadSubcategoryData(self,category_id):
        subcategory_vo_list = SubCategoryVO.query.filter_by(subcategory_category_id=category_id).all()
        return subcategory_vo_list

    def loadProduct(self,subcategory_id):
        default_product_vo_list = ProductVO.query.filter_by(product_subcategory_id=subcategory_id).all()
        return default_product_vo_list

