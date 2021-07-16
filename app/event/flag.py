
from app import FLAG


def get(key):
    return FLAG.get(key, None)


def update(key, value):
    return FLAG.update({key: value})


def check(key, pass_value):
    return pass_value == FLAG.get(key, None)
