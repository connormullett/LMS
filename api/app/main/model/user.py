
from .. import db, flask_bcrypt

class User(db.Model):

  __tablename__ = 'user'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String(255), unique=True, nullable=False)
  registered_on = db.Column(db.DateTime, nullable=False)
  admin = db.Column(db.Boolean, nullable=False, default=False)
  public_id = db.Column(db.String(100), unique=True)
  username = db.Column(db.String(50), unique=True)
  first_name = db.Column(db.String(30), nullable=True)
  last_name = db.Column(db.String(30), nullable=True)
  password_hash = db.Column(db.String(100))
  bio = db.Column(db.String(200), nullable=True)
  country_code = db.Column(db.String(2), nullable=True)
  area_code = db.Column(db.String(3), nullable=True)
  number = db.Column(db.String(7), nullable=True)
  display_contact_info = db.Column(db.Boolean, nullable=False, default=False)
  last_login = db.Column(db.DateTime, nullable=True)

  @property
  def password(self):
    raise AttributeError('password: write-only field')

  @password.setter
  def password(self, password):
    self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
  
  def check_password(self, password):
    return flask_bcrypt.check_password_hash(self.password_hash, password)
  
  def __repr__(self):
    return "<User '{}'>".format(self.username)
