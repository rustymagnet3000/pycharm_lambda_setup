import json
from requests.models import Response

import app


def invoke_function_and_get_message(function_name):
    lambda_client = app.get_lambda_client()
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse'
    )
    return json.loads(
        response['Payload']
        .read()
        .decode('utf-8')
    )


def generate_bad_response():
    resp = Response()
    resp.code = "expired"
    resp.error_type = "unauthorized"
    resp.status_code = 401
    resp._content = b'{ "status_code" : resp.status_code }'
    return resp


def test_unauthorized_send_cake_recipe(mocker):
    mocker.patch('app.send_cake_recipe', return_value=generate_bad_response())
    response = app.send_cake_recipe("bananas")
    assert response.status_code == 401


def test_send_cake_recipe():
    response = app.send_cake_recipe("nuts")
    assert response.status_code == 200


def test_get_environment_variable():
    assert app.get_secret_ingrediant() in 'chocolate'


def test_that_lambda_returns_correct_message():
    payload = invoke_function_and_get_message('lambda')
    assert 'Bad recipe' in payload

