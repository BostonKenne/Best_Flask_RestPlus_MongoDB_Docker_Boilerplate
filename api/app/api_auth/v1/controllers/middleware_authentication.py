
import jwt
from config import GLOBALS
from app import current_language, db
from app.libs.languages import langs
from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import dumps
from datetime import datetime, timedelta


class MiddlewareAuthentication:

    # login
    @classmethod
    async def login(cls, auth: any) -> (list, int, str):
        try:
            # Required condition
            user = db.users.find({"email": auth['email']}).count()
            if not user:
                return {'message': langs[current_language]['user-not-found']}, 404
            # check password
            user = db.users.find({"email": auth['email']})
            for record in user:
                verify_password = check_password_hash(record['password'], auth['password'])
                user_id = record['_id']
                user_email = record['email']
            # Generate token
            if verify_password:
                token = jwt.encode({
                                    'public_id': str(user_id),
                                    # 'email': str(user_email),
                                    'exp': datetime.utcnow() + timedelta(days=365)
                                    },
                                    GLOBALS.SECRET_KEY)
                return {'token': token.decode('UTF-8')}, 200
            else:
                return {'message': langs[str(current_language)]['user-invalid']}, 401
        except Exception as e:
            return {'message': langs[str(current_language)]['server-error'] + str(e)}, 500


    @classmethod
    async def async_login(cls, data: any) -> (list, str, int):
        try:
            return await cls.login(auth=data)
        except Exception as e:
            return {'message': langs[current_language]['server-error'] + str(e)}, 500


    #register methods
    @classmethod
    async def register(cls, data: any) -> (list, str, int):
        try:
            # step 1: check user email and user name
            check_user_email =  db.users.find({"email": data['email']}).count()
            check_user_name =  db.users.find({"name": data['name']}).count()
            if check_user_email:
                return {'message': langs[current_language]['email-taken']}, 500
            if check_user_name:
                return {'message': langs[current_language]['user-name-taken']}, 500
            data['password'] = str(generate_password_hash(data['password']))  #hashing password
            # database insertion
            data['is_deleted'] = False
            db.users.insert_one(data)

            # # test
            # role = dict(name="Admin", type="super admin")
            # db.roles.insert_one(role)


            return  {'message': langs[current_language]['user-created-successfully']}, 201
        except Exception as e:
            return {'message': langs[current_language]['server-error'] + str(e)}, 500


    #async register
    @classmethod
    async def async_register(cls, data: any) -> (list, str, int):
        try:
            return await cls.register(data=data)
        except Exception as e:
            return {'message': langs[current_language]['server-error'] + str(e)}, 500

