
from .. import db
from .question import Question


class Assessment(db.Model):

  __tablename__ = 'assessment'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  questions = db.relationship(Question, backref=db.backref('test_questions'), uselist=True)
  created_at = db.Column(db.DateTime, nullable=False)
  modified_at = db.Column(db.DateTime, nullable=True)
  module_id = db.Column(db.Integer, db.ForeignKey('module.id'))
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
