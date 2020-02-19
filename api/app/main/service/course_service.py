
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


def get_all_public_courses():
  return Course.query.filter_by(is_public=True).all()


def get_course_by_id(course_id):
  return Course.query.filter_by(id=course_id).first()


def get_courses_by_users_id(user_id):
  return Course.query.filter_by(author_id=user_id).all()


def update_course(course_id, data):
  course = get_course_by_id(course_id)
  for key, item in data.items():
    setattr(course, key, item)
  course.modified_on = datetime.datetime.utcnow()
  db.session.commit()
  return { 
    'status': 'updated course'
  }, 200


def delete_course_by_id(course_id):
  course = get_course_by_id(course_id)
  db.session.delete(course)
  _save_changes()
  return {'status': 'deleted'}, 200


def _save_changes(data=None):
  if data:
    db.session.add(data)

  db.session.commit()
