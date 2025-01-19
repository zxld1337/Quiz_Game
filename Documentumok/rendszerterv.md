# Quiz Game – Rendszerterv

## Bevezetés

Ez a dokumentum a Quiz Game projekt fejlesztési tervét tartalmazza. A projekt célja egy interaktív, felhasználóbarát quiz alkalmazás létrehozása, amely offline is működik. A következőkben a projektszerepköröket, az üzleti folyamatokat, a követelményeket, a fejlesztési és telepítési tervet részletezzük.

## 1. Projektszervezet

- **Projektvezető**: Levente – Felelős a projekt menedzsmentjéért, a feladatok koordinálásáért és a csapatmunkáért.
- **Rendszerelemző**: Levente – A követelmények meghatározása, a rendszer architektújának tervezése.
- **Fejlesztő**: Levente – A kódolásért, a funkcionalitás megvalósításáért felelős.
- **Tesztelő**: Levente – A rendszer tesztelése, a hibák felderítése és dokumentálása.
- **Felhasználói tesztelő**: Levente – A felhasználói élmény értékelése.

## 2. Üzleti folyamatok

- **Jelenlegi állapot**: Korlátozott offline szórakozási lehetőségek, nincs egységes quiz platform.
- **Célállapot**: Egy felhasználóbarát, offline quiz alkalmazás, amely képes véletlenszerű kérdéseket generálni és kiértékelni.

### Folyamatok:
1. Alkalmazás indítása
2. Kérdések megjelenítése és megválaszolása
3. Pontszámítás
4. Játék befejezése vagy újrakezdés

## 3. Követelmények

### Funkcionális:
- Felhasználóbarát felület
- Véletlenszerű kérdésgenerálás
- Pontszámítás

### Nem funkcionális:
- Offline működés
- Gyors válaszidő
- Több platformos kompatibilitás

## 4. Technikai részletek

### Fejlesztői környezet:
- **Programozási nyelv**: Python
- **Fejlesztői eszköz**: Visual Studio Code
- **Könyvtárak**: Tkinter (felület), random (véletlenszám-generálás), dataclasses (adatszerkezetek)

### Hardver és szoftver:
- Személyi számítógép vagy laptop
- Bármely modern operációs rendszer, amely támogatja a Pythont

## 5. Fejlesztési terv

1. **Felület tervezése**: A felhasználói felület prototípusának elkészítése.
2. **Kérdések és logika**: A kérdésbank felépítése, a kérdésgeneráló algoritmus megírása.
3. **Pontszámítás**: A válaszok kiértékelésének és a pontszámok számításának megvalósítása.
4. **Tesztelés**: Egységes és integrációs tesztek futtatása.
5. **Dokumentáció**: A kód dokumentálása, felhasználói útmutató készítése.

## 6. Telepítési terv

1. **Csomagolás**: Az alkalmazás egyetlen futtatható fájlba (pl. .exe) történő csomagolása.
2. **Telepítő**: Egy egyszerű telepítő létrehozása.
3. **Teszttelepítés**: A telepítő tesztelése különböző környezetekben.
4. **Terjesztés**: Az alkalmazás elérhetővé tétele a felhasználók számára (pl. letölthető fájlként).

## 7. Időterv és költségvetés

- **Időterv**: A fejlesztés egyes fázisainak időtartamának becslése.
- **Költségvetés**: A projekt költségeinek becslése (szoftverlicenck, hardver, stb.).

## 8. Kockázatok és teendők

### Kockázatok:
- Időcsúszás
- Változó követelmények
- Technikai problémák

### Teendők:
- Rendszeres státuszjelentések
- Rugalmas tervezés
- Alapos tesztelés

## 9. Befejezés

Ez a fejlesztési terv egy átfogó képet nyújt a Quiz Game projektről. A tervet folyamatosan aktualizálni kell a projekt előrehaladtával.

