
from flask_restplus import Namespace, fields


class UserDto:
  api = Namespace('user', description='user related ops')
  user = api.model('user', {
    'email': fields.String(required=True, description='email address'),
    'username': fields.String(required=True, descrition='username'),
    'public_id': fields.String(description='user ID')
  })
