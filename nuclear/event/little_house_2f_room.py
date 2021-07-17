
from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "2층 내방"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    for text in [
        "내방에서 1곳을 조사할 수 있다."
    ]:
        print_message(text=text)

    select = player.choice(["책상", "휴지통", "침대", "책장"])
    if select == "책상":
        type_ = random.choice(['a', 'b', 'c', 'd'])
        if type_ == "a":
            print_message(text="피부를 위한 로션을 발견했다.")
            item.get(["로션"])
        if type_ == "b":
            print_message(text="학원 광고가 붙어있는 물티슈를 발견했다.")
            item.get(["물티슈"])
        if type_ == "c":
            print_message(text="인터넷에서 구매한 사탕 무더기를 발견했다.")
            item.get(["사탕"] * 5)
        if type_ == "d":
            print_message(text="특별한 물건이 없다.")

    if select == "휴지통":
        type_ = random.choice(['a', 'a', 'a', 'b'])
        if type_ == "a":
            print_message(text="특별한 물건이 없다.")
        if type_ == "b":
            print_message(text="학원 광고가 붙어있는 물티슈를 발견했다.")
            item.get(["물티슈"])

    if select == "침대":
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

    if select == "책장":
        type_ = random.choice(['a', 'b'])
        if type_ == "a":
            print_message(text="과제할 때를 제외하고 사용하지 않은 사전을 발견했다.")
            item.get(["사전"])
        if type_ == "b":
            print_message(text="재밌는 소설 책을 발견했다.")
            item.get(["책"])

    return None
