list_1 = input('Введите числа: -- ')
list_1 = list_1.split()
list_1 = list(map(int, list_1))

def function_lucky(*args):
    if list_1[0] + list_1[1] + list_1[2] == list_1[3] + list_1[4] + list_1[5]:
        print('YOU ARE LUCKY MEN!')
    else:
        print("YOU LOSE")

function_lucky(list_1)