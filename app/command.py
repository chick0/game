def show_inventory():
    print("[플레이어의 인벤토리]")


__command__ = {
    "인벤토리": show_inventory
}

# do not touch this
__all__ = [name for name in dir() if not name.startswith("_")]
# do not touch this
