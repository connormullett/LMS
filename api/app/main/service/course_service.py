
import datetime

from app.main import db
from app.main.model.course import Course
from app.main.service import user_service


def save_new_course(data):

  user = user_service.get_user_by_public_id(data['public_id'])
  user_id = user.id
  
  new_course = Course(
    title=data['title'],
    author_id=user_id,
    description=data['description'],
    is_public=data['is_public'],
    created_on=datetime.datetime.utcnow()
  )

  _save_changes(new_course)
  return {
    'status': 'created',
  }, 201


def get_all_courses():
  return Course.query.filter_by(is_public=True).all()


def get_course_by_id(course_id):
  course = Course.query.filter_by(id=course_id).first()
  print(course.author.public_id)
  return course


def _save_changes(data):
  db.session.add(data)
  db.session.commit()
