from main import db
from flask import Blueprint

# Utilise the Blueprint function from Flask
db_cmd = Blueprint("db", __name__)

# Command to create the tables 
@db_cmd.cli.command('create')
def create_db():
    db.create_all()
    print('Tables successfully created!')


# Command to drop the tables 
@db_cmd.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables successfull dropped!')