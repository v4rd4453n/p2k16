import os

from flask import Flask

app = Flask(__name__, static_folder="../p2k16_web/static")

app.config.BOWER_KEEP_DEPRECATED = False
app.config['BOWER_COMPONENTS_ROOT'] = '../p2k16_web/bower_components'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

p2k16_config = os.getenv('P2K16_CONFIG')
if p2k16_config is not None:
    app.logger.info("Loading config from {}".format(p2k16_config))
    app.config.from_envvar('P2K16_CONFIG')
    app.logger.info("current dir = {}".format(os.path.abspath(os.curdir)))
    secret_file = os.path.abspath('./web/config-secret.cfg')
    if os.path.isfile(secret_file):
        app.logger.info("Loading config %s" % secret_file)
        app.config.from_pyfile(secret_file)


class P2k16UserException(Exception):
    """Exception that happened because the user did something silly. The message will be shown to the user"""

    def __init__(self, msg):
        self.msg = msg


class P2k16TechnicalException(Exception):
    """Exception for unexpected stuff."""
    pass