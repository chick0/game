from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "편의점 뒷문"
event_id = __name__


def type_a():
    for text in [
        "무엇인가 이상한 느낌이 당신을 경고합니다.",
        "그 이상한 느낌은 당신의 호기심보다 강해 당신은 다시 편의점으로 돌아옵니다."
    ]:
        print_message(text=text)


def type_b():
    for text in [
        "무엇인가 이상한 느낌이 당신을 경고합니다.",
        "이상한 느낌보다 당신의 호기심이 강하게 당신을 유혹합니다.",
        "당신은 뒷문을 열고 편의점 밖으로 나갑니다.",
        "그 순간 누군가 당신의 뒤통수를 후라이팬으로 강타합니다."
    ]:
        print_message(text=text)
    player.dead()


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        type_b()
    else:
        flag.update(event_id, True)
        type_a()

    return None
