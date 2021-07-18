
from . import print_title
from . import print_message
from nuclear.handler import *


# metadata
title = "작지만 잡동사니가 가득한 집"
event_id = __name__


def start():
    print_title(title=title)

    for text in [
        "당신은 작지만 잡동사니가 가득한 집에 있습니다.",
        "갑자기 당신 앞에 있는 TV 에서 나오는 프로그램이 중단되고 갑자기 긴급 속보가 방송되기 시작합니다.",
        "45분뒤 핵이 당신이 살고있는 옆동네에 떨어진다고 합니다.",
        "최대한 많은 짐을 챙겨서 마침 여름 휴가를 간 옆집 철수네 지하 벙커로 도망처야 합니다.",
        "또는 이 동네에서 탈출해야 합니다.",
        ""
    ]:
        print_message(text=text)

    ev_map = {
        "1층 화장실": event.get("little_house_1f_bath"),
        "1층 주방": event.get("little_house_1f_kitchen"),
        "2층 내방": event.get("little_house_2f_room"),
        "2층 창고": event.get("little_house_2f_storage"),
        "1번가 (이 집을 다시 조사 할 수 없음)": event.get("street_no1")
    }

    next_event_id = ev_map[player.choice(list(ev_map.keys()))]()
    if next_event_id is None:
        start()
    else:
        event.get(next_event_id)()
