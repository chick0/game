
from nuclear import VALUE


def get(item_name: list):
    for this in item_name:
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
