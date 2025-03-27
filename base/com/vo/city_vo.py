from base import db

class CityVO(db.Model):
    __tablename__ = "city_table"
    city_id = db.Column('city_id',db.Integer,primary_key=True,autoincrement=True)
    city_name = db.Column('city_name',db.String(255),nullable=False)

    def as_dict(self):
        return {
            'city_id':self.city_id,
            'city_name':self.city_name,
        }
db.create_all()