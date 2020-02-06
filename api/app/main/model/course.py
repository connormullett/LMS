
from .. import db


class Course(db.Model):

  __tablename__ = 'course'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(50), nullable=False, unique=True)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  author = db.relationship('User', backref=db.backref('course_author', uselist=False))
  description = db.Column(db.String(200), nullable=True)
  is_public = db.Column(db.Boolean, default=False, nullable=False)

  # TODO: change these to keys that refer back to this table for next values
  next_course_id = db.Column(db.Integer, nullable=True)
  views = db.Column(db.Integer)

  # todo: roles, students


# Course.next_course_id = db.Column(db.Integer, db.ForeignKey(Course.id))
# Course.next_course = db.relationship(Course, backref='next_course', remote_side=Course.id)
