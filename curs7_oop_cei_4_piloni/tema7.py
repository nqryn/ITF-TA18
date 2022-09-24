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

    def get_latura(self):
        print(f"Patratul are latura {self.__latura}")
        return self.__latura

    def set_latura(self, noua_latura):
        print(f"Patratul avea latura {self.__latura}, acum are latura {noua_latura}")
        self.__latura = noua_latura

    def del_latura(self):
        self.__latura = None

    def aria(self):
        return self.__latura ** 2


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def get_raza(self):
        print(f"Cercul are raza {self.__raza}")
        return self.__raza

    def set_raza(self, noua_raza):
        print(f"Cercul avea raza {self.__raza}, acum are raza {noua_raza}")
        self.__raza = noua_raza

    def del_raza(self):
        self.__raza = None

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
cerc.set_raza(7)
print(cerc.aria())
cerc.get_raza()
cerc.del_raza()
cerc.get_raza()
patrat.get_latura()
patrat.set_latura(8)
patrat.del_latura()