
from flask_restplus import Namespace, fields


class UserDto:
  api = Namespace('user', description='user related ops')
  user = api.model('user', {
    'email': fields.String(required=True, description='email address'),
    'username': fields.String(required=True, descrition='username'),
    'first_name': fields.String(required=False, description='users first name (optional)'),
    'last_name': fields.String(required=False, description='users last name (optional)'),
    'phone_number': fields.Integer(required=False, description='users phone number (optional)'),
    'display_contact_info': fields.String(required=False, description='should users pii be displayed'),
    'bio': fields.String(required=False, description='users biography'),
    'password': fields.String(required=True, description='users desired password'),
    'confirm_password': fields.String(required=True, description='password confirmation')
  })
