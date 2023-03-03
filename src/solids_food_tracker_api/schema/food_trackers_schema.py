from main import ma 


class FoodTrackerSchema(ma.Schema):
    class Meta:
        fields = ("id", "liked_food", "allergic_reaction", "date_eaten")
        # load_only = ["food_id", "child_id"]

        # parent = ma.Nested("ParentSchema")


food_tracker_schema = FoodTrackerSchema()
foods_tracker_schema = FoodTrackerSchema(many=True)
