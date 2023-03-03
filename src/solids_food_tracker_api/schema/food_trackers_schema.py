from main import ma 


class FoodTrackerSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["id", "liked_food", "allergic_reaction", "date_eaten"]
        # load_only = ["food_id", "child_id"]

        # parent = ma.Nested("ParentSchema")


food_tracker_schema = FoodTrackerSchema()
food_trackers_schema = FoodTrackerSchema(many=True)
