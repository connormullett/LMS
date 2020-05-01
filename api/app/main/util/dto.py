
from flask_restplus import Namespace, fields


class UserDto:
  api = Namespace('user', description='user related ops')
  user = api.model('user public', {
    'email': fields.String(required=True, description='email address'),
    'public_id': fields.String(description='users public facing id'),
    'username': fields.String(required=True, descrition='username'),
    'first_name': fields.String(required=False, description='users first name (optional)'),
    'last_name': fields.String(required=False, description='users last name (optional)'),
    'bio': fields.String(required=False, description='users biography'),
    'registered_on': fields.DateTime(required=False, description='when the user joined'),
    'last_login': fields.DateTime(required=False, description='when the user last logged in')
  })

  user_private = api.model('user private', {
    'public_id': fields.String(description='users public facing id'),
    'username': fields.String(required=True, descrition='username'),
    'first_name': fields.String(required=False, description='users first name (optional)'),
    'last_name': fields.String(required=False, description='users last name (optional)'),
    'bio': fields.String(required=False, description='users biography'),
    'registered_on': fields.DateTime(required=False, description='when the user joined'),
    'last_login': fields.DateTime(required=False, description='when the user last logged in')
  })

  user_me = api.model('user profile', {
    'email': fields.String(required=True, description='email address'),
    'public_id': fields.String(description='users public facing id'),
    'username': fields.String(required=True, descrition='username'),
    'first_name': fields.String(required=False, description='users first name (optional)'),
    'last_name': fields.String(required=False, description='users last name (optional)'),
    'country_code': fields.Integer(required=False, description='users country code for associated phone number'),
    'area_code': fields.Integer(required=False, description='users area code for given phone number'),
    'phone_number': fields.Integer(required=False, description='users phone number (optional)'),
    'display_contact_info': fields.Boolean(required=False, description='should users pii be displayed'),
    'bio': fields.String(required=False, description='users biography'),
    'registered_on': fields.DateTime(required=False, description='when the user joined'),
    'last_login': fields.DateTime(required=False, description='when the user last logged in'),
    'display_contact_info': fields.Boolean(description='should users private contact data be shown')
  })

  user_list = api.model('user_list', {
    'public_id': fields.String(description='users public facing id'),
    'username': fields.String(required=True, descrition='username'),
    'last_login': fields.DateTime(required=False, description='when the user last logged in')
  })

  user_create = api.model('user_create', {
    'email': fields.String(required=True, description='email address'),
    'username': fields.String(required=True, descrition='username'),
    'first_name': fields.String(required=False, description='users first name (optional)'),
    'last_name': fields.String(required=False, description='users last name (optional)'),
    'country_code': fields.Integer(required=False, description='country code associated with phone number'),
    'area_code': fields.Integer(required=False, description='area code of phone number'),
    'phone_number': fields.Integer(required=False, description='rest of phone number'),
    'display_contact_info': fields.Boolean(required=False, description='should users pii be displayed'),
    'bio': fields.String(required=False, description='users biography'),
    'password': fields.String(required=True, description='users desired password'),
    'confirm_password': fields.String(required=True, description='password confirmation'),
  })

  user_update = api.model('user_update', {
    'email': fields.String(required=True, description='email address'),
    'username': fields.String(required=True, descrition='username'),
    'first_name': fields.String(required=False, description='users first name (optional)'),
    'last_name': fields.String(required=False, description='users last name (optional)'),
    'country_code': fields.Integer(required=False, description='country code associated with phone number'),
    'area_code': fields.Integer(required=False, description='area code of phone number'),
    'phone_number': fields.Integer(required=False, description='rest of phone number'),
    'display_contact_info': fields.Boolean(required=False, description='should users pii be displayed'),
    'bio': fields.String(required=False, description='users biography'),
  })


class AuthDto:
  api = Namespace('auth', description='authentication')
  user_auth = api.model('login', {
    'email': fields.String(required=True, description='email address'),
    'password': fields.String(required=True, description='password')
  })


