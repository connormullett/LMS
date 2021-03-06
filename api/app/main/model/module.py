
from .. import db


class Module(db.Model):

  __tablename__ = 'module'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(30), nullable=False, unique=True)
  description = db.Column(db.String(200), nullable=True)
  
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  author = db.relationship('User', backref=db.backref('module_author', uselist=False))
  course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
  
  # this will have to change - one to many
  lessons = db.relationship('Lesson', backref=db.backref('lesson', uselist=True))

  next_module_id = db.Column(db.Integer, nullable=True)

  # prereqs - one to many (one module, many prereqs)

  created_at = db.Column(db.DateTime, nullable=False)
  modified_at = db.Column(db.DateTime, nullable=True)
  views = db.Column(db.Integer)
  is_public = db.Column(db.Boolean, nullable=False, default=False) 

  def __repr__(self):
    return "<Module '{}'>".format(self.title)


# Module.next_module_id = db.Column(db.Integer, db.ForeignKey(Module.id))
# Module.next_module = db.relationship(Module, backref='next_module', remote_side=Module.id)
