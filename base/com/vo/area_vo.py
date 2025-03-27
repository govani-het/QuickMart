from base import db
from base.com.vo.city_vo import CityVO


class AreaVO(db.Model):
    __tablename__ = "area_table"
    area_id = db.Column('area_id',db.Integer,primary_key=True,autoincrement=True)
    area_name = db.Column('area_name',db.String(255),nullable=False)
    area_city_id = db.Column('area_city_id',db.Integer,db.ForeignKey(CityVO.city_id,ondelete='CASCADE',onupdate='CASCADE'),nullable=False)
    def as_dict(self):
        return {
            'area_id':self.area_id,
            'area_name':self.area_name,
            'area_city_id':self.area_city_id
        }
db.create_all()