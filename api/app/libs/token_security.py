# Library imports
from app import db , current_language
from functools import wraps
from flask import request
import jwt
from config import GLOBALS
import random, string
from datetime import datetime
from bson.json_util import dumps, loads
from .languages import langs
from bson.objectid import ObjectId


# Token inspector
class token_required(object):

    def __call__(self, f):
        # required_abilitie = self.abilitie
        # required_role = self.role
        @wraps(f)
        def decorated(self, *args, **kwargs):
            token = None
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
                try:
                    # Decode the generated token on access login.
                    data = jwt.decode(token, GLOBALS.SECRET_KEY)
                    user = db.users.find_one({"_id": ObjectId(data["public_id"])})
                    # return str(user)
                    current_user = dict(name=user["name"], id=str(user["_id"]), email=user["email"], is_deleted=user["is_deleted"])
                    if not current_user:
                        return {'message': langs[current_language]['invalid-token'] + str(e)}, 401
                except Exception as e:
                    return {'message': langs[current_language]['invalid-token'] + str(e)}, 401

                return f(self, current_user, *args, **kwargs)
            if not token:
                return {'message': 'Permission denied token is required!'}, 401
        return decorated



# token handler for sockets



# Generate random password
def generate_random_password():
    try:
        length = 14
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        rnd = random.SystemRandom()
        return ''.join(rnd.choice(chars) for i in range(length))
    except Exception as e:
        return {"message": "Server Error!"}, 500

