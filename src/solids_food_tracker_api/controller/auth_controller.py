from flask import Blueprint, request, jsonify, abort
from main import db, bcrypt, jwt
from model.parent import Parent
from schema.parents_schema import parent_schema
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth = Blueprint('auth', __name__, url_prefix="/auth")

#route for parent registration
@auth.post("/register")
def auth_register():
    
    #the request data will be loaded in a parent_schema converted to JSON
    parent_fields = parent_schema.load(request.json)

    #find the parent
    parent = Parent.query.filter_by(email=parent_fields["email"]).first()
    print(parent)

    if parent:
    # return an abort message to inform the user. That will end the request
        return abort(400, description="Email already registered")

    #create parent object
    parent = Parent(**parent_fields)

    #add it to the database and commit the changes
    db.session.add(parent)
    db.session.commit()

    #create a variable that sets an expiry date
    expiry = timedelta(days=1)

    #create the access token
    access_token = create_access_token(identity=str(parent.id), expires_delta=expiry)

    # return the parent email and the access token
    return jsonify(parent_schema.dump(parent))



#route for parent login
@auth.post("/login")
def auth_login():

    #the request data will be loaded in a parent_schema converted to JSON
    parent_fields = parent_schema.load(request.json)

    #find the parent
    parent = Parent.query.filter_by(email=parent_fields["email"]).first()

    #there is not a user with that email or if the password is no correct send an error
    if not parent or not bcrypt.check_password_hash(parent.password, parent_fields["password"]):
        return abort(401, description="Incorrect username or password")
    
    #create a variable that sets an expiry date
    expiry = timedelta(days=1)

    #create the access token
    access_token = create_access_token(identity=str(parent.id), expires_delta=expiry)

    # return the parent email and the access token
    return jsonify({"parent":parent.email, "token": access_token })
