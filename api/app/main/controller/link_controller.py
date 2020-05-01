
from flask import request
from flask_restplus import Resource, marshal

from ..util.dto import LinkDto
from ..util.decorator import token_required, admin_token_required
from ..service import link_service, auth_helper


api = LinkDto.api
_link_create = LinkDto.link_create
_link = LinkDto.link
_link_update = LinkDto.link_update


@api.route('/')
class LinkList(Resource):
  # /link ops

  @api.doc('create a link')
  @token_required
  @api.expect(_link_create, validate=True)
  def post(self):
    data = request.json
    user_object = auth_helper.Auth.get_logged_in_user(request)
    data['public_id'] = user_object[0]['data']['public_id']
    return link_service.save_new_link(data)
  

@api.route('/<link_id>')
@api.param('link_id', 'id of link')
@api.response(404, 'link not found')
@api.response(403, 'permission denied')
class Link(Resource):
  # /link/<id> ops

  @api.doc('get a link')
  @api.marshal_with(_link)
  def get(self, link_id):
    link = link_service.get_link_by_id(link_id)
    if not link:
      api.abort(404)
    else:
      return link

  @api.doc('update a link')
  @api.expect(_link_update, validate=True)
  @token_required
  def put(self, link_id):
    data = request.json
    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_service.get_user_by_public_id(user_data[0]['data']['public_id'])

    link = link_service.get_link_by_id(link_id)

    if not link:
      api.abort(404)
    
    if user.id != link.author.id:
      api.abort(403)
    
    return link_service.update_link(link_id, data)
  
  @api.doc('delete link')
  @token_required
  def delete(self, link_id):
    data = request.json
    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_service.get_user_by_public_id(user_data[0]['data']['public_id'])

    link = link_service.get_link_by_id(link_id)

    if not link:
      api.abort(404)
    
    if user.id != link.author.id:
      api.abort(403)
    
    return link_service.delete_link_by_id(link_id)
