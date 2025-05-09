from base import db

from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.city_vo import CityVO
from base.com.vo.area_vo import AreaVO
from base.com.vo.user_address_vo import UserAddressVO

class UserAddressDAO:

    def get_area(self,city_vo):
        area_vo = AreaVO.query.filter_by(area_city_id=city_vo.area_city_id).all()
        return area_vo
    def add_address(self, address_vo):
        db.session.add(address_vo)
        db.session.commit()

    def view_address(self,user_id):
        address_vo = db.session.query(UserAddressVO, CityVO, AreaVO).join(CityVO, UserAddressVO.city == CityVO.city_id).join(AreaVO, UserAddressVO.area == AreaVO.area_id).filter(UserAddressVO.user_id == user_id).all()
        return address_vo

    def update_address(self,address_vo):
        db.session.merge(address_vo)
        db.session.commit()

    def delete_address(self,address_vo):
        user_address = UserAddressVO.query.get(address_vo.address_id)
        db.session.delete(user_address)
        db.session.commit()

    def edit_address(self, address_vo):
        address_vo = UserAddressVO.query.filter_by(address_id=address_vo.address_id).first()
        return address_vo