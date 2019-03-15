from app import create_app
from config import config, GLOBALS

app = create_app(GLOBALS.ENV)

if __name__ == "__main__":
    app.run(host=GLOBALS.CONF.HOST, debug=GLOBALS.CONF.DEBUG, port=GLOBALS.CONF.PORT)
