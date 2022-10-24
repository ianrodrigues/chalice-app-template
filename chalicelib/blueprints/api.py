from logging import getLogger

from chalice import Blueprint

logger = getLogger(__name__)

api = Blueprint(__name__)

logger.info("Loading module [%s].", __name__)


@api.route("/")
def index():
    logger.info("Processing function [%s.index].", __name__)
    return {"hello": "world"}
