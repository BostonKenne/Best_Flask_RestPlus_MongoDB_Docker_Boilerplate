import os


class Base:
    DEBUG = False
    PORT = 80
    HOST = '0.0.0.0'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    UPLOADED_IMAGES_DEST = "/webapp/app/static/image_uploads"

    @staticmethod
    def init_app(app):
        pass


class Development(Base):
    DEBUG = True


# Object production handler
class Production(Base):
    DEBUG = False
    # APPLICATION SERVER DEFAULTS
    #############################
    #    PRODUCTION USE ONLY    #
    #############################


# Object test handler
class Test(Base):
    DEBUG = True
    TESTING = True
    LIVESERVER_PORT = 9000



# Config arguments
config = {
    'DEVELOPMENT': Development,
    'PRODUCTION': Production,
    'DEFAULT': Development,
    'TEST': Test
}


# Global variables
class GLOBALS:
    ACCESS_ADMIN_KEY = "api2020BK"
    ENV = 'DEVELOPMENT'  # To change
    CONF = config[ENV]
    SECRET_KEY = Development.SECRET_KEY  # To change

    MAX_LOGIN_ATTEMPS = 5
    UPLOAD_IMAGES_DEST = Development.UPLOADED_IMAGES_DEST   # To change

