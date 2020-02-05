
from .. import db


class Lesson(db.Model):

  __tablename__ = 'lesson'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(30), unique=True, nullable=False)

  author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  author = db.relationship('author', backref=db.backref('user', uselist=False))

  module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)

  body = db.Column(db.String(1000), nullable=False)
  rating = db.Column(db.Numeric, nullable=False, default=0)
  created_at = db.Column(db.DateTime, nullable=False)
  modified_at = db.Column(db.DateTime, nullable=True)
  views = db.Column(db.Integer)
  is_public = db.Column(db.Boolean, nullable=False, default=False)

  def __repr__(self):
    return "<lesson '{}'>".format(self.title)

Lesson.next_lesson_id = db.Column(db.Integer, db.ForeignKey(Lesson.id))
Lesson.next_lesson = db.relationship(Lesson, backref='lesson', remote_side=Lesson.id)
