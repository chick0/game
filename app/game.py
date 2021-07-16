from time import sleep

from app.event import get_event


def print_line(message: str):
    print("  " + message)
    sleep(0.65)


def start(story, item):
    next_event(
        event_id=get_event("random.choice")(story['start']),
        story=story,
        item=item
    )
    print("game end!")


def next_event(event_id, story, item, back=None):
    event = story['event'][event_id]

    print(f"\n\n\n[ {event['name']} ]")
    for line in event['message']:
        if isinstance(line, str):
            print_line(line)
        elif isinstance(line, dict):
            if "event_id" in line.keys():
                ev_map = {}
                for ev_id in line.get("event_id"):
                    ev_map[story['event'][ev_id]['name']] = ev_id

                next_event(
                    event_id=ev_map[get_event(line.get("type"))(list(ev_map.keys()))],
                    story=story,
                    item=item,
                    back=event_id
                )

            elif "event" in line.keys():
                next_event(
                    event_id=no_event(
                        event_id=back,
                        event=line['event'][get_event(line.get("type"))(list(line.get("event").keys()))],
                        story=story,
                        item=item
                    ),
                    story=story,
                    item=item,
                    back=event_id
                )

            raise ValueError("유효한 변수가 없습니다")


def no_event(event_id, event, story, item):
    ev_type = event['type']
    if ev_type == "item.get":
        get_event(ev_type)(event['item'])

    for line in event['message']:
        if isinstance(line, str):
            print_line(line)

    return event_id
