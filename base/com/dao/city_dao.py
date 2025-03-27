from base import db
from base.com.vo import city_vo

from base.com.vo.city_vo import CityVO

class CityDAO:

    def insert_city(self, city_vo):
        db.session.add(city_vo)
        db.session.commit()

    def view_city(self):
        city_list = CityVO.query.all()
        return city_list

    def delete_city(self, city_vo):
        city = CityVO.query.get(city_vo.city_id)
        db.session.delete(city)
        db.session.commit()

    def edit_city(self, city_vo):
        city_list = CityVO.query.filter_by(city_id=city_vo.city_id)
        return city_list

    def update_city(self, city_vo):
        db.session.merge(city_vo)
        db.session.commit()