from base import db

from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.city_vo import CityVO
from base.com.vo.area_vo import AreaVO
from base.com.vo.user_address_vo import UserAddressVO

class UserAddressDAO:

    def getUserinfo(self,user_id):
        user = UserRegisterVO.query.filter_by(id=user_id).first()
        return user

    def getArea(self,city_vo):
        area_vo = AreaVO.query.filter_by(area_city_id=city_vo.area_city_id).all()
        return area_vo
    def add_address(self, address_vo):
        db.session.add(address_vo)
        db.session.commit()

    def view_address(self,user_id):
        address_vo = UserAddressVO.query.filter_by(user_id=user_id).first()
        return address_vo

    def update_address(self,address_vo):
        db.session.merge(address_vo)
        db.session.commit()