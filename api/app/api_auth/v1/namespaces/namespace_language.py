from flask_restplus import Namespace, Resource, reqparse, fields
from flask import request, jsonify
from app import current_language, lang
from app.libs.languages import langs
from app.libs.helper import run_in_loop
from ..controllers.middleware_authentication import MiddlewareAuthentication
# from app.libs.token_security import token_required



lang_api = Namespace('language', description="Namespace de gestion des langues")


change_lang_model = lang_api.model('change_language', {
    'lang': fields.String(description="Change app language", help="must not be blank", required=True)
} )

@lang_api.route('')
class Login(Resource):
    def get(self):
        ''' Get the current language '''
        try:
            return jsonify({
                'language': str(current_language),
                 "message": langs[current_language]['welcome']
            })
        except Exception as e:
            return {"message":  langs[current_language]['server-error'] + str(e)}, 500


    @lang_api.expect(change_lang_model)
    def post(self):
        """ Change the current language  """
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('lang', type=str, required=True)
            data = parser.parse_args()
            lang.change_language(data['lang'])
            return jsonify({
                'language': str(current_language),
            })
        except Exception as e:
            return {'message': "server-error "+ str(e) }



    # @app.route('/api/language', methods=['POST'])
    # def set_language():
    #     req = request.get_json()
    #     language = req.get('language', None)

    #     lang.change_language(language)

    #     return jsonify({
    #         'language': str(current_language),
    #     })