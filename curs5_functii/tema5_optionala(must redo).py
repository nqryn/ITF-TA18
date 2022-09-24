# """
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
# """
#
# def number_of_days_in_month():
#     if month in ["Ianuarie", "Martie", "Iunie", "Iulie", "August", "Octombrie", "Decembrie"]:
#         print("Luna aleasa are 31 de zile")
#     elif month in ["Martie", "Iunie", "Septembrie", "Noiembrie"]:
#         print("Luna aleasa are 30 de zile")
#     else:
#         print("Luna aleasa are 28 de zile")
# month = input("Alege o luna a anului:")
# number_of_days_in_month()
#
# """
# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)
# """
#
# def calculator(x, y):
#     a = x + y
#     b = x - y
#     c = x * y
#     d = x / y
#     return a, b, c, d
# x = int(input("x = "))
# y = int(input("y = "))
# a,b,c,d = calculator(x, y)
# print(f"{x} + {y} = {a}")
# print(f"{x} - {y} = {b}")
# print(f"{x} * {y} = {c}")
# print(f"{x} / {y} = {d}")
"""
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

def digit_count(lst):
    digit = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }
    for number in digit:
        for nr in digit:
            if nr == number:
                digit[number] += 1
    return digit
lst = [0, 0, 3, 3, 3, 4, 5, 6, 9, 9]
digit_count(lst)