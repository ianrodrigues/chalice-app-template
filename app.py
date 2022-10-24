from chalice import Chalice

from chalicelib import logging, sentry
from chalicelib.blueprints.api import api

logging.configure_logging()
sentry.configure_sentry()

app = Chalice(app_name=":app-name:")
app.register_blueprint(api)
