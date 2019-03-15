from flask_restplus import Namespace, Resource, reqparse, fields
from flask import request, jsonify
from app import current_language, lang, db
from app.libs.languages import langs
from app.libs.token_security import token_required
# from app.libs.helper import serial_data
import json
from bson.json_util import dumps, loads

# from app.libs.helper import run_in_loop
# from ..controllers.middleware_authentication import MiddlewareAuthentication



user_api = Namespace('users', description="Namespace de gestion des utilisateurs")



@user_api.route('')
class UserRoute(Resource):
    @user_api.doc(security="apikey")
    @token_required()
    def get(self, current_user):
        ''' Get all users '''
        try:
            return  dumps(db.users.find())
        except Exception as e:
            return {"message":  langs[current_language]['server-error'] + str(e)}, 500
    @user_api.doc(security="apikey")
    @token_required()
    def put(self, current_user):
        ''' Route for update the user account '''
        try:
            return  dumps(db.users.find())
        except Exception as e:
            return {"message":  langs[current_language]['server-error'] + str(e)}, 500



