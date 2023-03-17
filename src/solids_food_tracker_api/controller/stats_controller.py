from flask import Blueprint, jsonify
from main import db
from model.food_tracker import FoodTracker
from model.food import Food
from sqlalchemy import func, Integer, desc
from sqlalchemy.sql.expression import case


stats = Blueprint('stats', __name__, url_prefix="/stats")

# Most liked food stats 
@stats.get("/most_liked")
def get_most_liked_food():

    # Count the number of True values for each food_id, group together and order the most liked
    food_counts = (
        db.session.query(
            Food.food_name, 
            func.sum(func.cast(FoodTracker.liked_food, Integer)).label("num_liked") # Func.sum only counts the value True and turns to integer 1
            )
            .join(FoodTracker, FoodTracker.food_id == Food.id)
            .group_by(Food.id)
            .order_by(desc("num_liked"))
            .all()
)
    # Return the results
    output = []
    for food_name, num_liked in food_counts:
        output.append({"food_name": food_name, "liked_food_child_count": num_liked})
    
    return jsonify(output)


# Most disliked food stats 
@stats.get("/most_disliked")
def get_most_disliked_food():

    # Count the number of False values for each food_id, group together and order the most disliked
    food_counts = (
        db.session.query(
            Food.food_name, 
            func.sum(
            case((FoodTracker.liked_food == False, 1), else_= 0)) # Count False values as 1 and True values as 0
            .label("num_disliked")
            )
            .join(FoodTracker, FoodTracker.food_id == Food.id)
            .group_by(Food.id)
            .order_by(desc("num_disliked"))
            .all()
)

    # Return the results
    output = []
    for food_name, num_disliked in food_counts:
        output.append({"food_name": food_name, "disliked_food_child_count": num_disliked})
    
    return jsonify(output)


# Most allergenic food based on the database statistics
@stats.get("/most_allergic")
def get_most_allergic_food():

    # Count the number of True values for each food_id, group together and order the most allergenic
    food_counts = (
        db.session.query(
            Food.food_name,
            func.sum(func.cast(FoodTracker.allergic_reaction, Integer)).label("num_allergic") # Func.sum only counts the value True and turns to integer 1
        )
        .join(FoodTracker, FoodTracker.food_id == Food.id)
        .group_by(Food.id)
        .order_by(desc("num_allergic"))
        .all())

    # Return the results
    output = []
    for food_name, num_allergic in food_counts:
        output.append({"food_name": food_name, "allergic_child_count": num_allergic})
    
    return jsonify(output)

   
    


