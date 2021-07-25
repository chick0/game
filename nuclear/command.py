def show_inventory():
    """
    플레이어의 인벤토리를 확인하는 명령어
    """
    from . import VALUE
    print("[ 플레이어의 인벤토리 ]")
    for n, i in VALUE['items'].items():
        print(f"- {n}: {i}개")


def item():
    """
    아이템의 세부정보를 확인하는 명령어
    """
    from . import VALUE
    from .items import items
    from .handler import player

    keys = list(VALUE['items'].keys())
    if len(keys) >= 1:
        print("[ 세부정보를 확인하고 싶은 아이템을 선택해주세요 ]")

        key = player.choice(keys)
        print(f"{key}: {items[key]['explain']}")
    else:
        print("보유하고 있는 아이템이 없습니다.")


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
    "i": item,

    "help": help_,

    "debug": debug
}
