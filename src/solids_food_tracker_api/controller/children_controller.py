from flask import Blueprint, request
from main import db
from model.child import Child
from schema.children_schema import child_schema, children_schema


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