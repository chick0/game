
from nuclear import command


def choice(list_of_choice):
    def get_index(prompt: str = ""):
        tmp = input(prompt).strip()
        try:
            tmp = int(tmp) - 1

            if 0 <= tmp <= len(list_of_choice) - 1:
                return tmp
        except (ValueError, IndexError):
            if tmp in command.__command__.keys():
                command.__command__[tmp]()
            else:
                print("알 수 없는 명령어 입니다. 'help' 명령어를 사용해 사용할 수 있는 명령어를 확인하세요.")

        return get_index(prompt)

    for i, x in enumerate(list_of_choice):
        print(f"[{i+1}] : {x}")

    return list_of_choice[get_index(">>> ")]


def dead():
    from sys import exit
    from .. import VALUE
    from ..items import items
    from ..event import print_title
    from ..event import print_message

    print_title(title="플레이어가 죽었습니다")

    event_score = len(VALUE['event'].keys())
    item_score = 0
    for n, i in VALUE['items'].items():
        item_score += items[n]['score'] * i

    print_title(title="플레이어의 점수")
    for text in [
        f"이벤트 점수 : {event_score}",
        f"아이템 점수 : {item_score}",
        f"= 종합 점수 : {event_score + item_score}"
    ]:
        print_message(text=text, no_wait=True)

    exit(0)
