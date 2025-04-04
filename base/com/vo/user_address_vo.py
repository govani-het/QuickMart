from base import db

from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.city_vo import CityVO
from base.com.vo.area_vo import AreaVO

from base.com.vo.product_vo import ProductVO
class UserAddressVO(db.Model):
    __tablename__ = 'user_address'
    address_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserRegisterVO.id, ondelete='CASCADE',onupdate='CASCADE'), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.Text,nullable=False)
    city = db.Column(db.Integer,db.ForeignKey(CityVO.city_id, ondelete='CASCADE',onupdate='CASCADE'),nullable=False)
    area = db.Column(db.Integer,db.ForeignKey(AreaVO.area_id, ondelete='CASCADE',onupdate='CASCADE'),nullable=False)
    pincode = db.Column(db.Integer,nullable=False)

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