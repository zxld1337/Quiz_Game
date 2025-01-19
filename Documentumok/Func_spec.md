# Quiz Game – Funkcionális követelmények

## 1. Bevezetés

A jelen dokumentum a Quiz Game alkalmazás funkcionális követelményeit részletezi. Az alkalmazás célja, hogy interaktív és felhasználóbarát módon tesztelje a felhasználók tudását különböző témákban.

## 2. Célkitűzések

**Fő cél:** Egy olyan interaktív játék biztosítása, amely képes véletlenszerű kérdéseket generálni és azokat értékelni.

**További célok:**
- Esztétikus és intuitív felhasználói felület kialakítása.
- A felhasználó teljesítményének visszajelzése a játék végén.
- Az alkalmazás offline működésének biztosítása.

## 3. Nem célkitűzések

- **Haladó szintű elemzések:** Az alkalmazás nem nyújt részletes statisztikákat vagy elemzéseket a felhasználói teljesítményről.
- **Felhasználói tartalomgenerálás:** A felhasználók nem módosíthatják vagy bővíthetik a kérdések adatbázisát.
- **Többjátékos mód:** Az alkalmazás egyéni használatra készült, nem támogatja a többjátékos módot.

## 4. Használati esetek

| **Használati eset**          | **Szereplő** | **Leírás**                                              | **Eredmény**                                              |
|-------------------------------|----------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Játék elindítása         | Felhasználó       | A felhasználó elindítja az alkalmazást.               | A kezdőképernyő megjelenik.                      |
| Kérdések megválaszolása    | Felhasználó       | A felhasználó kiválaszt egy válaszlehetőséget.      | A válasz kiértékelésre kerül, és a következő kérdés megjelenik. |
| Játék befejezése          | Felhasználó       | A felhasználó befejezi a játékot.                    | Az eredményképernyő megjelenik, amely tartalmazza az elért pontokat. |

## 5. Képernyőtervek

- **Kezdőképernyő:** Egy üdvözlő üzenet és egy "Kezdés" gomb.
- **Kérdésképernyő:** A kérdés szövege és a válaszlehetőségek.
- **Eredményképernyő:** Az elért pontszám, valamint az "Újra próbálom" és "Kilépés" gombok.

## 6. Forgatókönyvek

- **Sikeres játékmenet:** A felhasználó elindítja a játékot, megválaszolja a kérdéseket, és megtekinti az eredményét.
- **Játék megszakítása:** A felhasználó bármikor megszakíthatja a játékot a bezárás gomb megnyomásával.

## 7. Funkció-követelmény megfeleltetés

| **Funkció**                | **Követelmény**                              |
|-----------------------------|--------------------------------------------|
| Kezdőképernyő megjelenítése | Felhasználóbarát felület                     |
| Kérdések megjelenítése     | Véletlenszerű kérdések generálása          |
| Pontszámok kijelzése         | Teljesítmény értékelése                    |
| Újrajátszás lehetősége     | Játék újraindítása                         |

## 8. Következtetés

A fenti funkcionális specifikáció meghatározza az alkalmazás alapvető működését. A további fejlesztési fázisban a részletes tervezés, a felhasználói felület kialakítása és a kódolás kerül sor.

**Megjegyzés:** A fenti dokumentum egy egyszerű példát mutat be a funkcionális specifikációra. Egy komplexebb rendszer esetén a követelményeket részletesebben kell kidolgozni, és lehetőség szerint diagramokkal, táblázatokkal is illusztrálni.

### Figyeljünk arra, hogy:

- A követelmények egyértelműek és konkrétak legyenek.
- A használati esetek lefedjék az összes fontos funkciót.
- A képernyőtervek vizuálisan is ábrázolják az alkalmazás felépítését.
- A forgatókönyvek a felhasználói interakciókat modellezik.

### A továbbiakban érdemes lehet kitérni a következőkre:

- **Nem funkcionális követelmények:** teljesítmény, biztonság, hozzáférhetőség.
- **Technikai megvalósítás:** használt technológiák, architektúra.
- **Teszt esetek:** a követelmények ellenőrzésére szolgáló tesztek.

