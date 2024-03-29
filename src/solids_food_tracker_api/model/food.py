from main import db

class Food(db.Model):
    __tablename__ = "foods"

    id = db.Column(db.Integer(), primary_key=True)

    food_name = db.Column(db.String(50), nullable=False, unique=True)

    food_type = db.Column(db.String(50), nullable=False)

     # One-to-many relationship setup for food-to-foodtracker
    food_trackers = db.relationship('FoodTracker', backref='food', cascade="all, delete", lazy=True)

   