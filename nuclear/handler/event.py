def get(name: str):
    return getattr(getattr(getattr(__import__(f"nuclear.event.{name}"), "event"), name), "start")


def get_event_id(name: str):
    return getattr(getattr(getattr(__import__(f"nuclear.event.{name}"), "event"), name), "event_id")
