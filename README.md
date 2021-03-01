# A Python AWS Lambda

A simple `Python` handler that sends a cake recipe to `httpbin.org`.  The server echos back the recipe. 

It is single `HTTP Post` request with a single `environment variable`.

### Run Lambda from within PyCharm

You can configure `PyCharm` in almost anyway you want with `plug-ins`. I chose to have different configurations that could:

1. run locally ( thanks to `python-lambda-local` )
2. Deploy to local `Docker` container
3. run just unit tests ( like `CircleCI` )
4. Deploy to `AWS Lambda`
     

![](.README_images/pycharm_config_options.png)

### Continuous Integration

The repo pushes to `github`.  It is configured to auto-build on `CircleCI`, when you push code changes.
All the `CircleCI` setup locally can be tested locally.
  

- Pass in `export SECRET_SAUCE="chocolate"`



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


### Deploy to AWS Lambda

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


