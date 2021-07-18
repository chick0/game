from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = ""
event_id = __name__


def start():
    print_title(title=title)
    return None
