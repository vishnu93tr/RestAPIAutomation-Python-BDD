import requests
from behave import *

from Payload import *
from utilities.resources import *
from utilities.configuration import *

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


@given('The {userid} of todo in path param')
def step_impl(context, userid):
    context.url = getconfig()['API']['endpoint'] + resources.todo_list + '/' + userid
    context.headers = headers()
    context.user_id = userid


@when('todo GET contract is executed')
def step_impl(context):
    context.response = requests.get(context.url, headers=context.headers, verify=False)


@then('Todo list is successfully displayed')
def step_impl(context):
    print(context.response.json())
    assert context.response.json()['id'] == int(context.user_id)


@then('check contract is returning {statuscode:d}')
def step_impl(context, statuscode):
    assert context.response.status_code == statuscode
