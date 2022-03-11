a_list: list[str] = ['a', 'b', 'd']
a_dict: dict[str, int] = {'a': 1, 'b': 2}
for i in a_list:
    if i in a_dict:
        print(i)
