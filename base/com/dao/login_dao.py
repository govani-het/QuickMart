from base import db
from base.com.vo.user_register_vo import UserRegisterVO


class LoginDAO:

    def check_login_username(self, login_vo):
        login_vo_list = UserRegisterVO.query.filter_by(
            email=login_vo.email).first()
        return login_vo_list
