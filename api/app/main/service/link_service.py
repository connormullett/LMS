
import datetime

from app.main import db
from app.main.model.link import Link

from app.main.service import user_service


def save_new_link(data):

  user = user_service.get_user_by_public_id(data['public_id'])
  user_id = user.id

  new_link = Link(
    created_by=user_id,
    link_text=data['link_text'],
    hyper_link=data['hyper_link'],
    is_public=data['is_public'] or False
  )

  _save_changes(new_link)
  return {
    'status': 'created'
  }, 201

def get_link_by_id(link_id):
  return Link.query.filter_by(id=link_id).first()


def delete_link_by_id(link_id):
  link = get_link_by_id(link_id)
  db.session.delete(link)
  _save_changes()
  return {'status': 'deleted'}, 200


def delete_link_by_instance(link):
  db.session.delete(link)
  _save_changes()
  return {
    'status': 'deleted'
  }, 200


def update_link(link_id, data):
  link = get_link_by_id(link_id)
  for key, item in data.items():
    setattr(link, key, item)
  link.modified_at = datetime.datetime.utcnow()
  db.session.commit()
  return {
    'status': 'updated course'
  }, 200


def _save_changes(data):
  db.session.add(data)
  db.session.commit()
