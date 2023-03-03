from main import db

class Parent(db.Model):
    __tablename__ = "parents"

    id = db.Column(db.Integer(), primary_key=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50))

    email = db.Column(db.String(50), nullable=False, unique=True)

    password = db.Column(db.String(20), nullable=False)

    children = db.relationship('Child', backref='parent', cascade="all, delete", lazy=True)