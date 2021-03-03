import demo_lambda
from requests.models import Response


def generate_bad_response():
    resp = Response()
    resp.code = "expired"
    resp.error_type = "unauthorized"
    resp.status_code = 401
    resp._content = b'{ "status_code" : resp.status_code }'
    return resp


def test_unauthorized_send_cake_recipe(mocker):
    mocker.patch('demo_lambda.send_cake_recipe', return_value=generate_bad_response())
    response = demo_lambda.send_cake_recipe("bananas")
    assert response.status_code == 401


def test_send_cake_recipe():
    response = demo_lambda.send_cake_recipe("nuts")
    assert response.status_code == 200


def test_get_environment_variable():
    assert demo_lambda.get_secret_ingrediant() in 'chocolate'
