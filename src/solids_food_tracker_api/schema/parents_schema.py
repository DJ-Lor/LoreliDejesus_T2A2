from main import ma 
from marshmallow import fields


class ParentSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["id", "first_name", "last_name", "email", "password", "children", "admin"]

    # Show chil/children fields when loading parent schema, with exclusion
    children = ma.List(fields.Nested("ChildSchema", exclude=("parent_id", "parent")))


parent_schema = ParentSchema()
parents_schema = ParentSchema(many=True)