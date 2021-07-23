def get():
    from .. import VALUE

    time = 0
    for i in VALUE['event'].values():
        time += i

    return time / 10


def check():
    from .. import MAX_TIME
    from ..event import print_message
    from . import player

    if MAX_TIME < get():
        for text in [
            "45분이 되었습니다.",
            "당신의 욕심이 당신의 목숨을 가져갈 시간이 되었습니다.",
            "비행기가 날라오는 소리가 들리며 하늘에 떠있는 점이 점점 커집니다."
        ]:
            print_message(text=text)

        player.dead()
