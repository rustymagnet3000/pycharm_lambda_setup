import requests
import os
import json

HOSTNAME = "https://httpbin.org/"
API_PATH = '{0}post'.format(HOSTNAME)
CAKE_RECIPE = {
        "ingrediant_1": "sugar",
        "ingrediant_2": "butter",
        "secret_sauce": os.environ.get('SECRET_SAUCE'),
    }


if __name__ == "__main__":

    resp = requests.post(API_PATH, data=CAKE_RECIPE)
    if resp.ok:
        json_response = json.loads(resp.content.decode('utf-8'))
        print("[*]request worked. {0}".format(json.dumps(json_response, indent=4, sort_keys=True)))
    else:
        print("[!]request failed".format(resp.status_code))
