from app.plugins import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(128), nullable=False)
    secret = db.Column(db.String(1024), nullable=False)
    salt = db.Column(db.String(32), nullable=False)
    display_name = db.Column(db.String(128))
    account_type = db.Column(db.Integer, nullable=False)

    