from base import db
from base.com.vo.user_register_vo import UserRegisterVO


class LoginDAO:
    def insert_login(self, login_vo):
        db.session.add(login_vo)
        db.session.commit()

    def view_login(self):
        login_vo_list = UserRegisterVO.query.all()
        return login_vo_list

    def check_login_username(self, login_vo):
        login_vo_list = UserRegisterVO.query.filter_by(
            email=login_vo.email).first()
        return login_vo_list

    def update_login(self, login_vo):
        db.session.merge(login_vo)
        db.session.commit()

    def find_login_id(self, login_vo):
        login_vo_list = \
            UserRegisterVO.query.filter_by(
                login_username=login_vo.login_username).all()[
                -1].login_id
        print(28,login_vo_list)
        return login_vo_list

    def login_validate_username(self, login_vo):
        login_vo_list = UserRegisterVO.query.filter_by(
            login_username=login_vo.login_username).all()
        return login_vo_list

    def login_validate_password(self, login_vo):
        login_vo_list = UserRegisterVO.query.filter_by(
            login_password=login_vo.login_password).all()
        return login_vo_list
