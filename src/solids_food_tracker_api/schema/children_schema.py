from main import ma 
from marshmallow import fields

class ChildSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["id", "child_name", "child_dob", "parent", "parent_id", "food_tracker"]
        
        # Attribute set so as not show when invoke dump to retrieve data
        load_only = ["parent_id"] 

    # Nested values to provide certain parent attributes on child_schema
    parent = fields.Nested("ParentSchema", only=("first_name", "email"))

    # Nested values to provide certain food_tracker attributes on child_schema
    food_tracker = fields.Nested("FoodTrackerSchema", only=("food_id", "date_eaten"))

child_schema = ChildSchema()
children_schema = ChildSchema(many=True)