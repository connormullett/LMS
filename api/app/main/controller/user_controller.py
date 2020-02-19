
import re

from flask import request
from flask_restplus import Resource, marshal

from ..util.dto import UserDto
from ..util.decorator import token_required, admin_token_required
from ..service import user_service, auth_helper

api = UserDto.api
_user = UserDto.user
_user_private = UserDto.user_private
_user_list = UserDto.user_list
_user_create = UserDto.user_create
_user_update = UserDto.user_update
_user_me = UserDto.user_me


@api.route('/')
class UserList(Resource):
  # /user ops

  @api.doc('list all users')
  @api.marshal_list_with(_user_list, envelope='data', skip_none=True)
  def get(self):
    return user_service.get_all_users()

  @api.response(201, 'created')
  @api.doc('create new user')
  @api.expect(_user_create, validate=True)
  def post(self):
    data = request.json
    return user_service.save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'the users public id')
@api.response(404, 'User not found')
class User(Resource):
  # /user/<id> ops

  @api.doc('get a user')
  def get(self, public_id):
    user = user_service.get_user_by_public_id(public_id)
    if not user:
      api.abort(404)
    
    if user.display_contact_info:
      return marshal(user, _user), 200
    
    return marshal(user, _user_private), 200


  @api.doc('admin update a user')
  @admin_token_required
  @api.expect(_user_update)
  def put(self, public_id):
    data = request.json()
    user = user_service.get_user_by_public_id(public_id)
    if not user:
      api.abort(404)
    else:
      return user_service.update_user(public_id, data)

  @api.doc('admin delete user')
  @admin_token_required
  def delete(self, public_id):
    user = user_service.get_user_by_public_id(public_id)
    if not user:
      api.abort(404)
    else:
      return user_service.delete_user_by_id(public_id)


@api.route('/me')
@api.param('public_id', 'the users public id')
class UserMe(Resource):
  # /user/me

  @api.doc('return current logged in user')
  @token_required
  @api.marshal_with(_user_me, skip_none=True)
  def get(self):
    data, status = auth_helper.Auth.get_logged_in_user(request)

    if status != 200:
      return data, status

    print(data)
    return user_service.get_user_by_public_id(data['data']['public_id'])
    

  @api.doc('update users account')
  @api.expect(_user_update)
  @token_required
  def put(self):
    data = request.json
    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_data[0]['data']
    return user_service.update_user(user['public_id'], data)

  @api.doc('delete users account')
  @token_required
  def delete(self):
    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_data[0]['data']
    return user_service.delete_user_by_id(user['public_id'])
