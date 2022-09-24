# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

# 2. Verifică și afișează dacă x este număr natural sau nu.
x = int(input('x = '))
if x >= 0:
    print("x este numar natural")
else:
    print("x nu este numar natural")

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x > 0:
    print("x este numar pozitiv")
elif x < 0:
    print("x este numar negativ")
else:
    print("x este neutru")

# 4. Verifică și afișează dacă x este între -2 și 13.
if -2 <= x <= 13:
    print("x este intre -2 si 13")
else:
    print("x nu este intre -2 si 13")

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
y = int(input('y = '))
if x - y < 5:
    print("Diferenta dintre x si y este mai mica de 5")
else:
    print("Diferenta dintre x si y este mai mare de 5")

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if not 5 < x < 27:
    print("x nu este intre 5 si 27")
else:
    print("x este intre 5 si 27")

"""
7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
"""

if x == y:
    print("x este egal cu y")
elif x < y:
    print("y este mai mare decat x")
else:
    print("x este mai mare decat y")

"""
8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
"""

z = int(input('z = '))
if x == y == z:
    print("Triunghiul xyz este echilateral")
elif x == y or x == z or y == z:
    print("Triunghiul xyz este isoscel")
else:
    print("Triunghiul xyz este oarecare")

"""
9. Citește o literă de la tastatură.

Verifică și afișează dacă este vocală sau nu
"""

litera = input('Introdu o litera: ')
vocale = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
if litera in vocale:
    print("Litera este o vocala")
else:
    print("Litera este o consoana")

"""
10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""

nota = float(input('Introdu nota: '))
if 9 <= nota <= 10:
    print('Echivalentul notei tale este A')
elif 8 <= nota < 9:
    print('Echivalentul notei tale este B')
elif 7 <= nota < 8:
    print('Echivalentul notei tale este C')
elif 6 <= nota < 7:
    print('Echivalentul notei tale este D')
elif 4 < nota < 6:
    print('Echivalentul notei tale este E')
elif 1 < nota < 4:
    print('Echivalentul notei tale este F')
else:
    print('Introdu o nota de la 1 la 10')

