from base import db

from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.product_vo import ProductVO
class UserAddressVO(db.Model):
    __tablename__ = 'user_address'
    address_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserRegisterVO.user_id, ondelete='CASCADE',onupdate='CASCADE'), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.Text,nullable=False)
    city = db.Column(db.String(80),nullable=False)
    area = db.Column(db.String(80),nullable=False)
    pincode = db.Column(db.Integer(80),nullable=False)

    def as_dict(self):
        return {
            'address_id':self.address_id,
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'city': self.city,
            'area': self.address_id,
            'pincode': self.pincode,

        }

    db.create_all()