from main import db

class Child(db.Model):
    __tablename__ = "children"

    id = db.Column(db.Integer(), primary_key=True)

    child_name = db.Column(db.String(50), nullable=False, unique=True)

    child_dob = db.Column(db.Date(), nullable=False)

    # Foreign key associated with parent-child (one-to-many)
    parent_id = db.Column(
        db.Integer(), db.ForeignKey("parents.id"), nullable=False
    )

    # One-to-many relationship setup for child-foodtracker
    food_trackers = db.relationship('FoodTracker', backref='child', cascade="all, delete", lazy=True)
