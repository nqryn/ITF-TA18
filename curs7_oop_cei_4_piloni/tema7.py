"""
2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
împreună).

ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’

INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)

POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""

from abc import ABC


class FormaGeometrica(ABC):
    PI = 3.14

    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print("Cel mai probabil am colturi")


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f"Patratul are latura {self.__latura}")
        return self.__latura

    @latura.setter
    def latura(self, noua_latura):
        print(f"Patratul avea latura {self.__latura}, acum are latura {noua_latura}")
        self.__latura = noua_latura

    @latura.deleter
    def latura(self):
        print("Se sterge latura")
        del self.__latura

    def aria(self):
        return self.__latura ** 2


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f"Cercul are raza {self.__raza}")
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f"Cercul avea raza {self.__raza}, acum are raza {raza}")
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print("Se sterge raza")
        del self.__raza

    def aria(self):
        return self.__raza ** 2 * self.PI

    def descrie(self):
        print("Eu nu am colturi")


cerc = Cerc(4)
cerc.descrie()
patrat = Patrat(5)
patrat.descrie()
print(cerc.aria())
print(patrat.aria())
cerc.raza = 7
print(cerc.aria())
cerc.raza
del cerc.raza
try:
    cerc.raza
except AttributeError as e:
    print("Raza a fost stearsa")
cerc = Cerc(10)
cerc.raza
