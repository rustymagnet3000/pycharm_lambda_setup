import requests
import os
from json import loads, dumps
import logging
import boto3
import botocore

CONFIG = botocore.config.Config(retries={'max_attempts': 0})

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def get_lambda_client():
    return boto3.client(
        'lambda',
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='eu-west-2',
        endpoint_url='',
        config=CONFIG
    )


def get_secret_ingrediant():
    return os.environ.get('SECRET_SAUCE')


def get_all_ingredients(spice):
    return {
        "ingrediant_1": "sugar",
        "ingrediant_2": "butter",
        "secret_sauce": get_secret_ingrediant(),
        "spice": spice
    }


def send_cake_recipe(spice):
    resp = requests.post(API_PATH, data=get_all_ingredients(spice))
    return resp


HOSTNAME = "https://httpbin.org/"
API_PATH = '{0}post'.format(HOSTNAME)


def handler(event, context):
    rec_body = dumps(event)
    LOGGER.info("Handler called!\tevent type:{0}".format(type(event)))
    if "spice" in event:
        recipe_response = send_cake_recipe(event["spice"])
        return loads(recipe_response.content.decode('utf-8'))
    else:
        return {
            "statusCode": 200,
            "body": dumps(
                {
                    "Bad recipe": "No spice passed to cake recipe",
                }
            ),
        }

