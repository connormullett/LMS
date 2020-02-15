
from flask import request
from flask_restplus import Resource

from ..util.dto import CourseDto
from ..util.decorator import token_required, admin_token_required
from ..service import course_service, auth_helper


api = CourseDto.api
_course_create = CourseDto.course_create


@api.route('/')
class CourseList(Resource):
  # /course ops

  @api.doc('create a course')
  @token_required
  @api.expect(_course_create, validate=True)
  def post(self):
    data = request.json
    user_object = auth_helper.Auth.get_logged_in_user(request)
    print(user_object)
    data['public_id'] = user_object[0]['data']['public_id']
    return course_service.save_new_course(data)
