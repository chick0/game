
from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "1층 주방"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    for text in [
        "주방에서 1곳을 조사할 수 있다."
    ]:
        print_message(text=text)

    select = player.choice(["싱크대", "냉장고", "휴지통", "찻장"])
    if select == "싱크대":
        type_ = random.choice(['a', 'b', 'c', 'd'])
        if type_ == "a":
            print_message(text="설거지가 끝난 후라이팬을 발견했다.")
            item.get(["후라이팬"])
        if type_ == "b":
            print_message(text="설거지 할 때 사용하는 비누를 발견했다.")
            item.get(["비누"])
        if type_ == "c":
            print_message(text="차를 마실때 사용하는 주전자를 발견했다.")
            item.get(["주전자"])
        if type_ == "d":
            print_message(text="설거지하고 손에 묻은 물을 닦을때 쓰는 수건이 걸려있다.")
            item.get(["수건"])

    if select == "냉장고":
        type_ = random.choice(['a', 'b', 'c', 'd'])
        if type_ == "a":
            print_message(text="냉장보관이 필요없는 사탕을 발견했다.")
            item.get(["사탕"] * 5)
        if type_ == "b":
            print_message(text="홈쇼핑으로 구매한 토마토 수프를 발견했다.")
            item.get(["토마토 수프"] * 2)
        if type_ == "c":
            print_message(text="창고형 마트에서 대량 구매한 토마토 수프가 6개를 발견했다.")
            item.get(["토마토 수프"] * 6)
        if type_ == "d":
            print_message(text="정수기 고장을 대비해서 사놓은 생수를 발견했다.")
            item.get(["생수"] * 4)

    if select == "휴지통":
        print_message(text="라면봉지 사이에 숨어있는 사탕 3개를 발견했다...")
        item.get(["사탕"] * 3)

    if select == "찻장":
        print_message(text="무거워서 자주 사용하지 않은 주전자를 발견했다.")
        item.get(["주전자"])
