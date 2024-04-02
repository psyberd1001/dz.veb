import math

n = int(input('Введите число: -- '))
def function_seek(n):
    list_check = []
    count = 2
    while count < n:
        for j_el_list in list_check:
            if j_el_list > int((math.sqrt(count)) + 1):
                list_check.append(count)
                break
            if (count % j_el_list == 0):
                break
        else:
            list_check.append(count)
        count += 1
    return list_check

print(function_seek(n))
