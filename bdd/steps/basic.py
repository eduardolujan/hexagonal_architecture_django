

import requests
from environ import Env as get_env
from behave import given, when, then


def get_host():
    env = get_env()
    local_debug = env.bool('LOCAL_DEBUG')
    if local_debug:
        host = f'http://localhost:8000'

@given('we have health check to test if the application is running')
def we_have_health_check(context):
    requests.get("")


@when('we implement a test')
def step_impl(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
