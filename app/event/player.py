def choice(list_of_choice):
    def get_index(prompt: str = ""):
        try:
            tmp = int(input(prompt)) - 1

            if 0 <= tmp <= len(list_of_choice) - 1:
                return tmp
        except (ValueError, IndexError):
            pass

        return get_index(prompt)

    for i, x in enumerate(list_of_choice):
        print(f"[{i+1}] : {x}")

    return list_of_choice[get_index(">>> ")]
