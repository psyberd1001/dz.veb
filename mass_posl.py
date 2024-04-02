#Расчет стоимости доставки

def function(*args):
    price_1 = 50
    price_3 = 200
    mass = int(input('Введите массу посылки: -- '))
    if mass <= 2:
        print(price_1, 'руб')
    if mass <= 10 and mass > 2:
        for i in range(2, mass - 1, 1):
            price_1 = price_1 + 20
        return print(price_1)
    if mass > 10:
        print(price_3)


function()

