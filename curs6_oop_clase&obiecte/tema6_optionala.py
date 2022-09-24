"""
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs  | cantitate | preț bucată | Total
Telefon |      7    |      700    | 49000
"""
from datetime import date


class Factura():
    SERIA = "YYY"
    numar = 0
    nume_produs = ""
    cantitate = 0
    pret_buc = 0.0

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        print(f"Factura seria {self.SERIA} numar {self.numar}")
        print(f"Data: {date.today()}")
        print(f"Produs  | cantitate | preț bucată |  Total")
        print(f"{self.nume_produs} |      {self.cantitate}    |     {self.pret_buc}     |  {self.cantitate * self.pret_buc}")


telefon = Factura(1001, "Telefon", 7, 700)
telefon.genereaza_factura()
telefon.schimba_cantitatea(10)
telefon.schimba_pretul(900)
telefon.schimba_nume_produs("Iphone")
telefon.genereaza_factura()

masina = Factura(1002, "Masina", 1, 15000)
masina.genereaza_factura()
masina.schimba_cantitatea(2)
masina.schimba_pretul(30000)
masina.schimba_nume_produs("Audi")
masina.genereaza_factura()

"""
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""


class Masina():
    marca = "Dacia"
    model = ""
    viteza_maxima = 0
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = {"alb", "negru", "rosu", "verde", "albastru", "galben"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f"Masina aleasa este marca {self.marca}, model {self.model}, are culoarea {self.culoare} si atinge o viteza maxima de {self.viteza_maxima} km/h.")

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoarea_aleasa):
        if culoarea_aleasa in self.culori_disponibile:
            self.culoare = culoarea_aleasa
        else:
            print(f"Culoarea aleasa nu este disponibila. Alegeti o alta culoare din lista {self.culori_disponibile}")

    def accelereaza(self, viteza):
        if viteza < 0:
            print(f"Eroare!! Nu se poate accelera la {viteza} km/h")
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f"{self.marca} {self.model} a atins viteza maxima de {self.viteza_actuala} km/h. Nu se poate accelera mai mult.")

    def franeaza(self):
        self.viteza_actuala = 0


masina1 = Masina("Duster", 180)
masina1.descrie()
masina1.inmatriculare()
print(masina1.inmatriculata)
masina1.vopseste("portocaliu")
masina1.accelereaza(-200)
masina1.accelereaza(210)
print(masina1.viteza_actuala)
masina1.vopseste("rosu")
masina1.descrie()
masina1.franeaza()
print(masina1.viteza_actuala)


"""
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""


class TodoList():
    todo = {

    }

    def adauga_task(self, nume, descriere):
        TodoList.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        del TodoList.todo[nume]

    def afiseaza_todo_list(self):
        print(TodoList.todo.keys())

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo:
            prompt = input(f"Taskul {nume_task } nu este in lista ta. Vrei sa-l adaugi? (da/nu): ")
            if prompt == "da":
                descriere = input(f"Descrie taskul {nume_task}: ")
                TodoList.todo[nume_task] = descriere
            else:
                print("La revedere")


task1 = TodoList()
task1.adauga_task("curatenie", "curatenie generala in locuinta")
task1.afiseaza_todo_list()
task1.afiseaza_detalii_suplimentare("tema")
task2 = TodoList()
task2.adauga_task("cumparaturi", "produse de curatenie")
print(TodoList.todo)
task2.afiseaza_detalii_suplimentare("gatit")
print(TodoList.todo)
task2.afiseaza_todo_list()