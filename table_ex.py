n = int(input('Введите число для таблицы умножения: -- '))

def function_table(n):
    for i in range(1, n + 1):
        for j in range(1, 11):
            print(i, '*',  j, "=", i * j)

function_table(n)
