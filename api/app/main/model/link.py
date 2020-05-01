
from .. import db


class Link(db.Model):

  __tablename__ = 'link'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  author = db.relationship('User', backref=db.backref('link_author', uselist=False))
  link_text = db.Column(db.String(50), nullable=True)
  hyper_link = db.Column(db.String(100), nullable=False)
  is_public = db.Column(db.Boolean, default=False)

  created_at = db.Column(db.DateTime, nullable=False)
  modified_at = db.Column(db.DateTime, nullable=True)
  def __repr__(self):
    return "<Link '{}'>".format(self.title)
