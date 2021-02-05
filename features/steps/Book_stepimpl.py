import requests
from behave import *

from Payload import *
from utilities.resources import *
from utilities.configuration import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


@given('The book details which needed to be added to Library API with {title} and {body} and {userid}')
def step_impl(context, title, body, userid):
    context.url = getconfig()['API']['endpoint'] + resources.add_book
    context.payload = addBook(title, body, userid)
    context.headers = headers()


@when('The AddBook post contract is executed')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers, verify=False)


@then('Book is successfully Added')
def step_impl(context):
    print(context.response.json())
    assert context.response.status_code == 201
