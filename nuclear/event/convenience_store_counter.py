from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "편의점 계산대"
event_id = __name__


def type_a():
    for text in [
        "당신은 POS 기계를 뜯어낼정도로 강하지 않습니다.",
        "대신 당신은 생수를 챙깁니다.",
    ]:
        print_message(text=text)
    item.get(["생수"])


def type_b():
    for text in [
        "당신은 POS 기계를 해킹할 정도로 똑똑하지 않습니다.",
        "대신 당신은 사탕을 챙깁니다.",
    ]:
        print_message(text=text)
    item.get(["사탕"])


def type_c():
    for text in [
        "누군가 이 편의점의 POS 기계를 훔쳐 당신은 아무것도 하지 못합니다.",
    ]:
        print_message(text=text)


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    random.choice([type_a, type_b, type_c])()
    return None
