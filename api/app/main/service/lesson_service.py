
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


def _save_changes(data):
  db.session.add(data)
  db.session.commit()
