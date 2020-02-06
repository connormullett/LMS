
import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
  user = User.query.filter_by(email=data['email']).first()

  if data.get('password') != data.get('confirm_password'):
      return {'status': 'password mismatch'}, 400
    
    if not _check_password_requirements(data.get('password')):
      return {
        'status': 'Password must be between 6 and 20 characters, ' \
        'contain atleast one uppercase and lowercase characters, ' \
        'a number, and must have at least one special symbol'
      }, 400
    
    if ' ' in data.get('username'):
      return {
        'status': 'fail',
        'message': 'Username cannot have spaces'
      }, 400

    public_contact_options = {
      'true': True,
      'false': False
    }

    try:
      data['display_contact_info'] = public_contact_options[data.get('display_contact_info').lower()]
    except AttributeError:
      data['display_contact_info'] = False

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


def _check_password_requirements(password):
  pattern = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
  match = re.search(pattern, password)
  
  if match:
    return True
