from main import db


class Fish(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    origin = db.Column(db.String(20))
    age_in_month = db.Column(db.Integer)
    weight_in_grams = db.Column(db.Integer)
    # self.name = name
    # self.origin = origin
    # self.age_in_months = age_in_months
    # self.weight = weight
