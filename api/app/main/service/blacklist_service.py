
from app.main import db
from app.main.model.blacklist import BlacklistToken

def save_token(token):
  blacklist_token = BlacklistToken(token=token)
  try:
    db.session.add(blacklist_token)
    db.session.commit()
    return {
      'status': 'success',
      'message': 'successfuly logged out'
    }, 200
  except Exception:
    return {
      'status': 'fail',
      'message': 'an error occured'
    }, 500
  
