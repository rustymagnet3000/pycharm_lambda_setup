import requests
import os
import json


def get_secret_ingrediant():
    return os.environ.get('SECRET_SAUCE')


def get_all_ingredients(spice):
    print(spice)
    return {
        "ingrediant_1": "sugar",
        "ingrediant_2": "butter",
        "secret_sauce": get_secret_ingrediant(),
        "new_ingrediant": spice
    }


def send_cake_recipe(new_ingrediant):
    resp = requests.post(API_PATH, data=get_all_ingredients(new_ingrediant))
    if resp.ok:
        print("[*]request worked. status = {0}".format(resp.status_code))
        return json.loads(resp.content.decode('utf-8'))
    else:
        print("[!]request failed".format(resp.status_code))
        return None


HOSTNAME = "https://httpbin.org/"
API_PATH = '{0}post'.format(HOSTNAME)


def rm_handler(event, context):
    json_response = send_cake_recipe(event)
    print("[*]{0}".format(json.dumps(json_response, indent=4, sort_keys=True)))

