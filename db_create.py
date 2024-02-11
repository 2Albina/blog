
import flask
from app import db

app = flask.Flask(__name__, instance_relative_config=True)

with app.app_context():
    db.create_all()
    db.session.commit()