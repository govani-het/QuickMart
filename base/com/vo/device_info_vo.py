from base import db
from base.com.vo.user_register_vo import UserRegisterVO


class DeviceInfoVO(db.Model):
    __tablename__ = 'device_info_table'
    device_id = db.Column('device_id', db.Integer, primary_key=True,
                          autoincrement=True)
    device_identity = db.Column('device_identity', db.String(250),
                                nullable=False)

    device_login_id = db.Column('device_login_id', db.Integer,
                                db.ForeignKey(UserRegisterVO.id,
                                              ondelete='CASCADE',
                                              onupdate='CASCADE'),
                                nullable=False)

    def as_dict(self):
        return {
            'device_id': self.device_id,
            'device_identity ': self.device_identity,
            'device_login_id': self.device_login_id,
        }


db.create_all()
