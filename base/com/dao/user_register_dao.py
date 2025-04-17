from base import db
from sqlalchemy import and_
from base.com.vo.user_register_vo import UserRegisterVO

class UserRegisterDAO:

    def insert_user_data(self, userData_vo):
        db.session.add(userData_vo)
        db.session.commit()

    def getUserData(self, user_email, user_password):
        user_data =  db.session.query(UserRegisterVO).filter(
            and_(UserRegisterVO.email == user_email, UserRegisterVO.password == user_password)
        ).one_or_none()

        return user_data