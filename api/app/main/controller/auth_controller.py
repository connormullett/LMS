
from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
  @api.doc('user login')
  @api.expect(user_auth, validate=True)
  def post(self):
    data = request.json
    return Auth.login_user(data=data)


@api.route('/logout')
class UserLogout(Resource):
  @api.doc('logout a user')
  def post(self):
    # 'Authorization <token>' as header
    token = request.headers.get('Authorization')
    return Auth.logout_user(token)
