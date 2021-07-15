def event(list_of_choice):
    def get_index(prompt: str = ""):
        try:
            tmp = int(input(prompt))
            if 1 <= tmp <= len(list_of_choice) + 1:
                return tmp
        except ValueError:
            pass

        return get_index(prompt)

    return list_of_choice[get_index()]
