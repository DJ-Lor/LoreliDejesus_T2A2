from flask import Blueprint, request, abort, jsonify
from main import db
from model.child import Child
from model.food_tracker import FoodTracker
from model.parent import Parent
from model.food import Food
from schema.children_schema import child_schema, children_schema
from schema.food_trackers_schema import food_tracker_schema, food_trackers_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


child = Blueprint('child', __name__, url_prefix="/children")

#child 

@child.get("/")
# #Decorator to make sure the jwt is included in the request
@jwt_required()
def get_children():

    #get the user id invoking get_jwt_identity
    parent_id = get_jwt_identity()

    #query children that belong to the authenticated parent
    children = Child.query.filter_by(parent_id=parent_id).all()

    if not children:
        return { "message": "There are no child/children under this parent" }
    
    #return the children of the authenticated parent
    return children_schema.dump(children)


@child.get("/<int:id>")
# #Decorator to make sure the jwt is included in the request
@jwt_required()
def get_child(id):

    #get the user id invoking get_jwt_identity
    parent_id = get_jwt_identity()

    child = Child.query.get(id)

    if not child:
            return  { "message": "ID cannot be found. Please try again" }
    
    if child.parent_id != parent_id:
        return abort(401, description= "Parent does not have access to this child")

    return child_schema.dump(child)


@child.post("/")
# #Decorator to make sure the jwt is included in the request
@jwt_required()
def create_child():

    #get the user id invoking get_jwt_identity
    parent_id = get_jwt_identity()

    child_fields = child_schema.load(request.json)

    child = Child(**child_fields)

    #parent_id taken from the token
    child.parent_id = parent_id

    db.session.add(child)
    db.session.commit()

    return child_schema.dump(child)


@child.put("/<int:id>")
#Decorator to make sure the jwt is included in the request
@jwt_required()
def update_child(id):

    #get the user id invoking get_jwt_identity
    parent_id = get_jwt_identity()

    child_fields = child_schema.load(request.json)

    child = Child.query.get(id)

    if not child:
        return abort(400, description= "Child does not exist")
    
    if child.parent_id != parent_id:
        return abort(401, description= "Parent does not have access to this child")

    child.child_name = child_fields["child_name"]
    child.child_dob = child_fields["child_dob"]

    db.session.commit()
    
    return {"Updated details": child_schema.dump(child)}


@child.delete("/<int:id>")
#Decorator to make sure the jwt is included in the request
@jwt_required()
def delete_child(id):
    # delete child --> request send the child id in the url
    # as the route is authenticated I have the parent id in the JWT token
    # to confirm if the child is accessible by the parent, i simply find the child and check if the parentid is the same

    #get the user id invoking get_jwt_identity
    parent_id = get_jwt_identity()

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
#Decorator to make sure the jwt is included in the request
@jwt_required()
def get_food_trackers(id):

    #get the user id invoking get_jwt_identity
    parent_id = get_jwt_identity()

    #find the child to associate the food tracker to
    child = Child.query.get(id)

    #return an error if the child doesn't exist
    if not child:
        return abort(400, description= "Child does not exist")
    
    #return an error message if the parent id does not have authorisation to child 
    if child.parent_id != parent_id:
        return abort(401, description= "Parent does not have access to this child")

    food_trackers = FoodTracker.query.filter_by(child_id=id)
    return food_trackers_schema.dump(food_trackers)


@child.post("/<int:id>/food_trackers")
#Decorator to make sure the jwt is included in the request
@jwt_required()
def create_food_trackers(id):

    #get the user id invoking get_jwt_identity
    parent_id = get_jwt_identity()

    #create a new food_tracker
    food_tracker_fields = food_tracker_schema.load(request.json)
    
    #find the child to associate the food tracker to
    child = Child.query.get(id)

    #find the food to associate the food tracker to
    food = Food.query.get(food_tracker_fields["food_id"])

    #return error if food_id is not valid
    if not food:
        return abort(400, description= "Food_id does not exist")
    
    #return an error if the child doesn't exist
    if not child:
        return abort(400, description= "Child does not exist")
    
    #return an error message if the parent id does not have authorisation to child 
    if child.parent_id != parent_id:
        return abort(401, description= "Parent does not have access to this child")

    #create the food tracker with the given values
    new_food_tracker = FoodTracker(**food_tracker_fields)
    new_food_tracker.child_id = id

    #add to the database and commit
    db.session.add(new_food_tracker)
    db.session.commit()

    #return the new food tracker in the response
    return jsonify(food_tracker_schema.dump(new_food_tracker))


@child.delete("/<int:child_id>/food_trackers/<int:food_tracker_id>")
#Decorator to make sure the jwt is included in the request
@jwt_required()
def delete_food_trackers(child_id, food_tracker_id):

    #get the user id invoking get_jwt_identity
    parent_id = get_jwt_identity()

    #find the child to associate the food tracker to
    child = Child.query.get_or_404(child_id)

    #find the food tracker records
    food_tracker = FoodTracker.query.get_or_404(food_tracker_id)

    
    #return an error message if the parent id does not have authorisation to child 
    if child.parent_id != parent_id:
        return abort(401, description= "No deletion. Parent does not have access to this child")

    #delete from database and commit
    db.session.delete(food_tracker)
    db.session.commit()

    #return the child in the response
    return {"message": "Food tracker deleted!"}



