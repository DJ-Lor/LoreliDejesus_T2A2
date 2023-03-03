from main import db

class Food(db.Model):
    __tablename__ = "foods"

    id = db.Column(db.Integer(), primary_key=True)

    food_name = db.Column(db.String(50), nullable=False)

    food_type = db.Column(db.String(50), nullable=False)

    