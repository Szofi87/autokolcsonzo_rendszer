from datetime import date
class Berles:
    def __init__(self, auto, datum: date):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"Bérlés: {self.auto.rendszam}, Dátum: {self.datum}"

    def ar_szamitas(self):
        return self.auto.berel()
