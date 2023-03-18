from main import db

class FoodTracker(db.Model):
    __tablename__ = "food_trackers"

    id = db.Column(db.Integer(), primary_key=True)

    liked_food = db.Column(db.Boolean(), nullable=False)

    allergic_reaction = db.Column(db.Boolean(), nullable=False)

    date_eaten = db.Column(db.Date(), nullable=False)

    # Foreign key associated food_id
    food_id = db.Column(
        db.Integer(), db.ForeignKey("foods.id"), nullable=False
    )
    # Foreign key associated child_id
    child_id = db.Column(
        db.Integer(), db.ForeignKey("children.id"), nullable=False
    )
    