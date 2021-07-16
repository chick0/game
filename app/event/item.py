
from app import VALUE


def get(item_name):
    for this in item_name:
        print(f"+1 {this}")
        try:
            VALUE['items'][this] += 1
        except KeyError:
            VALUE['items'][this] = 1


def use(item_name):
    # TODO: 인벤토리에 아이템 삭제
    for this in item_name:
        print(f"-1 {item_name}")
    return


def need(item_name_list):
    # TODO: 모든 아이템이 인벤토리에 있는지 확인
    return
