from flask import Blueprint, request, jsonify, abort
from main import db, bcrypt
from model.parent import Parent
from schema.parents_schema import parent_schema, parents_schema
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask_jwt_extended import jwt_required, get_jwt_identity


auth = Blueprint('auth', __name__, url_prefix="/auth")

# route for parent registration
@auth.post("/register")
def auth_register():
    
    # the request data will be loaded in a parent_schema converted to JSON
    parent_fields = parent_schema.load(request.json)

    # find the parent through the unique email address
    parent = Parent.query.filter_by(email=parent_fields["email"]).first()

    if parent:
    # return an abort message to inform the user. That will end the request
        return abort(400, description="Email already registered")

    # create parent object
    parent = Parent(**parent_fields)

    # add it to the database and commit the changes
    db.session.add(parent)
    db.session.commit()

    # create a variable that sets an expiry date
    expiry = timedelta(days=1)

    # create the access token
    access_token = create_access_token(identity=parent.id, expires_delta=expiry)

    # return the parent email and the access token
    return jsonify({"parent":parent_schema.dump(parent), "token": access_token, "message": "parent successfully registered!"})
   


# route for parent login
@auth.post("/login")
def auth_login():

    # the request data will be loaded in a parent_schema converted to JSON
    parent_fields = parent_schema.load(request.json)

    # find the parent through the unique email address
    parent = Parent.query.filter_by(email=parent_fields["email"]).first()

    # if there is not a user with that email or if the password is not correct, send an error
    if not parent or not bcrypt.check_password_hash(parent.password, parent_fields["password"]):
        return abort(401, description="Incorrect username or password")
    
    # create a variable that sets an expiry date
    expiry = timedelta(days=1)

    # create the access token
    access_token = create_access_token(identity=parent.id, expires_delta=expiry)

    # return the parent email and the access token
    return jsonify({"parent":parent.email, "token": access_token })


@auth.get("/parents")
# decorator to make sure the jwt is included in the request
@jwt_required()
def auth_get_parents():

    # get the user ID invoking get_jwt_identity
    parent_id = get_jwt_identity()

    # retrieve the parent from the database based on their ID
    parent = Parent.query.filter_by(id=parent_id).first()

    # check that parent authorisation is admin
    if parent.admin == False:
        return {"message": "no admin rights"}

    # return all parents as JSON data
    parents = Parent.query.all()

    return parents_schema.dump(parents)