from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "식당 냉장고"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    choice = random.choice(['a', 'b'])
    if choice == "a":
        print_message(text="냉장고에서 생수를 발견했다.")
        item.get(["생수"] * random.choice([1, 1, 1, 2, 2, 3]))
    else:
        print_message(text="토마토 수프를 발견했다.")
        item.get(["토마토 수프"])

    return
