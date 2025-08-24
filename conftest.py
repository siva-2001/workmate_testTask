import pytest
from router import router

@pytest.fixture(scope='module')
def router_object():
    yield router

