
import datetime

from app.main import db
from app.main.model.link import Link

from app.main.service import user_service


def save_new_link(data):
  new_link = Link(
    created_by=data['user_id'],
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
  return {'status': 'delete'}, 200


def _save_changes(data):
  db.session.add(data)
  db.session.commit()
