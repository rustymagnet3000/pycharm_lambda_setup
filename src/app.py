import requests
import os
from json import loads, dumps
import logging


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


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
    LOGGER.info("Handler called!\tevent type:{0}".format(type(event)))
    if "spice" in event:
        recipe_response = send_cake_recipe(event["spice"])
        recipe_json = loads(recipe_response.content.decode('utf-8'))
        LOGGER.info("JSON response\n{0}".format(recipe_json))
        return recipe_json
    else:
        return {
            "statusCode": 200,
            "body": dumps(
                {
                    "Bad recipe": "No spice passed to cake recipe",
                }
            ),
        }

