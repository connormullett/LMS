
from app.main import db
from app.main.model.blacklist import BlacklistToken

def save_token(token):
  blacklist_token = BlacklistToken(token=token)
  try:
    db.session.add(blacklist_token)
    db.session.commit()
    return True
  except Exception:
    return False
  
