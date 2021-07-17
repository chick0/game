
from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "1층 화장실"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    for text in [
        "화장실에서 1곳을 조사할 수 있다."
    ]:
        print_message(text=text)

    select = player.choice(["수납장", "욕조"])
    if select == "수납장":
        type_ = random.choice(['a', 'b', 'c', 'd'])
        if type_ == "a":
            print_message(text="다른 화장품 없이 오직 로션만 덩그러니 놓여있다.")
            item.get(["로션"])
        if type_ == "b":
            print_message(text="사탕과 로션이 놓여있다.")
            item.get(["사탕", "로션"])
        if type_ == "c":
            print_message(text="변기에서 사용할 수 없는 물티슈가 놓여있다.")
            item.get(["물티슈"])
        if type_ == "d":
            print_message(text="목욕후 마시려고 가져다 둔 생수가 놓여있다.")
            item.get(["생수"])

    if select == "욕조":
        type_ = random.choice(['a', 'b', 'c', 'd'])
        if type_ == "a":
            print_message(text="목욕용 오리 인형을 발견했다.")
            item.get(["인형"])
        if type_ == "b":
            print_message(text="비누만 덩그러니 남아있다.")
            item.get(["비누"])
        if type_ == "c":
            print_message(text="갑자기 뒤를 돌아보게 만드는 비누가 놓여있다.")
            item.get(["비누"])
        if type_ == "d":
            print_message(text="두툼한 수건이 욕조에 걸려있다.")
            item.get(["수건"])
