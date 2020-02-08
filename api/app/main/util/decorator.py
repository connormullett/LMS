
from functools import wraps
from flask import request

from app.main.service.auth_helper import Auth


def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    data, status = Auth.get_logged_in_user(request)
    token = data.get('data')

    if not token:
      return data, status

    return f(*args, **kwargs)

  return decorated


def admin_token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    data, status = Auth.get_logged_in_user(request)
    user_data = data.get('token')

    if not user_data:
      return data, status

    admin = token.get('admin')

    if not admin:
      return {
        'status': 'fail',
        'message': 'admin token required'
      }, 401

    return f(*args, **kwargs)

  return decorated
