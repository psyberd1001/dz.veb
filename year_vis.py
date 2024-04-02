def year_old(*args):
    year = int(input('Введите год для проверки: -- '))
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print('Congratuletion')
    else:
        print('LOSE')


year_old()
