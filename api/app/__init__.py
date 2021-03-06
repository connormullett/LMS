
from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.course_controller import api as course_ns
from .main.controller.link_controller import api as link_ns
from .main.controller.lesson_controller import api as lesson_ns
from .main.controller.module_controller import api as module_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
  title='Learning Management System',
  version='1.0',
  description='name to be determined'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(course_ns, path='/course')
api.add_namespace(link_ns, path='/link')
api.add_namespace(lesson_ns, path='/lesson')
api.add_namespace(module_ns, path='/module')
