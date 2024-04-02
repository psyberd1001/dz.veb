import random

number_1 = random.randint(0, 100)
print(number_1)

def function_seek(*args):
    number_seek = int(input('Попробуйте угадать введенное число! '))
    count = 1
    if number_seek == number_1:
        print('Вы нашли искомое число, поздравляю!')
    else:
        while number_seek != number_1:
            if number_seek > number_1:
                print('Вы очень близко, но искомое число меньше!', 'Количество попыток', count)
                count = count + 1
                print()
                number_seek = int(input('Попробуйте угадать введенное число! --'))
            if number_seek < number_1:
                print('Вы очень близко, но искомое число больше!', 'Количество попыток', count)
                count = count + 1
                print()
                number_seek = int(input('Попробуйте угадать введенное число! --'))
            if number_seek == number_1:
                print('Вы нашли искомое число, поздравляю!', 'Количество попыток', count)

function_seek()