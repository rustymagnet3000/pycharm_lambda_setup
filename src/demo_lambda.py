from base64 import b64decode
import requests
import os
from json import loads
import boto3

# ENCRYPTED = os.environ['SECRET_SAUCE']
# DECRYPTED = boto3.client('kms').decrypt(
#     CiphertextBlob=b64decode(ENCRYPTED),
#     EncryptionContext={'rm_handler': os.environ['MyPyLambdaFunction']}
# )['Plaintext'].decode('utf-8')


def get_secret_ingrediant():
    return os.environ.get('SECRET_SAUCE')


def get_all_ingredients(s):
    return {
        "ingrediant_1": "sugar",
        "ingrediant_2": "butter",
        "secret_sauce": get_secret_ingrediant(),
        "spice": s
    }


def send_cake_recipe(spice):
    resp = requests.post(API_PATH, data=get_all_ingredients(spice))
    return resp


HOSTNAME = "https://httpbin.org/"
API_PATH = '{0}post'.format(HOSTNAME)


def rm_handler(event, context):
    recipe_response = send_cake_recipe(event["spice"])
    return loads(recipe_response.content.decode('utf-8'))
