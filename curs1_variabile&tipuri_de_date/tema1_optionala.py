from math import ceil
"""
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
"""

cuvant = input('Introduceti un cuvant cu numar impar de litere: \n')
dim_cuvant = int(len(cuvant))
mijloc = ceil((dim_cuvant / 2)-1)
print(f'Litera din mijlocul cuvantului introdus este {cuvant[mijloc]}.')

# 2. Folosind assert, verifică dacă un string este palindrom.

cuvant = input('Introduceti un cuvant cu numar impar de litere: \n')
assert (str(cuvant) == str(cuvant)[::-1])
print('Cuvantul introdus este palindrom.')

"""
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
"""

cuvant1, cuvant2 = input('Introduceti doua cuvinte: \n').split()
print(cuvant1, cuvant2)


"""
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
"""

expresie = input('Introduceti expresia dorita:\n')
first_char = expresie[0]
last_char = int(expresie.rindex(first_char))
rest_chars = expresie[last_char:len(expresie)]
expresie = expresie[1:last_char].replace(first_char, first_char.upper())
expresie_cu_upper = first_char + expresie + rest_chars
print(expresie_cu_upper)

"""
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
"""

user = input('Introduceti userul: \n')
parola = input('Introduceti parola: \n')
hide_parola = len(parola) * '*'
print(f'Parola pentru userul {user} este {hide_parola} si are {len(parola)} caractere')
