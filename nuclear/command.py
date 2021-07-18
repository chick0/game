def show_inventory():
    """
    플레이어의 인벤토리를 확인하는 명령어
    """
    from . import VALUE
    print("[플레이어의 인벤토리]")
    for n, i in VALUE['items'].items():
        print(f"  {n}: {i}개")


def load():
    """
    게임의 진행상황을 불러오는 명령어
    """
    from os import path
    from json import load

    from . import FLAG
    from . import VALUE

    filename = input("[?].json : ") + ".json"
    try:
        json = load(
            fp=open(path.join(path.dirname(path.dirname(__file__)), filename), mode="r", encoding="utf8")
        )

        for i in range(0, len(FLAG)):
            del FLAG[list(FLAG.keys())[0]]
        FLAG.update(json['flag'])

        for i in range(0, len(VALUE)):
            del VALUE[list(VALUE.keys())[0]]
        VALUE.update(json['value'])

        print(f"** 게임을 불러왔습니다 : {filename} **")
    except (FileNotFoundError, Exception) as e:
        print(f"** 게임을 불러오지 못함:{e.__class__.__name__} **")
        print(e)


def save():
    """
    게임의 진행상황을 저장하는 명령어
    """
    from os import path
    from os import urandom
    from json import dump

    from . import FLAG
    from . import VALUE

    filename = urandom(2).hex() + ".json"
    dump(
        obj={
            "flag": FLAG,
            "value": VALUE
        },
        fp=open(path.join(path.dirname(path.dirname(__file__)), filename), mode="w", encoding="utf8")
    )
    print(f"** 게임이 저장되었습니다 : {filename} **")


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

    "save": save,
    "load": load,

    "debug": debug
}
