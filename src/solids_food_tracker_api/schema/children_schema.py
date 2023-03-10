from main import ma 
from marshmallow import fields

class ChildSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["id", "child_name", "child_dob", "parent", "parent_id", "food_tracker"]
        load_only = ["parent_id"]

    parent = fields.Nested("ParentSchema", only=("first_name", "email"))
    food_tracker = fields.Nested("FoodTrackerSchema", only=("food_id", "date_eaten"))

child_schema = ChildSchema()
children_schema = ChildSchema(many=True)