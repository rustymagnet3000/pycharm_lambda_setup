import requests
import os
from json import loads


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


def handler(event, context):
    recipe_response = send_cake_recipe(event["spice"])
    return loads(recipe_response.content.decode('utf-8'))
