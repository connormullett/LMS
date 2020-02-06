
from app.main.model.user import User
from ..service.blacklist_service import save_token


class Auth:

  @staticmethod
  def login_user(data):
    try:
      user = User.query.filter_by(email=data.get('email')).first()
      if user and user.check_password(data.get('password')):
        auth_token = user.encode_auth_token(user.id)
        if auth_token:
          return {
            'status': 'success',
            'Authorization': auth_token.decode()
          }, 200
        else:
          return {
            'status': 'fail',
            'message': 'email or password does not match'
          }
    except Exception as e:
      # TODO: log bad login attempts ?? 
      print(e)
      return { 
        'status': 'fail',
        'message': 'an error occured, try again'
      }, 500
  
  @staticmethod
  def logout_user(data):
    if data:
      auth_token = data.split(" ")[1]
    else:
      auth_token = ''
    
    if auth_token:
      resp = User.decode_auth_token(auth_token)
      if not isinstance(resp, str):
        return save_token(token=auth_token)
      else:
        return {
          'status': 'fail',
          'message': resp
        }, 401
    else:
      return {
        'status': 'fail',
        'message': 'invalid auth token'
      }, 403
