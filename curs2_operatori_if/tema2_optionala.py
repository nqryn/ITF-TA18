"""
1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""

x = int(input('Introdu un numar: '))
if -999 <= x <= 999:
    print('Numarul introdus nu are minim 4 cifre')
else:
    print('Numarul introdus are minim 4 cifre')

# 2.Verifică dacă x are exact 6 cifre.

x = int(input('Introdu un numar: '))
if -999999 <= x <= -100000 or 100000 <= x <= 999999:
    print('Numarul are exact 6 cifre')
else:
    print('Numarul nu are exact 6 cifre')

# 3.Verifică dacă x este număr par sau impar (x e int).
x = int(input('Introdu un numar: '))
if x % 2 == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')

"""
4. x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if x > y and x > z:
    print('x este cel mai mare numar')
elif y > x and y > z:
    print('y este cel mai mare numar')
elif z > x and z > y:
    print('z este cel mai mare numar')
else:
    print('Mai incearca o data si introdu 3 numere diferite')

"""
5.
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
"""

x = int(input('Unghiul x = '))
y = int(input('Unghiul y = '))
z = int(input('Unghiul z = '))
if x + y + z == 180:
    print('Acesta este un triunghi valid')
else:
    print('Acesta nu este un triunghi valid')

"""
6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
"""

my_string = "Coral is either the stupidest animal or the smartest rock"
x = int(input('x = '))
print(my_string[:(len(my_string) - x)])

"""
7.Același string. Declară un string nou care să fie format din primele 5 caractere
+ ultimele 5
"""

my_string = "Coral is either the stupidest animal or the smartest rock"
print(my_string[0:5] + my_string[len(my_string) - 5:])

"""
8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest '
"""

my_string = "Coral is either the stupidest animal or the smartest rock"
index = my_string.rfind('rock')
print(index)
print(my_string[:index])

"""
9. Citește de la tastatura un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
"""
my_string = input('Introdu un sir de caractere: ')
assert my_string[0].lower() == my_string[-1].lower()

"""
10. Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
"""

my_string = "0123456789"
print(my_string[1::2])
print(my_string[0::2])

"""
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll

Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
"""

import random
x = int(input('Alege un numar de la 1 la 6: '))
dice_roll = random.randint(1, 6)
print(dice_roll)
if x < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}')
elif x > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {x} si zarul a fost {dice_roll}')
