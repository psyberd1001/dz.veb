list_number = input('Введите числа которые нужно сложить: -- ')
list_number = list_number.split()
list_number_1 = []
sum_all_number = 0

def sum_rage(*args):
    sum_all_number = 0
    for i in range(len(list_number)):
        list_number_1.append(int(list_number[i]))
    for j in range(list_number_1[-1] + 1):
        sum_all_number = sum_all_number + j
    return sum_all_number

print(sum_rage())

