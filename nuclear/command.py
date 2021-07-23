def show_inventory():
    """
    플레이어의 인벤토리를 확인하는 명령어
    """
    from . import VALUE
    from .event import print_title
    from .event import print_message
    print_title(title="플레이어의 인벤토리", no_warp=True)
    for n, i in VALUE['items'].items():
        print_message(text=f"{n}: {i}개", no_wait=True)


def help_():
    """
    사용가능한 명령어를 보여주는 명령어
    """
    for key in __command__.keys():
        print(key, __command__[key].__doc__)


def debug():
    """
    [개발용] 변수를 확인하는 명령어
    """
    from . import FLAG
    from . import VALUE
    print(FLAG)
    print(VALUE)


__command__ = {
    "e": show_inventory,

    "help": help_,

    "debug": debug
}
