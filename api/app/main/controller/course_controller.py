
from flask import request
from flask_restplus import Resource

from ..util.dto import CourseDto
from ..util.decorator import token_required, admin_token_required
from ..service import course_service, auth_helper, user_service


api = CourseDto.api
_course_create = CourseDto.course_create
_course = CourseDto.course
_course_update = CourseDto.course_update


@api.route('/')
class CourseList(Resource):
  # /course ops

  @api.doc('create a course')
  @token_required
  @api.expect(_course_create, validate=True)
  def post(self):
    data = request.json
    user_object = auth_helper.Auth.get_logged_in_user(request)
    data['public_id'] = user_object[0]['data']['public_id']
    return course_service.save_new_course(data)
  
  @api.doc('get all courses')
  @api.marshal_list_with(_course, envelope='data', skip_none=True)
  def get(self):
    return course_service.get_all_public_courses()


@api.route('/<int:course_id>')
@api.param('course_id', 'id of the course')
@api.response(404, 'course not found')
@api.response(403, 'permission denied')
class Course(Resource):
  # /course/<id> ops

  @api.doc('get a course')
  @api.marshal_with(_course)
  def get(self, course_id):
    course = course_service.get_course_by_id(course_id)
    if not course:
      api.abort(404)
    else:
      return course

  @api.doc('update a course')
  @api.expect(_course_update, validate=True)
  @token_required
  def put(self, course_id):
    data = request.json
    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_service.get_user_by_public_id(user_data[0]['data']['public_id'])
    course = course_service.get_course_by_id(course_id)

    if not course:
      api.abort(404)

    if user.id != course.author.id:
      api.abort(403)
    return course_service.update_course(course_id, data)
  
  @api.doc('delete course')
  @token_required
  def delete(self, course_id):
    data = request.json
    user_data = auth_helper.Auth.get_logged_in_user(request)
    user = user_service.get_user_by_public_id(user_data[0]['data']['public_id'])
    course = course_service.get_course_by_id(course_id)

    if not course:
      api.abort(404)

    if user.id != course.author.id:
      api.abort(403)
    return course_service.delete_course_by_id(course_id)
  

@api.route('/me')
class CourseMe(Resource):

  @api.doc('get logged in user\'s courses')
  @api.marshal_list_with(_course, envelope='data')
  @token_required
  def get(self):
    user = auth_helper.Auth.get_logged_in_user(request)
    user_id = user_service.get_user_by_public_id(user[0]['data']['public_id']).id
    return course_service.get_courses_by_users_id(user_id)
