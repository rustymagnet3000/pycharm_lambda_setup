import json
from requests.models import Response
import boto3
from moto import mock_lambda
import src

# https://docs.pytest.org/en/stable/goodpractices.html


def invoke_function_and_get_message(function_name):
    lambda_client = boto3.client('lambda', region_name='eu-west-1')
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


@mock_lambda
def test_that_lambda_returns_correct_message():
    payload = {"args": {}, "data": "", "files": {},
               "form": {"ingrediant_1": "sugar", "ingrediant_2": "butter", "spice": "nutmeg"},
               "headers": {"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "Content-Length": "51",
                           "Content-Type": "application/x-www-form-urlencoded", "Host": "httpbin.org",
                           "User-Agent": "python-requests/2.25.1",
                           "X-Amzn-Trace-Id": "Root=1-604ef622-1e2b8d1c300ddd233ab26674"}, "json": "",
               "origin": "92.234.25.98", "url": "https://httpbin.org/post"}
    print(payload)
    assert 'Bad recipe' in payload
