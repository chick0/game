from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 2층 입원실 A"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        print_message(text="도어락이 반응하지 않습니다.")
        return
    else:
        flag.update(event_id, True)

    for text in [
        "문에는 전자식 도어락이 달려있습니다.",
        "문에는 간단한 메모가 붙어있습니다.",
        '"사생활 보호를 위해 잠겨있습니다."',
        "당신은 이 문을 무시하거나 비밀번호를 찍어볼 수 있습니다."
    ]:
        print_message(text=text)

    password = player.choice([1234, 2458, 8520, 8282])
    if password == 8282:
        for text in [
            "'삐리릭' 하는 소리와 함께 도어락이 열립니다.",
            "입원실에는 간호사의 옷이 있습니다.",
            "직원휴게실이 없는 간호사를 위해 4인용 병실을 개조한 것 같습니다.",
            "그래도 당신은 구급상자와 약을 발견했습니다.",
        ]:
            print_message(text=text)

        item.get(["구급상자", "약"])

    print_message(text="갑자기 '삐삐' 하는 소리와 갑자기 도어락이 꺼집니다.")
    print_message(text="도어락의 배터리 수명이 다한 것 같습니다.")
    return None
