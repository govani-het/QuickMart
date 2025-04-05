from base import db

from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.user_address_vo import UserAddressVO
from base.com.vo.user_order_item_vo import OrderItemVO
from base.com.vo.user_order_vo import OrderVO

from base.com.vo.city_vo import CityVO
from base.com.vo.area_vo import AreaVO

class AdminOrderDAO:

    def viewOrder(self):
        order_list = db.session.query(UserAddressVO,OrderVO,CityVO,AreaVO).join(UserAddressVO,OrderVO.user_id==UserAddressVO.user_id).join(CityVO, UserAddressVO.city == CityVO.city_id).join(AreaVO, UserAddressVO.area == AreaVO.area_id).all()
        return order_list