from app import db


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # spells = db.relationship('Spell', backref='list', lazy=True)


class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(64), index=True, unique=True)
    slevel = db.Column(db.Integer)
    verbal = db.Column(db.Boolean)
    somatic = db.Column(db.Boolean)
    material = db.Column(db.Boolean)
    concentration = db.Column(db.Boolean)
    ritual = db.Column(db.Boolean)
    description = db.Column(db.String(600))
