
from .. import db, flask_bcrypt


class Module(db.Model):

  __tablename__ = 'module'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(30), nullable=False, unique=True)
  
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  author = db.relationship('author', backref=db.backref('user', uselist=False))
  
  lessons = db.relationship('lesson', backref=db.backref('lesson', uselist=False))

  # prereqs - one to many (one module, many prereqs)

  rating = db.Column(db.Numeric, nullable=False, default=0)
  created_at = db.Column(db.DateTime, nullable=False)
  modified_at = db.Column(db.DateTime, nullable=True)
  views = db.Column(db.Integer)
  is_public = db.Column(db.Boolean, nullable=False, default=False) 

  def __repr__(self):
    return "<Module '{}'>".format(self.title)


Module.next_module_id = db.Column(db.Integer, db.ForeignKey(Module.id))
Module.next_module = db.relationship(Module, backref='module', remote_side=Module.id)
