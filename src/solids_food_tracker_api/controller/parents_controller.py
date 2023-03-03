from flask import Blueprint, request
from main import db
from model.parent import Parent
from schema.parents_schema import parent_schema, parents_schema


parent = Blueprint('parent', __name__, url_prefix="/parents")


@parent.get("/")
def get_parents():
    parents = Parent.query.all()
    return parents_schema.dump(parents)


@parent.post("/")
def create_parent():

    try:
        parent_fields = parent_schema.load(request.json)

        parent = Parent(**parent_fields)

        db.session.add(parent)
        db.session.commit()

    except:
        return {"message": "The information provided is incorrect, please try again"}

    return parent_schema.dump(parent)