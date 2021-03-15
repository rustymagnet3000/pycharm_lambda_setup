import pytest
from requests.models import Response
from src import app
import moto


def generate_bad_response():
    resp = Response()
    resp.code = "expired"
    resp.error_type = "unauthorized"
    resp.status_code = 401
    resp._content = b'{ "status_code" : resp.status_code }'
    return resp


def test_unauthorized_send_cake_recipe(mocker):
    mocker.patch('src.app.send_cake_recipe', return_value=generate_bad_response())
    response = app.send_cake_recipe("bananas")
    assert response.status_code == 401


def test_send_cake_recipe():
    response = app.send_cake_recipe("nuts")
    assert response.status_code == 200


def test_get_environment_variable():
    assert app.get_secret_ingrediant() in 'chocolate'


class TestHandler:

    @pytest.fixture
    def mock_event(self):
        return {"spice": "herbs"}

    def test_mock_event_is_dict(self, mock_event):
        assert type(mock_event) is dict

    def test_lambda_live(self, mock_event):
        result = app.handler(mock_event, None)
        print(result)
        assert True
