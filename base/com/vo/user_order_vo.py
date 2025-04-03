from base import db
from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.product_vo import ProductVO
class OrderVO(db.Model):
    __tablename__ = 'user_order_vo'
    order_id = db.Column('order_id',db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column('user_id',db.Integer, db.ForeignKey(UserRegisterVO.id, ondelete='CASCADE',
                                                  onupdate='CASCADE'), nullable=False)
    product_id = db.Column('product_id',db.Integer, db.ForeignKey(ProductVO.product_id, ondelete='CASCADE',
                                                  onupdate='CASCADE'),nullable=False)
    quantity = db.Column('quantity',db.Integer,nullable=False)
    price = db.Column('price',db.Integer,nullable=False)
    total_price = db.Column('total_price',db.Integer,nullable=False)

    def as_dict(self):
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': self.price,
            'total_price': self.total_price
        }


db.create_all()