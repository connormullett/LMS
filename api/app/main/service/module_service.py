
import datetime

from app.main import db
from app.main.model.module import Module
from app.main.service import user_service


def create_new_module(data):

  user = user_service.get_user_by_public_id(data['public_id'])
  user_id = user.id

  new_module = Module(
    title=data.get('title'),
    author_id=user_id,
    created_at=datetime.datetime.utcnow(),
    views=0,
    is_public=data.get('is_public')
  )

  _save_changes(new_module)
  return {
    'status': 'created'
  }, 201


def get_modules_by_course_id(course_id):
  return Module.query.filter_by(course_id=course_id).filter_by(is_public=True).all()


def get_modules_by_user_id(user_id):
  return Module.query.filter_by(author_id=user_id).all()


def get_module_by_id(module_id):
  return Module.query.filter_by(id=module_id).first()


def update_module(module_id, data):
  module = get_module_by_id(module_id)
  for key, item in data.items():
    setattr(module, key, item)
  module.modified_on = datetime.datetime.utcnow()
  db.session.commit()
  return {
    'status': 'updated module'
  }, 200


def delete_module(module_id):
  module = get_module_by_id(module_id)
  db.session.delete(module)
  _save_changes()
  return {'status': 'delete'}, 200


def _save_changes(data=None):
  if data:
    db.session.add(data)
  
  db.session.commit()
