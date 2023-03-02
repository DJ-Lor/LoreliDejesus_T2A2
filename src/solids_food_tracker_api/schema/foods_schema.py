from main import ma 


class FoodSchema(ma.Schema):
    class Meta:
        fields = ("id", "food_name", "food_type")


food_schema = FoodSchema()
foods_schema = FoodSchema(many=True)
