from main import ma 


class ChildSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "dob", "parent", "parent_id")
        load_only = ["parent_id"]

        parent = ma.Nested("ParentSchema")


child_schema = ChildSchema()
children_schema = ChildSchema(many=True)