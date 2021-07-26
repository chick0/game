
from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "컨테이너 집 침대"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        print_message(text="침대를 더 조사하기에는 시간이 부족합니다.")
        return
    else:
        flag.update(event_id, True)

    type_ = random.choice(['a', 'b', 'c', 'd'])
    if type_ == "a":
        print_message(text="곰돌이 인형을 발견했다.")
        item.get(["인형"])
    if type_ == "b":
        print_message(text="귀여운 너구리 인형을 발견했다.")
        item.get(["인형"])
    if type_ == "c":
        print_message(text="멍하게 생긴 판다 인형을 발견했다.")
        item.get(["인형"])
    if type_ == "d":
        print_message(text="목욕용 오리 인형을 발견했다...")
        item.get(["인형"])

    return None
