from abc import ABC, abstractmethod


class ShipBlueprint(ABC):
    @abstractmethod
    def tezlashish(self):
        pass

    def yelkanlarni_kotarish(self):
        pass

    @abstractmethod
    def burilish(self):
        pass

    @abstractmethod
    def langar_tashlash(self):
        pass

    @abstractmethod
    def tor_tashlash(self):
        pass

    @abstractmethod
    def danger(self):
        pass


class Ship(ShipBlueprint):
    def tezlashish(self, a=10):
        if a + self.__tezlik <= self.__max_tezlik:
            self.__tezlik += a
        else:
            self.__tezlik = self.__max_tezlik

    def burilish(self, yonalish=30):
        if self.__tezlik <= 20:
            self.__yonalish = yonalish
            print(f"Yo'nalish qayta sozlandi\nYangi yo;nalish {self.__yonalish}")
        else:
            print("Tezlik yuqori!!!")

    def langar_tashlash(self):
        if self.langar_tashlash():
            print("Langar tashlandi.")
        else:
            print("Langar ko'tarildi")
        self.__langar_pastda = not self.__langar_pastda

    def tor_tashlash(self):
        if self.__tor_tashlangan:
            print("Tor tashlandi.")
        else:
            print("Tor ko'tarildi")
        self.__tor_tashlangan = not self.__tor_tashlangan

    def danger(self):
        print(self.__sos)

    def __init__(self, nom, brend, sigim, max_tezlik, narx):
        self.__nom = nom
        self.__narx = narx
        self.__max_tezlik = max_tezlik
        self.__sigim = sigim
        self.__brend = brend
        self.__tezlik = 0
        self.__yonalish = 0
        self.__langar_pastda = True
        self.__yeklan = False
        self.__tor_tashlangan = False
        self.__sos = "SOS SOS SOS YORDAM PLIZ"
