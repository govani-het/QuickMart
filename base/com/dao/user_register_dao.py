from base import db

from base.com.vo.user_register_vo import UserRegisterVO

class UserRegisterDAO:

    def insertUserData(self, userData_vo):
        db.session.add(userData_vo)
        db.session.commit()