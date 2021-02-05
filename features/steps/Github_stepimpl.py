import requests
from behave import *

from utilities.resources import *
from utilities.configuration import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


@given('I have github auth credentials')
def step_impl(context):
    context.url = getconfig()['GITHUB']['endpoint'] + resources.github_repos
    context.session = requests.session()
    context.session.auth = context.auth = ('vishnu93tr', '11382e75f93600561c544e91e0e2d751c7054739')


@when('github repo get contract is hit')
def step_impl(context):
    context.response = context.session.get(context.url, verify=False)


@then('check contract is returning {statuscode:d}')
def step_impl(context, statuscode):
    assert context.response.status_code == statuscode
