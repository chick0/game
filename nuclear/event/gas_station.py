from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "주유소"
event_id = __name__


def type_a():
    check = flag.get(f"{event_id}:type_a:used")
    if check is None:
        flag.update(f"{event_id}:type_a:used", 1)
    else:
        flag.update(f"{event_id}:type_a:used", check + 1)
        if check >= 2:
            print_message(text="당신은 이 주유소를 더 이상 조사 할 수 없습니다.")
            return "street_no1"

    for text in [
        "시끄러운 주유소에 도착했습니다.",
        "자신의 차에 기름을 채우기 위해 서로 싸우는 사람들이 보입니다.",
        "당신은 주유소에서 2번 조사 할 수 있습니다.",
    ]:
        print_message(text=text)

    choice = player.choice(["주유기", "사무실", "세차장", "하수구", "1번가로 돌아가기"])

    if choice == "주유기":
        print_message(text="어떻게든 기름을 가져가기 위한 사람들로 인해 아무것도 하지 못했습니다.")

    if choice == "사무실":
        print_message(text="사무실의 철문에는 다급한 사람들이 몰려있습니다.")
        print_message(text="그 사람들한테 밀려 당신은 아무것도 찾을 수 없었습니다.")

    if choice == "세차장":
        if flag.check(f"{event_id}:event:c", True):
            return
        else:
            flag.update(f"{event_id}:event:c", True)
            choice = random.choice(['a', 'a', 'a', 'a', 'b', 'b'])
            if choice == "a":
                print_message(text="아무것도 발견하지 못했다.")
            if choice == "b":
                print_message(text="직원들을 위한 생수를 발견했다.")
                item.get(["생수"] * 2)

    if choice == "하수구":
        if flag.check(f"{event_id}:event:d", True):
            return
        else:
            flag.update(f"{event_id}:event:d", True)

        print_message(text="버려진 물티슈를 발견했다.")
        item.get(["물티슈"] * 2)

    if choice == "1번가로 돌아가기":
        return "street_no1"

    return None


def type_b():
    for text in [
        "조용한 주유소에 도착했습니다.",
        "무서울 정도로 조용한 주유소에서 당신은 공포를 느낌니다.",
    ]:
        print_message(text=text)

    choice = player.choice(["주유기", "사무실", "세차장", "하수구", "1번가로 돌아가기"])

    if choice == "주유기":
        print_message(text="피자국 마저 보이는 주유기에서 아무것도 찾지 못했습니다.")

    if choice == "사무실":
        print_message(text="살짝 찌그러진 철문이 단단함을 자랑하고 있습니다.")
        print_message(text="아무것도 찾을 수 없습니다.")

    if choice == "세차장":
        if flag.check(f"{event_id}:event:c", True):
            return
        else:
            flag.update(f"{event_id}:event:c", True)

        print_message(text="직원들을 위한 생수를 발견했다.")
        item.get(["생수"] * 2)

    if choice == "하수구":
        if flag.check(f"{event_id}:event:d", True):
            return
        else:
            flag.update(f"{event_id}:event:d", True)

        print_message(text="버려진 물티슈를 발견했다.")
        item.get(["물티슈"] * 2)

    if choice == "1번가로 돌아가기":
        return "street_no1"

    return None


def start():
    print_title(title=title)

    ev_map = {
        "a": type_a,
        "b": type_b,
    }

    event_type = flag.get(f"{event_id}:event_type")
    if event_type is None:
        event_type = random.choice(["a", "b"])
        flag.update(f"{event_id}:event_type", event_type)

    next_event_id = ev_map[event_type]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
