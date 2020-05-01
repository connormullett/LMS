
from flask import request
from flask_restplus import Resource

from ..util.dto import LessonDto
from ..util.decorator import token_required, admin_token_required
from ..service import lesson_service, auth_helper, user_service


api = LessonDto.api
_lesson_create = LessonDto.lesson_create
_lesson = LessonDto.lesson
_lesson_update = LessonDto.lesson_update


@api.route('/')
class LessonList(Resource):
  # /link ops

  @api.doc('create a lesson')
  @token_required()
  @api.expect(_link_create, validate=True)
  def post(self):
    data = request.json
    user_object = auth_helper.Auth.get_logged_in_user(request)
    user = user_service.get_user_by_public_id(user_object[0]['data']['public_id'])
    data['user_id'] = user.id

    return lesson_service.save_new_lesson(data)


  # TODO: implement pathing for searching by parent ID's


@api.route('/<lesson_id>')
@api.param('lesson_id', 'id of lesson')
@api.response(404, 'lesson not found')
class Lesson(Resource):
  # /lesson/<id> ops

  @api.doc('get a lesson')
  @api.marshal_with(_lesson)
  def get(self, lesson_id):
    lesson = lesson_service.get_lesson_by_id(lesson_id)
    if not lesson:
      api.abort(404)
    else:
      return lesson
  
  @api.doc('update a lesson')
  @api.expect(_lesson_update, validate=True)
  @token_required
  def put(self, lesson_id):
    data = request.json
    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_service.get_user_by_public_id(user_data[0]['data']['public_id'])

    lessson = lesson_service.get_lesson_by_id(lesson_id)

    if not lesson:
      api.abort(404)
    
    if user.id != lesson.author.id:
      api.abort(403)
    
    return lesson_service.update_lesson(lesson_id, data)


  @api.doc('delete a lesson')
  @token_required
  def delete(self, lesson_id):
    data = request.json

    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_service.get_user_by_public_id(user_data[0]['data']['public_id'])

    lesson = lesson_service.get_lesson_by_id(lesson_id)

    if not lesson:
      api.abort(404)
    
    if user.id != lesson.author.id:
      api.abort(403)
    
    return lesson_service.delete_lesson_by_id(lesson_id)
