
from app import command


def choice(list_of_choice):
    def get_index(prompt: str = ""):
        try:
            tmp = input(prompt)
            if tmp in command.__command__.keys():
                command.__command__[tmp]()

            tmp = int(tmp) - 1

            if 0 <= tmp <= len(list_of_choice) - 1:
                return tmp
        except (ValueError, IndexError):
            pass

        return get_index(prompt)

    for i, x in enumerate(list_of_choice):
        print(f"[{i+1}] : {x}")

    return list_of_choice[get_index(">>> ")]
