from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 1층 화장실"
event_id = __name__


def start():
    print_title(title=title)
    for text in [
        "소독약품 냄새와 배설물 냄새와 방향제 냄새가 섞여있는 화장실이 당신을 반깁니다.",
        "반가움도 잠시 역겨운 냄새를 느낀 당신은 서둘러 화장실에서 도망칩니다.",
    ]:
        print_message(text=text)

    return None
