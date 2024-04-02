my_str = input('Введите строку для подсчета длины: ')


def function_my_len(*args):
    count = 0
    for i in my_str:
        count = count + 1
    return count


print(function_my_len(my_str))
