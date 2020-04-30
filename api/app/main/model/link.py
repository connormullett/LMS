
from .. import db


class Link(db.Model):

  __tablename__ = 'link'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  link_text = db.Column(db.String(50), nullable=True)
  hyper_link = db.Column(db.String(100), nullable=False)
  is_public = db.Column(db.Boolean, default=False)
