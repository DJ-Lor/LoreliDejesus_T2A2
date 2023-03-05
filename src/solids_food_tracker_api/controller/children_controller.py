from flask import Blueprint, request
from main import db
from model.child import Child
from model.food_tracker import FoodTracker
from schema.children_schema import child_schema, children_schema
from schema.food_trackers_schema import food_tracker_schema, food_trackers_schema



child = Blueprint('child', __name__, url_prefix="/children")


@child.get("/")
def get_children():
    children = Child.query.all()
    return children_schema.dump(children)


@child.post("/")
def create_child():

    child_fields = child_schema.load(request.json)

    child = Child(**child_fields)

    db.session.add(child)
    db.session.commit()

    return child_schema.dump(child)


@child.get("/<int:id>/food_trackers")
def get_food_trackers(id):
    food_trackers = FoodTracker.query.all()
    return food_trackers_schema.dump(food_trackers)


@child.post("/<int:id>/food_trackers")
def create_food_trackers(id):
    #Create a new food_tracker
    food_tracker_fields = food_tracker_schema.load(request.json)

    food_tracker = FoodTracker(**food_tracker_fields)

    db.session.add(food_tracker)
    db.session.commit()

    return food_tracker_schema.dump(food_tracker)
