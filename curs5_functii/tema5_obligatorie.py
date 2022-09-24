"""
1.Funcție care să calculeze și să returneze suma a două numere
"""


def suma():
    return a + b


a = int(input("a = "))
b = int(input("b = "))
s = suma()
print(f"a + b = {s}")

"""
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
"""


def true_false():

    if x % 2 == 0:
        return True
    else:
        return False


x = int(input("Introdu un numar. Voi afisa TRUE daca este par sau FALSE daca este impar.\n"))
print(true_false())

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""


def name_char_count():
    x = len(nume)
    y = len(prenume)
    z = len(nume_mijlociu)
    return x + y + z
nume = input("Nume: ")
prenume = input("Prenume: ")
nume_mijlociu = input("Nume mijlociu: ")
print(f"Numarul total de caractere:", name_char_count())

"""
4. Funcție care returnează aria dreptunghiului
"""


def aria():
    s = x * y
    return s


x = int(input("Latimea dreptunghiului: "))
y = int(input("Lungimea dreptunghiului: "))
s = aria()
print(f"Aria dreptunghiului: {s}")

"""
5. Funcție care returnează aria cercului
"""


def aria_cerc():
    s = 3.14 * r ** 2
    return s


r = int(input("Raza cercului: "))
s = aria_cerc()
print(f"Aria cercului: {s}")

"""
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
"""


def find_char():
    if x in str:
        return True
    else:
        return False


my_str = input("Introdu un string de caractere: ")
x = input("Caracterul cautat: ")
print(find_char())

"""
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""


def lower_upper_count():
    low = upp = 0
    for i in str:
        if i == i.upper():
            upp += 1
        else:
            low += 1
    print(f"Numarul de caractere lower case este {low}")
    print(f"Numarul de caractere upper case este {upp}")


my_str = input("Introdu un string de caractere: ")
lower_upper_count()

"""
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
"""


def number_list(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
          lst[i] = -lst[i]
    return lst


lst = []
n = int(input("Introdu numarul de elemente al listei: "))
for i in range(0, n):
    elem = int(input("Introdu elementele: "))
    lst.append(elem)
print(lst)
print(number_list(lst))

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
"""


def compare(x, y):
    if x > y:
        print(f"{x} > {y}")
    elif x < y:
        print(f"{x} < {y}")
    else:
        print(f"{x} = {y}")


x = input("x = ")
y = input("y = ")
compare(x, y)


"""
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""


def set_insert(x, my_set):
    if x in my_set:
        print("Nu am adaugat numărul în set. Acesta există deja")
        return False
    else:
        my_set.add(x)
        print("Am adaugat numărul nou în set")
        return True


my_set = {98, 8, 3, -44}
set_insert(7, my_set)
print(my_set)
