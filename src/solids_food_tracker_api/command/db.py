from main import db
from flask import Blueprint


db_cmd = Blueprint("db", __name__)


@db_cmd.cli.command('create')
def create_db():
    db.create_all()
    print('Tables successfully created!')


@db_cmd.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables successfull dropped!')