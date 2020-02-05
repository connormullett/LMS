
import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
  user = User.query.filter_by(email=data['email']).first()
  if not user:
    new_user = User(
      public_id=str(uuid.uuid4()),
      email=data['email'],
      username=data['username'],
      password=data['password'],
      registered_on=datetime.datetime.utcnow(),
      first_name=data['first_name'],
      last_name=data['last_name'],
      bio=data['bio'],
      phone_number=data['phone_number'],
      display_contact_info=data['display_contact_info'],
    )
    save_changes(new_user)
    return True
  return False


def get_all_users():
  return User.query.all()


def get_user_by_public_id(public_id):
  return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
  db.session.add(data)
  db.session.commit()
