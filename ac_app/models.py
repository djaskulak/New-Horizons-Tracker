from ac_app.extensions import db
from sqlalchemy_utils import URLType
from ac_app.utils import FormEnum
from flask_login import UserMixin

class AnimalPersonality(FormEnum):
  JOCK = 'Jock'
  CRANKY = 'Cranky'
  PEPPY = 'Peppy'
  SISTERLY = 'Sisterly'
  LAZY = 'Lazy'
  NORMAL = 'Normal'
  SNOOTY = 'Snooty'
  OTHER = 'Other'

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(80), nullable=False, unique=True)
  password = db.Column(db.String(80), nullable=False)
  name = db.Column(db.String(80), nullable=False)
  island = db.Column(db.String(80), nullable=False)
  items = db.relationship('Item', back_populates='user')
  animals = db.relationship('Animal', back_populates='user')

class Animal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  personality = db.Column(db.Enum(AnimalPersonality), default=AnimalPersonality.OTHER)
  name = db.Column(db.String(80), nullable=False)
  photo = db.Column(URLType)
  user = db.relationship('User', back_populates='animals')

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  name = db.Column(db.String(80), nullable=False)
  photo = db.Column(URLType)
  price = db.Column(db.Integer, nullable=False)
  user = db.relationship('User', back_populates='items')
