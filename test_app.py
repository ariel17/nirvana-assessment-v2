from http import HTTPStatus

import pytest

import configs
from app import app


@pytest.fixture
def client():
    return app.test_client()


class TestController:

    def test_400_missing_parameter(self, client):
        r = client.get("/")
        assert HTTPStatus.BAD_REQUEST == r.status_code

    def test_400_invalid_value(self, client):
        r = client.get("/?member_id=x")
        assert HTTPStatus.BAD_REQUEST == r.status_code

    def test_200_ok(self, client):
        r = client.get("/?member_id=1")
        assert HTTPStatus.OK == r.status_code

    def test_500_by_external_error(self, client):
        for api1_must_fail, api2_must_fail, api3_must_fail in [
            (True, False, False),
            (False, True, False),
            (False, False, True),
        ]:
            configs.API1_MUST_FAIL = api1_must_fail
            configs.API2_MUST_FAIL = api2_must_fail
            configs.API3_MUST_FAIL = api3_must_fail
            r = client.get("/?member_id=1")
            assert HTTPStatus.INTERNAL_SERVER_ERROR == r.status_code
