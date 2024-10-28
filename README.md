GDE_OOP
# Autókölcsönző Rendszer

## Leírás
Ez a projekt egy egyetemi beadandó feladat - autókölcsönző rendszer, amely lehetővé teszi autók bérlését, a bérlések lemondását, és az aktuális bérlések listázását. 

## Funkciók
- **Autó bérlése**: Autók bérelhetők egy napra, a bérlés ára függ az autó típusától.
- **Bérlés lemondása**: A felhasználó lemondhatja a meglévő bérlését.
- **Bérlések listázása**: Az összes aktuális bérlés megtekinthető.

## Használt technológiák
- Python 3.13.0

## Projekt struktúrája
A projekt fájlszerkezete a következő:

autokolcsonzo_rendszer/
│
├── main.py                 
├── models/                 
│   ├── auto.py             
│   ├── szemelyauto.py      
│   ├── teherauto.py        
│   ├── berles.py           
│   └── autokolcsonzo.py    
│
├── data/                   
│   └── adatok.txt                       
│
├── README.md               
└── .gitignore              



## Telepítési útmutató
1. **Klónozd a repository-t**:

   git clone https://github.com/Szofi87/autokolcsonzo_rendszer.git
   
   cd autokolcsonzo_rendszer
   
3. **Futtatás**: 
   python main.py
   
## Használati útmutató
A program elindítása után a következő műveletek közül választhatsz:

1. **Autó bérlése**: Add meg az autó rendszámát, és a program visszaadja a bérleti díjat.
2. **Bérlés lemondása**: Add meg az autó rendszámát a bérlés lemondásához.
3. **Bérlések listázása**: A program kilistázza az összes aktuális bérlést.
4. **Kilépés**: Lezárja a programot.

## Előre feltöltött adatok
A program indulásakor három autó és négy bérlés szerepel az adatbázisban, hogy a felhasználó azonnal használatba vehesse a rendszert.
- **Szemelyauto** ("AAA-123", "Toyota Corolla", 5000, 5)
- **Szemelyauto**("BBB-456", "Honda Civic", 5500, 5)
- **Teherauto**("CCC-789", "Ford Transit", 10000, 1000)
- **berles1** = (2024, 10, 24)
- **berles2** = (2024, 10, 25)
- **berles3** = (2024, 10, 26)
- **berles4** = (2024, 10, 27)

