from base import db

from base.com.vo.cart_vo import CartVO
from base.com.vo.product_vo import ProductVO

class CartDAO:

    def add_cart(self,cart_vo):
        db.session.add(cart_vo)
        db.session.commit()

    def get_cart_data(self,user_id):
        cart_data = db.session.query(ProductVO, CartVO).join(ProductVO, ProductVO.product_id == CartVO.product_id).filter(CartVO.user_id == user_id).all()
        return cart_data

    def delete_cart(self,cart_id):
        cart_vo = CartVO.query.get(cart_id)
        db.session.delete(cart_vo)
        db.session.commit()

    def delete_cart_all_item(self,user_id):
        CartVO.query.filter_by(user_id=user_id).delete()
        db.session.commit()

    def get_cart_item(self,user_id,product_id):
        cart_vo = CartVO.query.filter_by(user_id=user_id,product_id=product_id).first()
        return cart_vo


    def mearge_cart(self,cart_vo):
        db.session.merge(cart_vo)
        db.session.commit()