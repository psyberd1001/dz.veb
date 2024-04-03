small_symbols_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
big_symbols_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
small_symbols_eng = "abcdefghijklmnopqrstuvwxyz"
big_symbols_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shift(text, symbols, n):  # функция смещения каждого символа
    index = symbols.find(text)
    if index + n < len(symbols):
        return symbols[index + n]
    else:
        return symbols[(index + n) % len(symbols)]


def back_shift(text, symbols, n): # функция обратного смещения, так же по символьно
    index = symbols.find(text)
    if index - n >= 0:
        return symbols[index - n]
    else:
        return symbols[(index - n) % len(symbols)]


def encrypt(text, n=4): # функция которая шифрует весь текст соответственно используя функцию shift для смещения по символьно
    res = ""

    for i in range(0, len(text)):
        if text[i] in small_symbols_rus or text[i] in big_symbols_rus:
            if text[i].isupper():
                res += shift(text[i], big_symbols_rus, n)

            elif text[i].islower():
                res += shift(text[i], small_symbols_rus, n)
            else:
                res += text[i]
        if text[i] in small_symbols_eng or text[i] in big_symbols_eng:
            if text[i].isupper():
                res += shift(text[i], big_symbols_eng, n)

            elif text[i].islower():
                res += shift(text[i], small_symbols_eng, n)
            else:
                res += text[i]

    return res


def decrypt(text, n=4): # обратная функция дешифрования по символьно
    res = ""

    for i in range(0, len(text)):
        if text[i] in small_symbols_rus or text[i] in big_symbols_rus:
            if text[i].isupper():
                res += back_shift(text[i], big_symbols_rus, n)

            elif text[i].islower():
                res += back_shift(text[i], small_symbols_rus, n)
            else:
                res += text[i]
        if text[i] in small_symbols_eng or text[i] in big_symbols_eng:
            if text[i].isupper():
                res += back_shift(text[i], big_symbols_eng, n)

            elif text[i].islower():
                res += back_shift(text[i], small_symbols_eng, n)
            else:
                res += text[i]
    return res


str = encrypt(input())
print(str)
print(decrypt(str))