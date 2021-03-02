# A simple AWS Lambda with PyCharm

A simple `Python` handler that sends a cake recipe to `httpbin.org`.  The server echos back the recipe. 

It is single `HTTP Post` request with a single `environment variable`.

### Run Lambda from within PyCharm

You can configure `PyCharm` in almost anyway with `plug-ins`:

<!-- TOC depthfrom:2 depthto:2 withlinks:true updateonsave:true orderedlist:false -->

- [Run lambda locally from command line](#run-lambda-locally-from-command-line)
- [Run Unit Tests locally](#run-unit-tests-locally)
- [Run as local lambda](#run-as-local-lambda)
- [Build locally with CircleCI](#build-locally-with-circleci)
- [Deploy to AWS Lambda from command line](#deploy-to-aws-lambda-from-command-line)

<!-- /TOC -->

After setting up new `configurations` my final `PyCharm` setup was:

![config_options](.README_images/pycharm_config_options.png)

## Run lambda locally from command line

```bash
pip3 install python-lambda-local
python-lambda-local -f rm_handler demo_lambda.py inputs.json
```

To enabled `control + r` to run the configuration, follow this AWS article:

### Run locally inside a `Docker` container

Run lambda locally within PyCharm, inside Docker Container
Install the `plug-in`:

![plug-in-preferences](.README_images/plug-in.png)

Then - assuming you have `Docker Desktop` installed, you just need to setup a new `configuration` in `PyCharm`:

![docker-setup](.README_images/pycharm_docker.png)

Then specify that you want to run function inside a container:

![container-step](.README_images/765e0c94.png)

## Run Unit Tests locally

When testing locally, instead of running from `terminal`, you can add a `New Configuration` in `PyCharm`.

This is a simple way to pass in `Environment Variables` and checks `Unit Tests` before passing to `CircleCI`.

![](.README_images/pycharm_new_pytest_config.png)

## Run as local `lambda`

<https://medium.com/@bezdelev/how-to-test-a-python-aws-lambda-function-locally-with-pycharm-run-configurations-6de8efc4b206>


## Build locally with CircleCI

The repo pushed to `github`.  It was configured to auto-build on `CircleCI`, when you pushed code changes.
All the `CircleCI` setup locally could be tested locally.
  
```bash
circleci config process .circleci/config.yml > process.yml
circleci local execute -c process.yml --job build-and-test -e SECRET_SAUCE=chocolate
```

## Deploy to `AWS Lambda` from command line

#### Create

```bash
aws lambda create-function \
    --function-name MyPyLambdaFunction \
    --runtime python3.7 \
    --zip-file fileb://my-deployment-package.zip \
    --handler demo_lambda.rm_handler \
    --role arn:aws:iam::XXXXXXXXX:role/rm-lambda-demo-role
```

#### Zip up code and dependencies

```bash
pip3 install -r requirements.txt --target ./package
cd package
zip -r ../my-deployment-package.zip .
cd ..
zip -g my-deployment-package.zip demo_lambda.py
```

#### Update

Code change:

`zip -g my-deployment-package.zip demo_lambda.py`

Then upload:

```bash
aws lambda update-function-code \
    --function-name  MyPyLambdaFunction \
    --zip-file fileb://my-deployment-package.zip
```

### Invoke

```bash
aws lambda invoke out.txt \
    --function-name MyPyLambdaFunction \
    --log-type Tail \
    --query 'LogResult' \
    --output text |  base64 -d
```
