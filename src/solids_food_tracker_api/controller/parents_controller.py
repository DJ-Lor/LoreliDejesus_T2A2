from flask import Blueprint
from model.parent import Parent
from schema.parents_schema import parent_schema, parents_schema


parent = Blueprint('parent', __name__, url_prefix="/parents")


@parent.get("/")
def get_parents():
    parents = Parent.query.all()
    return parent_schema.dump(parents)