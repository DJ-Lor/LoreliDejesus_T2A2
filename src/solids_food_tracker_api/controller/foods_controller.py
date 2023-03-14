from flask import Blueprint, request, abort
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

    try:
        food_fields = food_schema.load(request.json)

        food = Food(**food_fields)

        db.session.add(food)
        db.session.commit()

    except:
        return {"message": "The information provided is incorrect, no duplicates permitted"}

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





