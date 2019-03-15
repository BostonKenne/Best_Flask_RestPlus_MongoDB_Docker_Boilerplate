from ..namespaces.namespace_authentication import auth_api
from flask_restplus import fields


login_model = auth_api.model("login", {
    "email": fields.String(description="user email", help="must not be blank", required=True),
    "password": fields.String(description="user password", help="must not be blank", required=True)
})


register_model = auth_api.model("register", {
    "name": fields.String(description="user name", help="must not be blank", required=True),
    "email": fields.String(description="user email", help="must not be blank", required=True),
    "password": fields.String(description="user password", help="must not be blank", required=True)
})