from base import db

from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.city_vo import CityVO
from base.com.vo.area_vo import AreaVO

class UserAddressDAO:

    def getUserinfo(self,user_id):
        user = UserRegisterVO.query.filter_by(id=user_id).first()
        return user

    def getCity(self):
        city = CityVO.query.all()
        return city

    def getArea(self,city_vo):
        area_vo = AreaVO.query.filter_by(area_city_id=city_vo.area_city_id).all()
        return area_vo