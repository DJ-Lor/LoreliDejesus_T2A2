from main import ma 


class ParentSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email", "password")


parent_schema = ParentSchema()
parents_schema = ParentSchema(many=True)