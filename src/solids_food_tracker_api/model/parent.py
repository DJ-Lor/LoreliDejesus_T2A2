from main import db, bcrypt

class Parent(db.Model):
    __tablename__ = "parents"

    id = db.Column(db.Integer(), primary_key=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50))

    email = db.Column(db.String(50), nullable=False, unique=True)

    password = db.Column(db.String(128), nullable=False)

    children = db.relationship('Child', backref='parent', cascade="all, delete", lazy=True)

    def __init__(self, first_name, last_name, email, password, children=None):
        self.first_name = first_name
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.last_name = last_name
        self.email = email
        self.children = children or []