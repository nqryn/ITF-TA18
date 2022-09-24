"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
"""
print("Exercitiul 1")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in range(len(masini)):
    print(f"Masina mea preferata este {masini[masina]}")

print("*" * 100)

for masina in masini:
    print(f"Masina mea preferata este {masina}")

print("*" * 100)

i = 0
while i < len(masini):
    print(f"Masina mea preferata este {masini[i]}")
    i += 1

print("*" * 100)
"""
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrise cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
"""
print("Exercitiul 2")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in range(1, len(masini)-1):
    masini[masina] = masini[masina].upper()
else:
    print(masini)

"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
"""
print("Exercitiul 3")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Mercedes":
        print(f"Am gasit masina {masina} dorita de dvs.")
        break
    else:
        print(f"Am găsit mașina {masina}. Mai căutam.")

"""
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
"""
print("Exercitiul 4")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Trabant" or masina == "Lăstun":
        continue
    print(f"S-ar putea să vă placă mașina {masina}")

"""
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
"""
print("Exercitiul 5")

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == "Trabant" or masina == "Lăstun":
        masini_vechi.append(masina)
        idx = masini.index(masina)
        masini[idx] = "Tesla"
print(f"Modele vechi:{masini_vechi}")
print(f"Modele noi:{masini}")

"""
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.

"""
print("Exercitiul 6")
pret_masini = {'Dacia': 6800, 'Lăstun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}
for masina, pret in pret_masini.items():
     if pret < 15000:
         print(f"Pentru un buget de sub 15000 euro puteti alege masina {masina}")

"""
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
print("Exercitiul 7")

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for numar in numere:
    if numar == 3:
        count += 1
print(f"Numarul 3 apare de {count} ori ")

"""
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
print("Exercitiul 8")

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma += numar
print(f"Suma numerelor este: {suma}")

"""
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
"""
print("Exerctiul 9")

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_max = 0
for numar in numere:
    if numar > nr_max:
        nr_max = numar
print(f"Cel mai mare numar este: {nr_max}")

"""
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
"""
print("Exerctiul 10")

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar in range(len(numere)):
    if numere[numar] > 0:
        numere[numar] = - numere[numar]
print(numere)
