import random
import string


def addBook(title, body1, userid):
    body = {

        "title": title,
        "body": body1,
        "userId": userid

    }
    return body


def headers():
    header = {
        "Content-Type": "application/json"
    }
    return header
