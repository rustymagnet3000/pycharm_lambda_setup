# A Python AWS Lambda

A simple `Python` handler that sends a cake recipe to `httpbin.org`.  The server echos back the recipe. 

It is single `HTTP Post` request with a single `environment variable`.

### Interesting pieces:

- It builds on `CircleCI`, when you push code changes
- You can the `lambda` locally inside PyCharm
- You can test the `CircleCI` setup locally

### Run lambda locally from command line

```
pip3 install python-lambda-local
python-lambda-local -f rm_handler demo_lambda.py inputs.json
```
To enabled `control + r` to run the configuration, follow this AWS article:

### Run lambda locally within PyCharm

https://medium.com/@bezdelev/how-to-test-a-python-aws-lambda-function-locally-with-pycharm-run-configurations-6de8efc4b206

### Run Unit Tests locally within PyCharm

When testing locally, instead of running from `terminal`, you can add a `New Configuration` in `PyCharm`.

This is a simple way to pass in `Environment Variables` and checks `Unit Tests` before passing to `CircleCI`.


![](.README_images/pycharm_new_pytest_config.png)


### Build locally with CircleCI

```bash
circleci config process .circleci/config.yml > process.yml
circleci local execute -c process.yml --job build-and-test -e SECRET_SAUCE=chocolate
```


### Run on AWS Lambda

If it works locally, then you still have to get AWS setup mirror the local setup:

- Pass in `export SECRET_SAUCE="chocolate"`
  
- Validate it passes via the `awsCLI`