class ModuleDto:
  api = Namespace('module', description='module model')
  module_create = api.model('module_create', {
    'title': fields.String(),
    'is_public': fields.Boolean(required=False),
    'description': fields.String(required=False),
    'course_id': fields.Integer(required=True)
  })

  module = api.model('module', {
    'id': fields.Integer(description='unique module identifier'),
    'title': fields.String(description='title of the module'),
    'description': fields.String(description='short description of the module'),
    'author_id': fields.String(description='id of the user that created the module'),
    'author': fields.Nested(UserDto.user_list),
    'course_id': fields.Integer(),
    # TODO: add lessons as nested attributes
    'created_at': fields.DateTime(description='timestamp of module creation'),
    'modified_at': fields.DateTime(description='timestamp of when module was last edited'),
    'views': fields.Integer(description='view count of module'),
    'is_public': fields.Boolean(description='defines if module can be viewed publicly')
  })

  module_update = api.model('module_update', {
    'title': fields.String(),
    'description': fields.String(),
    'is_public': fields.Boolean()
  })


class CourseDto:
  api = Namespace('course', description='courses model')
  course_create = api.model('course_create', {
    'title': fields.String(required=True, description='title of the course'),
    'description': fields.String(required=False, description='short description of the course'),
    'is_public': fields.Boolean(required=False, description='does the course get displayed')
  })

  course = api.model('course', {
    'id': fields.Integer(description='course unique identifier'),
    'title': fields.String(description='title of the course'),
    'description': fields.String(description='short description of the course'),
    'is_public': fields.Boolean(description='does the course get displayed'),
    'created_on': fields.DateTime(description='when the course was created'),
    'modified_on': fields.DateTime(description='last time the course was updated'),
    'author_id': fields.String(description='id of the user that created the course',
      attribute='author.public_id'),
    'author': fields.Nested(UserDto.user_list),
    'modules': fields.Nested(ModuleDto.module)
    # TODO: added modules for nested attributes
  })

  course_update = api.model('course_update', {
    'title': fields.String(description='title of the course'),
    'description': fields.String(description='short description of the course'),
    'is_public': fields.Boolean(description='does the course get displayed')
  })


class LessonDto:
  api = Namespace('lesson', description='lesson module')
  lesson_create = api.model('lesson_create', {
    'title': fields.String(description='title of the module'),
    'body': fields.String(description='text body of the lesson'),
    'is_public': fields.Boolean(description='defines if module can be viewed publicly')
  })

  lesson = api.model('lesson', {
    'id': fields.Integer(description='unique module identifier'),
    'title': fields.String(description='title of the module'),
    'description': fields.String(description='short description of the module'),
    'author_id': fields.String(description='id of the user that created the module'),
    'author': fields.Nested(UserDto.user_list),
    'body': fields.String(description='text body of the lesson'),
    'created_at': fields.DateTime(description='timestamp of module creation'),
    'modified_at': fields.DateTime(description='timestamp of when module was last edited'),
    'views': fields.Integer(description='view count of module'),
    'is_public': fields.Boolean(description='defines if module can be viewed publicly')
  })

  lesson_update = api.model('lesson_update', {
    'title': fields.String(description='title of the module'),
    'body': fields.String(description='text body of the lesson'),
    'description': fields.String(description='short description of the module')
  })


class LinkDto:
  api = Namespace('link')
  link_create = api.model('link_create', {
    'link_text': fields.String(),
    'hyper_link': fields.String(),
    'is_public': fields.Boolean()
  })

  link = api.model('link', {
    'id': fields.Integer(),
    'author_id': fields.String(),
    'author': fields.Nested(UserDto.user_list),
    'link_text': fields.String(),
    'hyper_link': fields.String(),
    'is_public': fields.Boolean()
  })

  link_update = api.model('link_update', {
    'link_text': fields.String(),
    'hyper_link': fields.String(),
    'is_public': fields.Boolean()
  })
