
from flask_restplus import Namespace, fields


class UserDto:
  api = Namespace('user', description='user related ops')
  user = api.model('user', {
    'email': fields.String(required=True, description='email address'),
    'username': fields.String(required=True, descrition='username'),
    'first_name': fields.String(required=False, description='users first name (optional)'),
    'last_name': fields.String(required=False, description='users last name (optional)'),
    'phone_number': fields.String(required=False, description='users phone number (optional)'),
    'display_contact_info': fields.Boolean(required=False, description='should users pii be displayed'),
    'bio': fields.String(required=False, description='users biography'),
    'password': fields.String(required=True, description='users desired password'),
    'confirm_password': fields.String(required=True, description='password confirmation'),
    'registered_on': fields.DateTime(required=False, description='when the user joined'),
    'last_login': fields.DateTime(required=False, description='when the user last logged in')
  })

  user_create = api.model('user_create', {
    'email': fields.String(required=True, description='email address'),
    'username': fields.String(required=True, descrition='username'),
    'first_name': fields.String(required=False, description='users first name (optional)'),
    'last_name': fields.String(required=False, description='users last name (optional)'),
    'phone_number': fields.String(required=False, description='users phone number (optional)'),
    'display_contact_info': fields.Boolean(required=False, description='should users pii be displayed'),
    'bio': fields.String(required=False, description='users biography'),
    'password': fields.String(required=True, description='users desired password'),
    'confirm_password': fields.String(required=True, description='password confirmation'),
  })


class AuthDto:
  api = Namespace('auth', description='authentication')
  user_auth = api.model('login', {
    'email': fields.String(required=True, description='email address'),
    'password': fields.String(required=True, description='password')
  })
