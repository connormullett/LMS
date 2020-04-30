
import datetime

from app.main import db
from app.main.model.lesson import Lesson
from app.main.model.user import User

from app.main.service import user_service


def save_new_lesson(data):

  # data['user_id'] should be set in controller

  new_lesson = Lesson(
    title=data['title'],
    body=data['body'],
    created_at=datetime.datetime.utcnow(),
    is_public=data['is_public'] or False,
    author_id=data['user_id'],
    module_id=data['module_id']
  )

  _save_changes(new_lesson)
  return {
    'status': 'created'
  }, 201


def get_all_public_lessons():
  return Lesson.query.filter_by(is_public=True)


def get_all_public_lessons_by_module_id(module_id):
  return Lesson.query.filter_by(module_id=module_id).filter_by(is_public=True).all()


def get_all_lessons_by_module_id(module_id):
  return Lesson.query.filter_by(module_id=module_id).all()


def get_lesson_by_id(lesson_id):
  return Lesson.query.filter_by(id=lesson_id).first()


def update_lesson(lesson_id):
  lesson = get_lesson_by_id(lesson_id)
  for key, item in data.items():
    setattr(lesson, key, item)
  lesson.modified_at = datetime.datetime.utcnow()
  db.session.commit()
  return {
    'status': 'updated module'
  }, 200


def delete_lesson_by_id(lesson_id):
  lesson = get_lesson_by_id(lesson_id)
  db.session.delete(lesson)
  _save_changes()
  return {'status': 'delete'}, 200


def _save_changes(data):
  db.session.add(data)
  db.session.commit()
