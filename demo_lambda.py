import requests
import os
import json


def get_secret_ingrediant():
    return os.environ.get('SECRET_SAUCE')


def send_cake_recipe():
    resp = requests.post(API_PATH, data=CAKE_RECIPE)
    if resp.ok:
        json_response = json.loads(resp.content.decode('utf-8'))
        print("[*]request worked. {0}".format(json.dumps(json_response, indent=4, sort_keys=True)))
        return True
    else:
        print("[!]request failed".format(resp.status_code))
        return False


HOSTNAME = "https://httpbin.org/"

API_PATH = '{0}post'.format(HOSTNAME)
CAKE_RECIPE = {
        "ingrediant_1": "sugar",
        "ingrediant_2": "butter",
        "secret_sauce": get_secret_ingrediant(),
    }


def rm_handler(event, context):
    return send_cake_recipe()

