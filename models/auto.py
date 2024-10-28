from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
        self.berelve = False

    @abstractmethod
    def __str__(self):
        pass

    def berel(self):
        if self.berelve:
            raise ValueError("Az autó már bérlés alatt van.")
        self.berelve = True
        return self.berleti_dij

    def lemond(self):
        if not self.berelve:
            raise ValueError("Az autó nincs bérlés alatt.")
        self.berelve = False
