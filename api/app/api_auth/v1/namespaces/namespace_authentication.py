from flask_restplus import Namespace, Resource, reqparse
from flask import request
from app import current_language
from app.libs.helper import run_in_loop
from app.libs.languages import langs
from ..controllers.middleware_authentication import MiddlewareAuthentication



auth_api = Namespace('authentication', description="Namespace de l'authentification")

from ..models.authentication_model import (
    login_model,register_model
)


@auth_api.route('/login')
class Login(Resource):
    @auth_api.expect(login_model)
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("email", type=str, required=True)
            parser.add_argument("password", type=str, required=True)
            data = parser.parse_args()
            return run_in_loop(MiddlewareAuthentication.async_login, data)
        except Exception as e:
            return {"message": langs[current_language]['server-error'] + str(e)}, 500

@auth_api.route('/register')
class Register(Resource):
    @auth_api.expect(register_model)
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("name", type=str, required=True)
            parser.add_argument("email", type=str, required=True)
            parser.add_argument("password", type=str, required=True)
            data = parser.parse_args()
            return run_in_loop(MiddlewareAuthentication.async_register, data)
        except Exception as e:
            return {"message": langs[current_language]['server-error'] + str(e)}, 500