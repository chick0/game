def get(name):
    module, func = name.split(".")
    return getattr(getattr(getattr(__import__(f"app.event.{module}"), "event"), module), func)
