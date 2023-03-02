from main import db

class Child(db.Model):
    __tablename__: "children"

    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(), nullable=False)

    dob = db.Column(db.Date(), nullable=False)

    parent_id = db.Column(
        db.Integer(), db.ForeignKey("parents.id"), nullable=False
    )

