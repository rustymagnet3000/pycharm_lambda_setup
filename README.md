# Demo AWS Lambda with CircleCI

Simple `Python` script that sends a cake recipe to `httpbin.org`.

The server echos back the recipe.

It is single `HTTP Post` request with a single `environment variable`.

### Unit Tests
When testing locally, instead of running from `terminal`, you can add a `New Configuration` in `PyCharm`.

This is a simple way to pass in `Environment Variables`.


![](.README_images/pycharm_new_pytest_config.png)


### Build with CircleCI

```bash
circleci local execute -c process.yml --job build-and-test

circleci local execute -c process.yml --job build-and-test -e SECRET_SAUCE=chocolate
```

### AWS Command Line
```bash
aws iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json
```