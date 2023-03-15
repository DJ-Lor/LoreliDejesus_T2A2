from flask import Blueprint, request, abort, jsonify
from main import db
from model.food import Food
from schema.foods_schema import food_schema, foods_schema


food = Blueprint('food', __name__, url_prefix="/foods")


@food.get("/")
def get_foods():
    foods = Food.query.all()
    return foods_schema.dump(foods)


@food.post("/")
def create_food():

    food_fields = food_schema.load(request.json)

    food = Food(**food_fields)

    food.food_name = food_fields["food_name"]
    food.food_type = food_fields["food_type"]

    declared_food_types = ['protein', 'dairy', 'vegetable', 'fruits', 'grains', 'others']

    if food.food_type not in declared_food_types:
        return jsonify({"error": "Invalid input. Food type options are 'protein', 'dairy', 'vegetable', 'fruits', 'grains', 'others'"}), 400

    db.session.add(food)
    db.session.commit()

        
    return food_schema.dump(food)




@food.delete("/<int:id>")
def update_food(id):

    food_fields = food_schema.load(request.json)

    food = Food.query.get(id)

    if not food:
        return abort(400, description= "Item does not exist")
    
    food.food_name = food_fields["food_name"]
    food.food_type = food_fields["food_type"]

    db.session.commit()
    
    return food_schema.dump(food)





