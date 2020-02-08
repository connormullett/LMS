
import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
  
  status, message = User.validate_user(data)

  if status:
    return {
      'status': 'fail',
      'message': message
    }

  try:
    data['display_contact_info'] = _public_contact_options[data.get('display_contact_info').lower()]
  except AttributeError:
    data['display_contact_info'] = False

  new_user = User(
    public_id=str(uuid.uuid4()),
    email=data['email'],
    username=data['username'],
    password=data['password'],
    registered_on=datetime.datetime.utcnow(),
    first_name=data['first_name'],
    last_name=data['last_name'],
    bio=data['bio'],
    # phonenumber=data['phone_number'],
  )
  _save_changes(new_user)
  return generate_token(new_user)


def get_all_users():
  return User.query.all()


def get_user_by_public_id(public_id):
  return User.query.filter_by(public_id=public_id).first()


def _save_changes(data):
  db.session.add(data)
  db.session.commit()


def generate_token(user):
  try:
    auth_token = user.encode_auth_token(user.id)
    return {
      'status': 'success',
      'Authorization': auth_token.decode()
    }, 201
  except Exception as e:
    return {
      'status': 'fail',
      'message': 'ERROR: {}'.format(e)
    }, 401


_public_contact_options = {
  'true': True,
  'false': False
}
