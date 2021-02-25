# Demo AWS Lambda with CircleCI

Simple `Python` script that sends a cake recipe to `httpbin.org`.

The server echos back the recipe.

It is single `HTTP Post` request with a single `environment variable`.

### Unit Tests
When testing locally, instead of running from `terminal`, you can add a `New Configuration` in `PyCharm`.

This is a simple way to pass in `Environment Variables`.


![](.README_images/pycharm_new_pytest_config.png)