from os import name
from flask import request
from app.api import api_bp
from app.plugins import db
from app.schema.user import UserReq
from app.models.user import User
from app.schema.response import Response

@api_bp.route('/users', methods=['POST'])
def register_user():
    
    data = request.get_json()
    schema = UserReq()
    new_user = schema.load(data)

    user = User.query.filter_by(account=new_user.account).first()
    if user is None:
        db.session.add(new_user)
        db.session.commit()

    return Response().json()