
import re

from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service import user_service

api = UserDto.api
_user = UserDto.user
_user_create = UserDto.user_create


@api.route('/')
class UserList(Resource):
  @api.doc('list all users')
  @api.marshal_list_with(_user, envelope='data')
  def get(self):
    return user_service.get_all_users()
  
  @api.response(201, 'created')
  @api.doc('create new user')
  @api.expect(_user_create, validate=True)
  def post(self):
    data = request.json

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

    if not user_service.save_new_user(data=data):
      return {
        'status': 'failed to create user'
      }, 400
    return {
      'status': 'created new user successfully'
    }, 201


@api.route('/<public_id>')
@api.param('public_id', 'the user public id')
@api.response(404, 'User not found')
class User(Resource):
  @api.doc('get a user')
  @api.marshal_with(_user)
  def get(self, public_id):
    user = user_service.get_user_by_public_id(public_id)
    if not user:
      api.abort(404)
    else:
      return user


def _check_password_requirements(password):
  pattern = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
  match = re.search(pattern, password)
  
  if match:
    return True
