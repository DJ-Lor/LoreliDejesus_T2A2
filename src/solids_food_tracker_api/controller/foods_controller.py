from flask import Blueprint, request, abort, jsonify
from main import db
from model.food import Food
from schema.foods_schema import food_schema, foods_schema


food = Blueprint('food', __name__, url_prefix="/foods")


# Retrieve all food registered in database
@food.get("/")
def get_foods():
    foods = Food.query.all()
    return foods_schema.dump(foods)

# Create a new food post 
@food.post("/")
def create_food():

    food_fields = food_schema.load(request.json)

    food = Food(**food_fields)

    # Fields updated for the food table
    food.food_name = food_fields["food_name"]
    food.food_type = food_fields["food_type"]

    # Limit food_types from this list
    declared_food_types = ['protein', 'dairy', 'vegetable', 'fruits', 'grains', 'others']

    # Declare error if food_type not in list
    if food.food_type not in declared_food_types:
        return jsonify({"error": "Invalid input. Food type options are 'protein', 'dairy', 'vegetable', 'fruits', 'grains', 'others'"}), 400

    # Add and commit food entry
    db.session.add(food)
    db.session.commit()

    # Return the summary of the new food added
    return food_schema.dump(food)






