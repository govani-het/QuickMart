from base import db
from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.user_address_vo import UserAddressVO
from base.com.vo.product_vo import ProductVO
from datetime import datetime

class OrderVO(db.Model):
    __tablename__ = 'user_order_vo'
    order_id = db.Column('order_id', db.Integer, primary_key=True, autoincrement=True)
    address_id = db.Column('address_id', db.Integer, db.ForeignKey(UserAddressVO.address_id, ondelete='CASCADE',
                                                                   onupdate='CASCADE'), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey(UserRegisterVO.id, ondelete='CASCADE',
                                                             onupdate='CASCADE'), nullable=False)
    final_price = db.Column('final_price', db.Integer, nullable=False)

    status = db.Column(db.String(20), nullable=False, default='Pending')
    payment_method = db.Column(db.String(50), nullable=False)
    current_date = db.Column(db.DateTime, default=datetime.utcnow)


    def as_dict(self):
        return {
            'order_id': self.order_id,
            'address_id': self.address_id,
            'user_id': self.user_id,
            'final_price': self.final_price,
            'status': self.status,
            'payment_method': self.payment_method,
            'current_date': self.current_date
        }

    db.create_all()