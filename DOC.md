# Quiz Game Dokumentáció

## 1. Funkcionális specifikáció

### A rendszer céljai és nem céljai
#### Célok
- Egy interaktív kvízjáték megvalósítása, amely szórakoztató módon fejleszti a játékosok tudását.
- A játékosok számára különböző témakörökből véletlenszerűen választott kérdéseket biztosítani.
- A helyes válaszok számlálása és a játék végén egy összegzés megjelenítése.
- Egyszerű, grafikus felhasználói felület biztosítása, amely könnyen érthető és használható.
- A játék újrajátszhatóságának lehetősége a felhasználói élmény növelése érdekében.
- Az azonnali visszajelzés biztosítása a felhasználók számára a válaszaik helyességéről.

#### Nem célok
- Nem cél a játék hálózati funkcióinak megvalósítása.
- Nem cél az eredmények tárolása vagy rangsor készítése.
- Nem cél a kérdésbank bővítése vagy online frissítése.
- Nem cél a többfelhasználós mód támogatása vagy statisztikák elemzése.

### Használati esetek
1. **Játék indítása**: A felhasználó megnyitja a játékot, és elindítja az első kvízkérdést.
2. **Válaszadás**: A játékos kiválaszt egy választ a megadott lehetőségek közül.
3. **Játék vége**: Miután az összes kérdést megválaszolta, a játékos látja a végeredményt.
4. **Új játék indítása vagy kilépés**: A játék végén a felhasználó új játékot indíthat vagy kiléphet az alkalmazásból.
5. **Eredmények visszajelzése**: A játék során azonnali visszajelzés a helyes vagy helytelen válaszokról.
6. **Helytelen válasz következménye**: A játékos látja a helytelen válaszokat, de ez nem befolyásolja a következő kérdés lehetőségét.

### Megfeleltetés
| Követelmény         | Használati esetek       |
|---------------------|-------------------------|
| Interaktív játék    | Játék indítása, Válaszadás |
| Eredmények megjelenítése | Játék vége, Eredmények visszajelzése |
| Újrakezdés opció    | Új játék indítása       |
| Felhasználóbarát UI | Játék indítása, Válaszadás, Játék vége |
| Visszajelzés        | Eredmények visszajelzése, Helytelen válasz következménye |

### Képernyőtervek
1. **Kezdőképernyő**: A "Üdvözöllek a Quiz Játékomban!" szöveggel és egy "Kezdés" gombbal.
2. **Kérdések képernyője**: Egy kérdés szövegével és három válaszlehetőséggel rendelkező gombokkal.
3. **Eredmény képernyő**: A "Gratulálok!" szöveg, a helyes válaszok száma, és két gomb: "Újra próbálom" és "Kilépés".
4. **Helyes válasz visszajelzés képernyője**: A kiválasztott válasz után rövid értesítés arról, hogy a válasz helyes volt-e.
5. **Helytelen válasz visszajelzés képernyője**: A rendszer közli, hogy a válasz helytelen volt, és megmutatja a helyes választ.

### Forgatókönyvek
#### Kezdőképernyő
1. A felhasználó megnyitja az alkalmazást.
2. Megjelenik egy "Üdvözöllek a Quiz Játékomban!" üzenet.
3. A "Kezdés" gombra kattintva a játék elindul.

#### Játék közben
1. A rendszer véletlenszerűen kiválaszt egy kérdést.
2. A játékos választ egyet a lehetőségek közül.
3. A rendszer számlálja a helyes válaszokat és új kérdést jelenít meg, amíg van kérdés.
4. A kiválasztott válasz után azonnali visszajelzés jelenik meg a helyességről.
5. Ha a válasz helytelen, a rendszer megmutatja a helyes választ.

#### Játék vége
1. Az összes kérdés megválaszolása után a rendszer kiírja az eredményt.
2. A játékos dönthet: "Újra próbálom" vagy "Kilépés".

## 2. Követelmény specifikáció

### Vezetői összefoglaló
A Quiz Game egy oktató és szórakoztató alkalmazás, amely kvízkérdéseken keresztül teszteli és fejleszti a felhasználók általános tudását. A rendszer egyszerű, mégis interaktív grafikus felületet biztosít, amely lehetővé teszi a kérdések gyors megválaszolását. Az alkalmazás célja az, hogy a felhasználók számára egy könnyen kezelhető, újrajátszható élményt nyújtson, amely bármely asztali környezetben futtatható. Emellett lehetőséget biztosít a tanulásra a válaszok kiértékelése által.

### Vágyálomrendszer leírása
- **Felhasználóbarát felület**: Könnyen kezelhető grafikus interfész.
- **Széleskörű kérdésbank**: Különböző témakörökből érkező véletlenszerű kérdések.
- **Pontszámlálás**: A helyes válaszok számlálása és megjelenítése.
- **Többször újrajátszható**: A játék végeztével újrakezdési lehetőség.
- **Azonnali visszajelzés**: Minden válasz után visszajelzés a helyességről.
- **Egyszerű telepíthetőség**: A játék bármilyen Python-támogatott operációs rendszeren futtatható.
- **Tanulási lehetőség**: A helytelen válaszok esetén a helyes válasz megmutatása.
- **Interaktív élmény**: Dinamikus játékélmény azonnali vizuális visszacsatolással.

## 3. Rendszerterv

### A rendszer célja
A cél egy egyszerű, de hatékony kvízjáték létrehozása, amely szórakoztató módon fejleszti a játékosok tudását és biztosítja az interaktivitást egy asztali környezetben. A rendszer biztosítja, hogy a játékosok számára változatos és érdekes kérdések jelenjenek meg, miközben a játék gyors és intuitív marad. Emellett lehetőséget nyújt arra, hogy a játékosok tanuljanak a helyes válaszok megismerése által.

### Követelmények
#### Funkcionális követelmények
- **Kérdések megjelenítése**: Véletlenszerűen kiválasztott kérdések jelenjenek meg a képernyőn.
- **Válaszlehetőségek**: Három válaszlehetőség gombként.
- **Eredménykijelzés**: A helyes válaszok számának megjelenítése a játék végén.
- **Újrakezdési lehetőség**: A játék újraindítható legyen anélkül, hogy újra kellene indítani az alkalmazást.
- **Azonnali visszajelzés**: A válasz helyességének azonnali jelzése.
- **Tanulási funkció**: A helytelen válasz után a helyes válasz megmutatása.

#### Nem funkcionális követelmények
- **Könnyű használhatóság**: Az interfész legyen intuitív és egyszerű.
- **Gyors válaszidő**: A kérdések közötti váltás késleltetése minimális legyen.
- **Platformfüggetlenség**: A játék működjön Windows, macOS és Linux rendszereken is a Python és Tkinter használatával.
- **Minimális erőforrásigény**: A játék alacsony rendszerigényű, így régebbi gépeken is futtatható legyen.

### Technikai részletek
- **Fejlesztési nyelv**: Python 3.10 vagy újabb.
- **Grafikus keretrendszer**: Tkinter a felhasználói interfészhez.
- **Adatkezelés**: Kérdések listába rendezve, egyszerű Python osztályokkal.
- **Tesztelés**: Manuális tesztelés a funkcionális követelmények ellenőrzésére.
- **Kód minősége**: A program betartja a PEP 8 szabványt, így könnyen érthető és karbantartható.

