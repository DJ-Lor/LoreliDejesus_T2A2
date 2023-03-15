from flask import Blueprint, jsonify
from main import db
from model.food_tracker import FoodTracker
from model.food import Food
from sqlalchemy import func, Integer, desc


stats = Blueprint('stats', __name__, url_prefix="/stats")


@stats.get("/most_liked")
def get_most_liked_food():

    #count the number of True values for each food_id
    food_counts = (
        db.session.query(
            Food.food_name, 
            func.sum(func.cast(FoodTracker.liked_food, Integer)).label("num_liked")
            )
            .join(FoodTracker, FoodTracker.food_id == Food.id)
            .group_by(Food.id)
            .order_by(desc("num_liked"))
            .all()
)
    #return the results
    output = []
    for food_name, num_liked in food_counts:
        output.append({"food_name": food_name, "liked_food": num_liked})
    
    return jsonify(output)


@stats.get("/most_allergic")
def get_most_allergic_food():

    #count the number of True values for each food_id
    food_counts = (
        db.session.query(
            Food.food_name,
            func.sum(func.cast(FoodTracker.allergic_reaction, Integer)).label("num_allergic")
        )
        .join(FoodTracker, FoodTracker.food_id == Food.id)
        .group_by(Food.id)
        .order_by(desc("num_allergic"))
        .all()
)

    #return the results
    output = []
    for food_name, num_allergic in food_counts:
        output.append({"food_name": food_name, "allergic_child_count": num_allergic})
    
    return jsonify(output)

   
    


