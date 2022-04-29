from flask import request
from app.api import api_bp
from app.plugins import db
from app.schema.user import UserReq
from app.models.user import User
from app.schema.response import Response
from marshmallow import ValidationError

@api_bp.route('/users', methods=['POST'])
def register_user():
    
    data = request.get_json()
    schema = UserReq()

    try:
        new_user = schema.load(data)
    except ValidationError as err:
        return Response(status_code=400, msg=err.messages).json()

    user = User.query.filter_by(account=new_user.account).first()

    if user:
        return Response(status_code=400, msg=f"user {new_user.account} has already existed.").json()
    
    db.session.add(new_user)
    db.session.commit()

    return Response().json()


