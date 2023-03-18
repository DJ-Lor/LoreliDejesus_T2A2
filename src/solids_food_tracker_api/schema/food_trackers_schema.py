from main import ma 
from marshmallow import fields

class FoodTrackerSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["id", "child_name", "liked_food", "allergic_reaction", "date_eaten", "food_id", "child_id"]
       

    # Nested values to provide certain child attributes on foodtracker_schema
    child_name = fields.Nested("ChildSchema", only=("child_name",))


food_tracker_schema = FoodTrackerSchema()
food_trackers_schema = FoodTrackerSchema(many=True)
