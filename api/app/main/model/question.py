
from .. import db


class Question(db.Model):
  
  __tablename__ = 'question'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  assessment_id = db.Column(db.Integer(), db.ForeignKey('assessment.id'))

  # TODO: question type implementation, answers, num questions, etc

