import demo_lambda


def test_failed_send_cake_recipe(mocker):
    print("[*]Patching")
    mocker.patch('demo_lambda.send_cake_recipe', return_value=False)
    assert demo_lambda.send_cake_recipe() is False


def test_live_send_cake_recipe():
    assert demo_lambda.send_cake_recipe() is True


def test_get_environment_variable():
    assert demo_lambda.get_secret_ingrediant() in 'chocolate'
