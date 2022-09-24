"""
Tema: faceti o clasa (Televizor) cu minim 3 atribute, 3 metode si 3 obiecte cu care sa va jucati.
Ganditi-va ce alte clase ar putea exista in ecosistemul vostru,
cu care clasa voastra poate interactiona?
"""
class TV:
    def __init__(self, marca, diagonala, pret):
        self.marca = marca
        self.diagonala = diagonala
        self.pret = pret

    def pret_nou(self, pret_nou):
        if pret_nou < self.pret:
            print(f"Vesti bune!! Pretul televizorului {self.marca} a scazut de la {self.pret} la {pret_nou}")
        elif self.pret < pret_nou:
            print(f"Din pacate, pretul televizorului {self.marca} a crescut de la {self.pret} la {pret_nou}")
        else:
            print("Pretul a ramas acelasi")
        self.pret = pret_nou


    def change_channel(self, channel, new_channel):
        if channel != new_channel:
            print(f"Erai pe canalul {channel} si ai mutat pe canalul {new_channel}")
        else:
            print("Nu ai schimbat canalul")
        self.channel = new_channel

    def change_volume(self, volume, new_volume):
        if new_volume == 0:
            print("Ai oprit sonorul")
        elif new_volume > volume:
            print(f"Ai marit volumul de la {volume} la {new_volume}")
        elif new_volume < volume:
            print(f"Ai micsorat volumul de la {volume} la {new_volume}")
        self.volume = new_volume

samsung = TV("Samsung", 100, 1500)
lg = TV("LG", 120, 1800)
samsung.change_channel(9, 10)
samsung.change_channel(10, 52)
samsung.change_volume(8, 0)
print(samsung.pret)
samsung.pret_nou(1400)
samsung.pret_nou(1800)

"""
Pentru toate clasele, creați cel puțin 2 obiecte cu valori diferite și apelați toate
metodele clasei.
"""
"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""

class Cerc:
    raza = 0
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cerc {self.culoare} cu raza {self.raza}")

    def aria(self):
        return self.raza ** 2 * 3.14

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return self.raza * 3.14

cerc_verde = Cerc(4, "verde")
cerc_rosu = Cerc(7, "rosu")
cerc_verde.descrie_cerc()
cerc_rosu.descrie_cerc()
print(cerc_rosu.aria())
print(cerc_rosu.diametru())
print(cerc_rosu.circumferinta())

"""
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""

class Dreptunghi():
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Dreptunghi {self.culoare} cu lungimea {self.lungime} si latimea {self.latime}")

    def aria(self):
        return self.latime * self.lungime

    def perimetru(self):
        return (self.latime + self.lungime) * 2

    def schimba_culoarea(self, noua_culoare):
        print(f"Dreptunghiul era {self.culoare} si acum este {noua_culoare}")
        self.culoare = noua_culoare

dreptunghi_galben = Dreptunghi(8, 5, "galben")
dreptunghi_galben.descrie()
print(dreptunghi_galben.aria())
print(dreptunghi_galben.perimetru())
dreptunghi_galben.schimba_culoarea("albastru")
dreptunghi_galben.descrie()

dreptunghi_alb = Dreptunghi(20, 10, "alb")
dreptunghi_alb.descrie()
print(dreptunghi_alb.aria())
print(dreptunghi_alb.perimetru())
dreptunghi_alb.schimba_culoarea("negru")
dreptunghi_alb.descrie()


"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""

class Angajat():
    nume = ""
    prenume = ""
    salariu = 0.0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"Angajatul {self.nume} {self.prenume} are salariul {self.salariu} lei")

    def nume_complet(self):
        return self.nume + " " + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu = self.salariu + self.salariu / procent


angajat1 = Angajat("Ionescu", "Ion", 3000)
angajat1.descrie()
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
angajat1.marire_salariu(10)
angajat1.descrie()
print(angajat1.salariu_anual())


"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""

class Cont():
    iban = ""
    titular_cont = ""
    sold = 0.0

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma_retrasa):
        self.sold -= suma_retrasa
        return self.sold

    def creditare_cont(self, suma_adaugata):
        self.sold += suma_adaugata
        return self.sold

client1 = Cont("XXXX XXXX XXXX XXXX", "Ionescu Ion", 10000)
client1.afisare_sold()
client1.debitare_cont(4000)
client1.afisare_sold()
client1.creditare_cont(500)
client1.afisare_sold()

