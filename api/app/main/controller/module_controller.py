
from flask import request
from flask_restplus import Resource

from ..util.dto import ModuleDto
from ..util.decorator import token_required, admin_token_required
from ..service import module_service, auth_helper, user_service


api = ModuleDto.api
_module_create = ModuleDto.module_create
_module = ModuleDto.module
_module_update = ModuleDto.module_update


@api.route('/')
class ModuleList(Resource):
  # /module ops

  @api.doc('create a module')
  @token_required
  @api.expect(_module_create, validate=True)
  def post(self):
    data = request.json
    user_object = auth_helper.Auth.get_logged_in_user(request)
    data['public_id'] = user_object[0]['data']['public_id']
    return module_service.create_new_module(data)

  @api.doc('get all modules')
  @api.marshal_list_with(_module, envelope='data', skip_none=True)
  def get(self):
    return module_service.get_all_public_modules()


@api.route('/<module_id>')
@api.param('module_id', 'id of the module')
@api.response(404, 'module not found')
@api.response(403, 'permission denied')
class Module(Resource):
  # /module/<id> ops

  @api.doc('get a module')
  @api.marshal_with(_module)
  def get(self, module_id):
    module = module_service.get_module_by_id(module_id)
    if not module:
      api.abort(404)
    else:
      return course
  
  @api.doc('update a module')
  @api.expect(_module_update, validate=True)
  @token_required
  def put(self, module_id):
    data = request.json
    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_service.get_user_by_public_id(user_data[0]['data']['public_id'])
    module = module_service.get_module_by_id(module_id)

    if not module:
      api.abort(404)

    if user.id != module.author.id:
      api.abort(403)
    return module_service.update_module(module_id, data)
  
  @api.doc('delete module')
  @token_required
  def delete(self, module_id):
    data = request.json
    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_service.get_user_by_public_id(user_data[0]['data']['public_id'])
    module = module_service.get_module_by_id(module_id)

    if not module:
      api.abort(404)
    
    if user.id != module.author.id:
      api.abort(403)
    return module_service.delete_module_by_id(module_id)
