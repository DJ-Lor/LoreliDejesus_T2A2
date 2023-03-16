from main import ma 
from marshmallow import fields


class ParentSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["id", "first_name", "last_name", "email", "password", "children", "admin"]

        #attribute set so as not show when invoke dump to retrieve data
        # load_only = ["password"]

    children = ma.List(fields.Nested("ChildSchema", exclude=("parent_id", "parent")))


parent_schema = ParentSchema()
parents_schema = ParentSchema(many=True)