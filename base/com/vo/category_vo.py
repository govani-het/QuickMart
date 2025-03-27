from base import db

class CategoryVO(db.Model):
    __tablename__ = "category_table"
    category_id = db.Column('category_id',db.Integer,primary_key=True,autoincrement=True)
    category_name = db.Column('category_name',db.String(255),nullable=False)
    category_description = db.Column('category_description',db.Text,nullable=False)
    category_image_name = db.Column('category_image_name', db.String(255),
                                   nullable=False)
    category_image_path = db.Column('category_image_path', db.String(255),
                                   nullable=False)

    def as_dict(self):
        return {
            'category_id':self.category_id,
            'category_name':self.category_name,
            'category_description':self.category_description,
            'category_image_name':self.category_image_name,
            'category_image_path':self.category_image_path
        }
db.create_all()