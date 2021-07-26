
from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "컨테이너 집 창문"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        print_message(text="창문을 더 조사하기에는 시간이 부족합니다.")
        return
    else:
        flag.update(event_id, True)

    for text in [
        "군부대에서 헬리콥터를 이용해 군인을 지역 밖으로 이동시키고 있다.",
        "군부대의 닫힌 문에 사람들이 모이기 시작한다.",
        "갑자기 문이 열리고 사람들을 안으로 들여보내기 시작했다.",
        "그리고 그 사람들은 헬리콥터를 타고 마을을 빠져나가기 시작했다.",
    ]:
        print_message(text=text)

    # 군부대 항의 / 다른 사람들은 헬리콥터를 탔음
    flag.update("military.resident-helicopter", True)
    return None
