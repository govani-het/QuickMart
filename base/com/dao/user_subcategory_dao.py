
from base.com.vo.subcategory_vo import SubCategoryVO
from base.com.vo.product_vo import ProductVO
class UserSubcategoryDao:
    def load_subcategory_data(self,category_id):
        subcategory_vo_list = SubCategoryVO.query.filter_by(subcategory_category_id=category_id).all()
        return subcategory_vo_list

    def load_product_list(self,subcategory_id):
        default_product_vo_list = ProductVO.query.filter_by(product_subcategory_id=subcategory_id).all()
        return default_product_vo_list

    def load_product(self,product_id):
        product_vo_list = ProductVO.query.filter_by(product_id=product_id)
        return product_vo_list


