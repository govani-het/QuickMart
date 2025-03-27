from base import db
from base.com.vo.city_vo import CityVO
from base.com.vo.area_vo import AreaVO

class AreaDAO:

    def city_data(self):
        city_list = CityVO.query.all()
        return city_list

    def add_area(self,area_vo):
        db.session.add(area_vo)
        db.session.commit()

    def view_area(self):
        area_vo = db.session.query(CityVO,AreaVO).join(CityVO,CityVO.city_id==AreaVO.area_city_id).all()
        return area_vo

    def delete_area(self,area_id):
        area_vo = AreaVO.query.get(area_id)
        db.session.delete(area_vo)
        db.session.commit()

    def edit_area(self,area_vo):
        area_list = AreaVO.query.filter_by(area_id=area_vo.area_id).first()
        return area_list

    def update_area(self,area_vo):
        db.session.merge(area_vo)
        db.session.commit()