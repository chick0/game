def show_inventory():
    print("[플레이어의 인벤토리]")


def debug():
    from nuclear import FLAG
    from nuclear import VALUE
    print(FLAG)
    print(VALUE)


__command__ = {
    "인벤토리": show_inventory,
    "inventory": show_inventory,

    "debug": debug
}

# do not touch this
__all__ = [name for name in dir() if not name.startswith("_")]
# do not touch this
