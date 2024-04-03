number_start = int(input('Введите начало: -- '))
number_stop = int(input('Введите конец: -- '))

def sum_rage_number(*args):
    sum_all_number = 0
    for i in range(number_start, number_stop + 1):
        sum_all_number = sum_all_number + i
    return sum_all_number

print(sum_rage_number())

