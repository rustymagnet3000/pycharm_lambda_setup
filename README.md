# A Python AWS Lambda

Simple `Python` script that sends a cake recipe to `httpbin.org`.  The server echos back the recipe. It is single `HTTP Post` request with a single `environment variable`.

The interesting piece is:

 - It builds on `CircleCI`, when you push code changes
 - You can test the lambda locally inside of PyCharm

### Run lambda locally with PyCharm

```
pip3 install python-lambda-local
python-lambda-local -f rm_handler demo_lambda.py inputs.json
```
To enabled `control + r` to run the configuration, follow this AWS article:

https://medium.com/@bezdelev/how-to-test-a-python-aws-lambda-function-locally-with-pycharm-run-configurations-6de8efc4b206


### Unit Tests
When testing locally, instead of running from `terminal`, you can add a `New Configuration` in `PyCharm`.

This is a simple way to pass in `Environment Variables`.


![](.README_images/pycharm_new_pytest_config.png)


### Build with CircleCI

```bash
circleci local execute -c process.yml --job build-and-test

circleci local execute -c process.yml --job build-and-test -e SECRET_SAUCE=chocolate
```

