import datetime
from models.szemelyauto import Szemelyauto
from models.teherauto import Teherauto
from models.autokolcsonzo import Autokolcsonzo
from models.berles import Berles


def main():
    kolcsonzo = Autokolcsonzo("Szofi's Autorent")

    auto1 = Szemelyauto("AAA-123", "Toyota Corolla", 5000, 5)
    auto2 = Szemelyauto("BBB-456", "Honda Civic", 5500, 5)
    auto3 = Teherauto("CCC-789", "Ford Transit", 10000, 1000)

    kolcsonzo.autok_hozzaadasa(auto1)
    kolcsonzo.autok_hozzaadasa(auto2)
    kolcsonzo.autok_hozzaadasa(auto3)

    berles1 = Berles(auto1, datetime.date(2024, 10, 24))
    berles2 = Berles(auto2, datetime.date(2024, 10, 25))
    berles3 = Berles(auto3, datetime.date(2024, 10, 26))
    berles4 = Berles(auto1, datetime.date(2024, 10, 27))

    kolcsonzo.berles_hozzaadasa(berles1)
    kolcsonzo.berles_hozzaadasa(berles2)
    kolcsonzo.berles_hozzaadasa(berles3)
    kolcsonzo.berles_hozzaadasa(berles4)

    while True:
        print("\n1. Autó bérlése\n2. Bérlés lemondása\n3. Bérlések listázása\n4. Kilépés")
        valasz = input("Válassz egy opciót: ")

        if valasz == "1":
            rendszam = input("Add meg az autó rendszámát: ")
            if not rendszam.strip():
                print("Érvénytelen rendszám.")
                continue

            datum = datetime.date.today()
            try:
                ar = kolcsonzo.auto_berlese(rendszam, datum)
                print(f"A bérlés sikeres, az ár: {ar} Ft.")
            except ValueError as e:
                print(e)

        elif valasz == "2":
            rendszam = input("Add meg az autó rendszámát a lemondáshoz: ")
            if not rendszam.strip():
                print("Érvénytelen rendszám.")
                continue

            try:
                uzenet = kolcsonzo.berles_lemondasa(rendszam)
                print(uzenet)
            except ValueError as e:
                print(e)

        elif valasz == "3":
            berlesek = kolcsonzo.berles_listazasa()
            if berlesek:
                print("\nAktuális bérlések:")
                for berles in berlesek:
                    print(berles)
            else:
                print("Nincsenek aktuális bérlések.")

        elif valasz == "4":
            print("Kilépés.")
            break

        else:
            print("Érvénytelen opció.")


if __name__ == "__main__":
    main()
