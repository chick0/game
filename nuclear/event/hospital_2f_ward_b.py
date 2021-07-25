from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 2층 입원실 B"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    for text in [
        "비어있는 병실에서 아무것도 찾을 수 없습니다.",
        "심지어 8인실인데도 어떤 물건도 남아있지 않습니다.",
        "당신보다 이 입원실에 빨리 온 사람이 있었나 봅니다.",
        "벽 구석에 작은 낙서가 적혀있습니다..",
        '"우리는 왜 휴게실이 없을까?"',
        "그 옆에 다른 글씨체가 답장을 적었습니다.",
        '"그러게요..."'
    ]:
        print_message(text=text)

    return None
