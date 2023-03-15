from flask import Blueprint
from main import db
from model.food_tracker import FoodTracker
from sqlalchemy import func, Integer


stats = Blueprint('stats', __name__, url_prefix="/stats")


@stats.get("/most_liked")
def get_most_liked_food():

    # Count the number of True values for each food_id
    food_counts = (
    db.session.query(FoodTracker.food_id, func.sum(func.cast(FoodTracker.liked_food, Integer)).label("num_liked"))
    .group_by(FoodTracker.food_id)
    .all()
)
 
    print(food_counts)

    # Print the results
    output = ""
    for food_id, num_liked in food_counts:
        output += f"Food ID {food_id}: {num_liked} likes \n"

    return output


@stats.get("/most_allergic")
def get_most_allergic_food():

    # Count the number of True values for each food_id
    food_counts = (
    db.session.query(FoodTracker.food_id, func.sum(func.cast(FoodTracker.allergic_reaction, Integer)).label("num_allergic"))
    .group_by(FoodTracker.food_id)
    .all()
)
 
    print(food_counts)

    # Print the results
    output = ""
    for food_id, num_allergic in food_counts:
        output += f"Food ID {food_id}: {num_allergic} allergic child \n"
        
    return output

   
    