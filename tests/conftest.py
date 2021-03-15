import os


# override pytest_generate_tests to set ENV variable
def pytest_generate_tests(metafunc):
    os.environ['SECRET_SAUCE'] = 'chocolate'

