from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "교회"
event_id = __name__


def type_a():
    for text in [
        "교회에 도착한 당신은 공포심을 느낍니다.",
        "구원과 생존을 위한 기도가 교회를 가득 채웁니다.",
        "당신의 눈에서 눈물이 흐르기 시작합니다.",
        "그 기도 소리를 들으며 당신도 기도를 시작합니다.",
        "끝을 알 수 없는 기도는 핵이 터질 때 까지 반복되었습니다.",
    ]:
        print_message(text=text)

    player.dead()


def type_b():
    for text in [
        "교회에 도착한 당신은 공포심을 느낍니다.",
        "구원과 생존을 위한 기도가 교회를 가득 채웁니다.",
        "당신은 그 기도 소리에서 광기를 느낍니다.",
        "당신은 교회에서 도망칩니다.",
    ]:
        print_message(text=text)


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        print_message(text="이 교회에 다시 들어가고 싶지 않습니다.")
        return None
    else:
        flag.update(event_id, True)

    random.choice([type_a, type_b, type_b, type_b, type_b, type_b])()
    return None
