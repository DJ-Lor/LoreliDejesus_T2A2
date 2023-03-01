from main import db

class Parent(db.Model):
    __tablename__: "parents"

    id = db.Column(db.Integer(), primary_key=True)

    first_name = db.Column(db.String(), nullable=False)

    last_name = db.Column(db.String())

    email = db.Column(db.String(), nullable=False, unique=True)

    password = db.Column(db.String(), nullable=False)