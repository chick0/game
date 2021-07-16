def show_inventory():
    print("[플레이어의 인벤토리]")


def debug():
    from app import FLAG
    from app import VALUE
    print(FLAG)
    print(VALUE)


def save():
    from os import path
    from json import dump
    from new import uuid4

    from app import FLAG
    from app import VALUE
    from app import BASE_PATH

    filename = uuid4().__str__() + ".json"
    dump(
        obj={
            "flag": FLAG,
            "value": VALUE
        },
        fp=open(path.join(path.dirname(BASE_PATH), filename), mode="w", encoding="utf8")
    )
    print(f"** 게임이 저장되었습니다 : {filename} **")


__command__ = {
    "인벤토리": show_inventory,
    "inventory": show_inventory,
    "save": save,

    "debug": debug
}

# do not touch this
__all__ = [name for name in dir() if not name.startswith("_")]
# do not touch this
