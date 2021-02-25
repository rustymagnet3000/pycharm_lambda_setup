import main


def test_failed_send_cake_recipe(mocker):
    print("[*]Patching")
    mocker.patch('main.send_cake_recipe', return_value=False)
    assert main.send_cake_recipe() is False


def test_live_send_cake_recipe():
    assert main.send_cake_recipe() is True


def test_get_environment_variable():
    assert main.get_secret_ingrediant() in 'chocolate'
