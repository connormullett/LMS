
import datetime, decimal
import json
import jwt
import re

from app.main.model.blacklist import BlacklistToken

from .. import db, flask_bcrypt
from ..config import key

class User(db.Model):

  __tablename__ = 'user'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String(255), unique=True, nullable=False)
  registered_on = db.Column(db.DateTime, nullable=False)
  modified_on = db.Column(db.DateTime, nullable=True)
  admin = db.Column(db.Boolean, nullable=False, default=False)
  public_id = db.Column(db.String(100), unique=True)
  username = db.Column(db.String(50), unique=True)
  first_name = db.Column(db.String(30), nullable=True)
  last_name = db.Column(db.String(30), nullable=True)
  password_hash = db.Column(db.String(100))
  bio = db.Column(db.String(200), nullable=True)
  country_code = db.Column(db.String(2), nullable=True)
  area_code = db.Column(db.String(3), nullable=True)
  phone_number = db.Column(db.String(7), nullable=True)
  display_contact_info = db.Column(db.Boolean, nullable=False, default=False)
  last_login = db.Column(db.DateTime, nullable=True)

  @property
  def password(self):
    raise AttributeError('password: write-only field')

  @password.setter
  def password(self, password):
    self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
  
  def check_password(self, password):
    return flask_bcrypt.check_password_hash(self.password_hash, password)

  def set_login(self):
    self.last_login = datetime.datetime.utcnow()
    db.session.commit()
  
  def __repr__(self):
    return "<User '{}'>".format(self.username)
  
  @staticmethod
  def encode_auth_token(user_id):
    try:
      payload = {
        # expires, issued at, subscriber
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
      }
      return jwt.encode(
        payload, key, algorithm='HS256'
      )
    except Exception as e:
      return e
  
  @staticmethod
  def decode_auth_token(token):
    try:
      payload = jwt.decode(token, key)
      is_blacklisted_token = BlacklistToken.check_blacklist(token)
      if is_blacklisted_token:
        return 'token blacklisted, login'
      else:
        return payload['sub']
    except jwt.ExpiredSignatureError:
      return 'signature expired'
    except jwt.InvalidTokenError:
      return 'invalid token'
  
  @staticmethod
  def validate_user(data):

    out = None

    user = User.query.filter_by(email=data.get('email')).first()

    if user or User.query.filter_by(username=data.get('username')).first():
      out = 'user already exists'

    if data.get('password') != data.get('confirm_password'):
        out = 'password mismatch'

    if not _check_password_requirements(data.get('password')):
      out = 'Password must be between 6 and 20 characters, ' \
        'contain atleast one uppercase and lowercase characters, ' \
        'a number, and must have at least one special symbol'

    if ' ' in data.get('username'):
      out = 'Username cannot have spaces'
    
    return isinstance(out, str), out
  

def _check_password_requirements(password):
  pattern = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
  match = re.search(pattern, password)

  if match:
    return True
