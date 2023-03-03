from flask import Blueprint, request
from main import db
from model.food_tracker import FoodTracker
from schema.food_trackers_schema import food_tracker_schema, food_trackers_schema


food_tracker = Blueprint('food_tracker', __name__, url_prefix="/food_trackers")


@food_tracker.get("/")
def get_food_trackers():
    food_trackers = FoodTracker.query.all()
    return food_trackers_schema.dump(food_trackers)


@food_tracker.post("/")
def create_food_tracker():

    try:
        food_tracker_fields = food_tracker_schema.load(request.json)

        food_tracker = FoodTracker(**food_tracker_fields)

        db.session.add(food_tracker)
        db.session.commit()

    except:
        return {"message": "The information provided is incorrect, no duplicates permitted"}

    return food_tracker_schema.dump(food_tracker)