from flask import Blueprint, request, abort, jsonify
from main import db
from model.child import Child
from model.food_tracker import FoodTracker
from model.parent import Parent
from schema.children_schema import child_schema, children_schema
from schema.food_trackers_schema import food_tracker_schema, food_trackers_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


child = Blueprint('child', __name__, url_prefix="/children")

#child 

@child.get("/")
def get_children():
    children = Child.query.all()
    return children_schema.dump(children)


@child.get("/<int:id>")
def get_child(id):
    child = Child.query.get(id)

    if not child:
            return  { "message": "ID cannot be found. Please try again" }

    return child_schema.dump(child)


@child.post("/")
def create_child():

    child_fields = child_schema.load(request.json)

    child = Child(**child_fields)

    db.session.add(child)
    db.session.commit()

    return child_schema.dump(child)


@child.put("/<int:id>")
def update_child(id):

    child_fields = child_schema.load(request.json)

    child = Child.query.get(id)

    if not child:
        return abort(400, description= "Child does not exist")
    
    child.child_name = child_fields["child_name"]
    child.child_dob = child_fields["child_dob"]

    db.session.commit()
    
    return child_schema.dump(child)


@child.delete("/<int:id>")
#Decorator to make sure the jwt is included in the request
@jwt_required()
def delete_child(id):
    # delete child --> request send the child id in the url
    # as the route is authenticated I have the parent id in the JWT token
    # to confirm if the child is accessible by the parent, i simply find the child and check if the parentid is the same

    #get the user id invoking get_jwt_identity
    parent_id = int(get_jwt_identity())

    #find the child
    child = Child.query.get(id)

    if not child:
        return abort(400, description= "No deletion. Child does not exist")
    
    if child.parent_id != parent_id:
        return abort(401, description= "No deletion. Parent does not have access to this child")

    
    db.session.delete(child)
    db.session.commit()
    
    return {"message": "Child deleted!"}


#food tracker

@child.get("/<int:id>/food_trackers")
def get_food_trackers(id):
    #find the child to associate the food tracker to
    child = Child.query.get(id)

    #return an error if the child doesn't exist
    if not child:
        return abort(400, description= "Child does not exist")

    food_trackers = FoodTracker.query.filter_by(child_id=id)
    return food_trackers_schema.dump(food_trackers)


@child.post("/<int:id>/food_trackers")
def create_food_trackers(id):
    #create a new food_tracker
    food_tracker_fields = food_tracker_schema.load(request.json)
    
    #find the child to associate the food tracker to
    child = Child.query.get(id)

    #return an error if the child doesn't exist
    if not child:
        return abort(400, description= "Child does not exist")
    
    #create the food tracker with the given values
    new_food_tracker = FoodTracker(**food_tracker_fields)
    new_food_tracker.child_id = id

    #add to the database and commit
    db.session.add(new_food_tracker)
    db.session.commit()

    #return the child in the response
    return jsonify(food_tracker_schema.dump(new_food_tracker))
