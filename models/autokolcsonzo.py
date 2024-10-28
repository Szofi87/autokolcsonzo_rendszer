from models.berles import Berles
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autok_hozzaadasa(self, auto):
        self.autok.append(auto)

    def berles_hozzaadasa(self, berles):
        self.berlesek.append(berles)

    def berles_listazasa(self):
        return [str(berles) for berles in self.berlesek]

    def auto_berlese(self, rendszam, datum):
        for auto in self.autok:
            if auto.rendszam == rendszam and not auto.berelve:
                berles = Berles(auto, datum)
                self.berles_hozzaadasa(berles)
                return berles.ar_szamitas()
        raise ValueError("Az autó nem elérhető.")

    def berles_lemondasa(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                berles.auto.lemond()
                self.berlesek.remove(berles)
                return f"A {rendszam} rendszámú autó bérlése lemondva."
        raise ValueError("Nincs ilyen bérlés.")
