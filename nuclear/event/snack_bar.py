from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "식당"
event_id = __name__


def start():
    print_title(title=title)
    if flag.check(event_id, "burn"):
        print_message(text="이 식당은 불타고 있어 조사가 불가능합니다.")
        return "street_no1"

    for text in [
        "당신은 아무도 없는 조용한 식당에 도착했습니다.",
        "누군가가 밥을 먹었던 흔적과, 누군가 조리한 흔적만이 남아있습니다.",
    ]:
        print_message(text=text)

    ev_map = {
        "주방": event.get("snack_bar_kitchen"),
        "계산대": event.get("snack_bar_counter"),
        "냉장고": event.get("snack_bar_refrigerator"),
        "냉동창고": event.get("snack_bar_cold_storage"),
        "1번가로 돌아가기": event.get("street_no1"),
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
