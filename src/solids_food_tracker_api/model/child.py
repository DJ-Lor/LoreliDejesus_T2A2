from main import db

class Child(db.Model):
    __tablename__ = "children"

    id = db.Column(db.Integer(), primary_key=True)

    child_name = db.Column(db.String(50), nullable=False)

    child_dob = db.Column(db.Date(), nullable=False)

    parent_id = db.Column(
        db.Integer(), db.ForeignKey("parents.id"), nullable=False
    )

