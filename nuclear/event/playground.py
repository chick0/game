from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "놀이터"
event_id = __name__


def type_a():
    print_message(text="놀이터에는 모래먼지만 남아있을뿐 아무것도 남아있지 않습니다.")


def type_b():
    print_message(text="놀이터의 주인인 아이들은 없고 사탕 몇개만 남아있습니다.")
    item.get(["사탕"] * random.choice([2, 2, 3, 3, 3, 4, 5, 6]))


def type_c():
    print_message(text="놀이터에 있는 아이가 당신에게 선물을 줍니다.")
    item.get([random.choice(["사탕", "비누", "책", "인형", "수건"])])


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    random.choice([type_a, type_a, type_b, type_b, type_b, type_c])()

    return None
