import requests
from behave import *

from utilities.resources import *
from utilities.configuration import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


@given('I have login and auth credentials')
def step_impl(context):
    context.url = getconfig()['GITHUB']['endpoint'] + resources.github_user
    context.auth = ('vishnu93tr', '11382e75f93600561c544e91e0e2d751c7054739')


@when('user get contract is hit')
def step_impl(context):
    context.response = requests.get(context.url, auth=context.auth, verify=False)


@then('check contract is returning {statuscode:d}')
def step_impl(context, statuscode):
    assert context.response.status_code == statuscode

