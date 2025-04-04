from base import db

class UserRegisterVO(db.Model):
    __tablename__ = 'user_register'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)


    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'password': self.password
        }

    db.create_all()