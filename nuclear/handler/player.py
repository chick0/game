
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
    print("[플레이어가 죽었습니다]")

    from ..command import show_inventory
    show_inventory()

    # TODO: 도전과제

    exit(0)
