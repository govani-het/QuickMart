from base import db

class UserRegisterVO(db.Model):
    __tablename__ = 'user_register'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    login_role = db.Column('login_role', db.String(100), nullable=False, default='user')
    login_status = db.Column('login_status', db.Boolean, nullable=False, default=True)

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'login_role': self.login_role,
            'login_status': self.login_status
        }


    db.create_all()