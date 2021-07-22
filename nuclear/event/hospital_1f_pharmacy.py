from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "병원 1층 약국"
event_id = __name__


def left():
    for text in [
        "당신은 왼쪽 서랍을 뒤지기 시작합니다.",
        "그것도 잠시 누군가가 당신을 뒤로 밀쳐냅니다.",
        "당신은 뒤로 넘어집니다.",
        "은색과 붉은색이 보이는 깡통이 당신의 머리로 날아옵니다.",
        "당신은 그 물건을 피하거나 잡을 수 있습니다."
    ]:
        print_message(text=text)

    choice = player.choice(["잡는다", "피한다"])
    if choice == "잡는다":
        success = True if random.choice([0, 0, 1, 1, 1]) == 0 else False
        if success:
            print_message(text="당신의 놀라운 순발력으로 날아오는 물건을 잡았습니다.")
            print_message(text="날아온 물건은 토마토 수프였습니다.")
            item.get(["토마토 수프"])
        else:
            for text in [
                "당신의 손보다 깡통이 더 빨랐습니다.",
                "당신은 정신이 희미해집니다.",
                "누군가가 당신을 향해 다가오는 느낌이 듭니다.",
            ]:
                print_message(text=text)

            print_message(text="당신은 쓰러지려하는 정신을 붙잡아야 합니다.")
            choice = player.choice(["저항한다", "포기한다"])
            if choice == "저항한다":
                for text in [
                    "비틀거리는 몸을 억지로 일으키자 당신에게 다가오는 습격자는 당신을 피해 지나갑니다.",
                    "당신에게 날라온 물건을 발견했습니다.",
                    "토마토 수프를 줍고 당신은 약국에서 도망치듯 나갑니다."
                ]:
                    print_message(text=text)

                item.get(["토마토 수프"])
            else:
                for text in [
                    "누군가가 당신을 강하게 강타합니다.",
                    "희미한 의식은 더 이상 돌아올 일이 없습니다.",
                ]:
                    print_message(text=text)

                player.dead()
    else:
        print_message(text="날아온 물건을 확인하지도 않고 당신은 약국에서 도망칩니다.")


def right():
    for text in [
        "당신은 오른쪽 서랍을 뒤지기 시작합니다.",
        "서랍안에 남아있는 것은 비어있는 약봉투만 보입니다."
    ]:
        print_message(text=text)

    choice = random.choice(['a', 'b', 'b'])
    if choice == "a":
        for text in [
            "그래도 서랍 구석에 약이 하나 남아있었습니다.",
        ]:
            print_message(text=text)

        item.get(["약"] * 3)


def counter():
    for text in [
        "당신은 접수 창구를 뒤지기 시작합니다.",
        "필요한 약은 보이지 않고 처방전만 보입니다.",
        "그래도 당신은 어린이들을 위한 사탕을 발견합니다."
    ]:
        print_message(text=text)
    item.get(["사탕"])


def trash():
    for text in [
        "쓰레기 통에는 별다른 물건이 없었습니다.",
        "누군가가 먹은 쌍화탕과 비타민 음료의 유리 병만 있을 뿐 입니다.",
        "그래도 당신은 쓰레기 통 구석에 있는 사탕을 발견했습니다."
    ]:
        print_message(text=text)
    item.get(["사탕"] * 2)


def door():
    for text in [
        "당신은 옆문을 열고 들어갔습니다.",
        "옆문을 열고 도착한 곳은 병원 밖이었습니다."
    ]:
        print_message(text=text)

    return "street_no2"


def back():
    for text in [
        "당신은 약이 급하지 않다고 생각해서 약국에서 나기기로 결정합니다."
    ]:
        print_message(text=text)


def start():
    print_title(title=title)
    if flag.check(event_id, True):
        return
    else:
        flag.update(event_id, True)

    for text in [
        "약이 급한 사람들이 약을 챙기기 위해 약국을 뒤집어 놓았다.",
        "사람들은 여전히 필요한 약을 찾기 위해 돌아다니고 있습니다.",
        "당신은 저 사람들 사이에 들어가서 약을 찾거나 약국에서 나갈 수 있습니다.",
        "하지만 다시 이 약국으로 돌아올 수 없습니다."
    ]:
        print_message(text=text)

    ev_map = {
        "왼쪽 서랍": left,
        "오른쪽 서랍": right,
        "접수 창구": counter,
        "쓰레기 통": trash,
        "약국 옆문": door,
        "돌아가기": back
    }

    return ev_map[player.choice(list(ev_map.keys()))]()
