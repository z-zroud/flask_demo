from marshmallow import Schema, fields, post_load
from app.models.user import User
from app.utils.security import gen_salt, encrypt_password

class UserReq(Schema):
    account = fields.String(data_key='account')
    password = fields.String(data_key='password')
    display_name = fields.String(data_key='display_name')
    account_type = fields.Int(data_key='account_type')

    @post_load
    def create_user(self, data, **kwargs):
        new_user = User()
        new_user.salt = gen_salt()
        new_user.secret = encrypt_password(data['password'], new_user.salt)
        new_user.account = data['account']
        new_user.display_name = data['display_name']
        new_user.account_type = data['account_type']

        return new_user

