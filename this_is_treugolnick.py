first_storona = int(input('Первая сторона равна: '))
second_storona = int(input('Вторая сторона равна: '))
therd_storona = int(input('Третья сторона равна: '))
bool_number = True
def function_proverka(first_storona, second_storona, therd_storona):
    if first_storona + second_storona > therd_storona and first_storona + therd_storona > second_storona and second_storona + therd_storona > first_storona:
        bool_number = True
        print('Да, может')
    else:
        bool_number = False
        print('Неа, может ещё подумаете?')
    return bool_number

print(function_proverka(first_storona, second_storona, therd_storona))