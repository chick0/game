from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "2층 창고"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    for text in [
        "창고에서 1곳을 조사할 수 있다."
    ]:
        print_message(text=text)

    choice = player.choice(["왼쪽 선반", "오른쪽 선반"])
    if choice == "왼쪽 선반":
        print_message(text="사탕 무더기를 발견했다.")
        item.get(["사탕"] * 6)

    if choice == "오른쪽 선반":
        print_message(text="물티슈 무더기를 발견했다.")
        item.get(["물티슈"] * 6)

    return None
