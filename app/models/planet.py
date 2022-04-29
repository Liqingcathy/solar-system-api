from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_from_sun = db.Column(db.Integer)
    name = db.Column(db.String)
    desc = db.Column(db.String)
    size = db.Column(db.Integer)
    