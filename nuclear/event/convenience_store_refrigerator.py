from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "편의점 냉장고"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    choice = random.choice(['a', 'a', 'a',
                            'b', 'b', 'b', 'b',
                            'c', 'c',
                            'd'])

    if choice == "a":
        print_message(text="생수를 발견했다.")
        item.get(["생수"] * 2)

    elif choice == "b":
        print_message(text="토마토 수프를 발견했다.")
        item.get(["토마토 수프"])

    elif choice == "c":
        print_message(text="사탕을 발견했다.")
        item.get(["사탕"])

    elif choice == "d":
        print_message(text="비누를 발견했다......")
        item.get(["비누"])

    return None
