import os
from typing import Iterator

from chalice.test import Client
from pytest import fixture

from app import app

os.environ["CHALICE_DEBUG"] = "True"
os.environ["CHALICE_STAGE"] = "test"


@fixture
def chalice_client() -> Iterator[Client]:
    with Client(app) as client:
        yield client
