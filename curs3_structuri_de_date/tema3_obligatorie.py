
"""
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
"""

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# 2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))

"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
"""

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
l3 = l1 + l2
print(l3)
l4 = []
l4.extend(l1)
l4.extend(l2)
print(l4)
"""
4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
"""

l4.sort()
print(l4)
l4.remove(0)
print(l4)
"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
"""

if l3:
    print('Lista nu este goala')
else:
    print('Lista este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.

l3.clear()
print(l3)

"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
"""

if l3:
    print('Lista nu este goala')
else:
    print('Lista este goala')

"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""

print(f'Ana a luat nota', dict1['Ana'])
print(f'Gigel a luat nota', dict1['Gigel'])
print(f'Dorel a luat nota', dict1['Dorel'])

"""
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
"""

dict1['Dorel'] = 6
print(f'Dorel a luat nota', dict1['Dorel'])

"""
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
"""

dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

"""
12. Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
"""

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

"""
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
"""

if weekend <= zile_sapt:
    print("Weekend este un subset al zilelor săptămânii")
else:
    print("Weekend nu este un subset al zilelor săptămânii")

# 14. Afișează diferențele dintre aceste 2 seturi.

print(zile_sapt - weekend)

# 15. Afișază intersecția elementelor din aceste 2 seturi.

print(weekend.intersection(zile_sapt))
print(weekend & zile_sapt)






