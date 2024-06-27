def get_last_length(s: str):
    lst = s.split()
    res = len(lst[-1])
    return res


s = "luffy is still joyboy"

print(get_last_length(s))

