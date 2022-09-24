# 1.În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# o variabila este un container din memorie care stocheaza valori

"""
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :

- string
- int
- float
- bool

Observație: Valorile vor fi alese de tine după preferințe.
"""
nume = 'Calin'
varsta = 35
greutate = 82.3
permis = True

# 3.Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(nume))
print(type(varsta))
print(type(greutate))
print(type(permis))

"""
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
"""
greutate = round(greutate)
print(greutate)
print(type(greutate))

""" 
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
"""
print('Numele meu este ' + nume)
print('Am varsta de ' + str(varsta) + ' de ani')
print('Cantaresc ' + str(greutate) + ' kg')
print('Detin permis de conducere ' + str(permis))

"""
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
"""
nume = input('Numele este: \n')
prenume = input('Prenumele este: \n')
print('Numele complet are ', len(nume) + len(prenume), 'caractere')

"""
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
"""
lat = input('Latimea dreptunghiului este: \n')
lung = input('Lungimea dreptunghiului este: \n')
print('Aria dreptunghiului este: ', int(lat) * int(lung))

"""
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':

- afișează de câte ori apare cuvântul 'the';

9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
10. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.
"""
fraza = 'Coral is either the  stupidest animal or the smartest rock'
print('Cuvantul "the" apare de', fraza.count(' the '), 'ori')
assert fraza.isnumeric() == True
print('Fraza contine doar numere')




