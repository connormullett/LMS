
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
    return user_service.save_new_user(data=data)


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
