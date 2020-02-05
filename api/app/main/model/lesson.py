
from .. import db, flask_bcrypt


class Lesson(db.Model):

  __tablename__ = 'lesson'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(30), unique=True, nullable=False)

  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  author = db.relationship('author', backref=db.backref('user', uselist=False))

  module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)

  # TODO should relate another lesson
  # next_lesson = db.Column(db.String(40), nullable=True)

  body = db.Column(db.String(1000), nullable=False)
  rating = db.Column(db.Numeric, nullable=False, default=0)
  created_at = db.Column(db.DateTime, nullable=False)
  modified_at = db.Column(db.DateTime, nullable=True)
  views = db.Column(db.Integer)
  is_public = db.Column(db.Boolean, nullable=False, default=False)

  def __repr__(self):
    return "<lesson '{}'>".format(self.title)
