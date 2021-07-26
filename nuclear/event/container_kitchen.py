
from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "컨테이너 집 싱크대"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        print_message(text="싱크대를 더 조사하기에는 시간이 부족합니다.")
        return
    else:
        flag.update(event_id, True)

    print_message(text="싱크대에는 내가 먹은 토마토 수프 통조림과 먹지 않은 통조림이 몇개 남아있다.")
    print_message(text="그리고 옆에 있는 생수도 몇개 챙겼다.")
    item.get(["토마토 수프"] * random.choice([2, 3, 3, 3, 4, 4, 4, 5, 5, 6]))
    item.get(["생수"] * random.choice([3, 3, 3, 4, 5]))
    return None
