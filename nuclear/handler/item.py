
from nuclear import VALUE
from nuclear.items import items


def get(item_name: list):
    for this in item_name:
        if this not in list(items.keys()):
            raise KeyError("등록되지 않은 아이템을 사용자의 인벤토리에 추가하려 했습니다.")

        print(f"+1 {this}")
        try:
            VALUE['items'][this] += 1
        except KeyError:
            VALUE['items'][this] = 1


def use(item_name: str) -> bool:
    if item_name in VALUE['items'].keys():
        print(f"-1 {item_name}")
        return True

    return False
