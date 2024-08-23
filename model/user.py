# models.py
from flask_mongoengine import Document
from flask_mongoengine.fields import StringField

class User(Document):
    username = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
