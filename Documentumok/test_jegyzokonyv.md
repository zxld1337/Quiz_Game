# Quiz Game – Teszt Jegyzőkönyv

## Alapinformációk
**Projekt neve:** Quiz Game  
**Tesztelés dátuma:** 2025.01.19  
**Tesztet végezte:** Levente  

## Tesztelés Célja
Az alkalmazás funkcionalitásának és stabilitásának ellenőrzése, beleértve a különböző funkcionális és nem-funkcionális követelmények teljesülését.

## Tesztkörnyezet
- **Operációs rendszer:** Windows 11 Home
- **Hardver:** Ryzen 9 5900HS
- **Szoftverkörnyezet:** Python 3.12.6, Tkinter

## Tesztelési Módszer
Manuális tesztelés, a tesztelési forgatókönyvek alapján. A hibák dokumentálása az eredményekkel és a megfigyelésekkel együtt.

## Tesztelési Forgatókönyvek

### 1. Forgatókönyv: Az alkalmazás indítása
- **Elvárt eredmény:** Az alkalmazás sikeresen elindul, és megjelenik a kezdőképernyő.
- **Teszt eredmény:** Sikeres
- **Megjegyzés:** Gyors indulás.

### 2. Forgatókönyv: Kérdések megjelenítése
- **Elvárt eredmény:** A kérdések véletlenszerűen jelennek meg, és helyes formátumban jelennek meg a válaszlehetőségekkel.
- **Teszt eredmény:** Sikeres
- **Megjegyzés:** Nem történt ismétlődés.

### 3. Forgatókönyv: Válasz kiválasztása
- **Elvárt eredmény:** A felhasználó által kiválasztott válasz után a rendszer azonnal értékeli a helyességet.
- **Teszt eredmény:** Sikeres
- **Megjegyzés:** Müködés, az elvártnak megfelelően történt.

### 4. Forgatókönyv: Pontszámok megjelenítése
- **Elvárt eredmény:** A játék végén a rendszer helyesen összesíti és kijelzi a pontszámokat.
- **Teszt eredmény:** Sikeres
- **Megjegyzés:** A pontszám a valóságot tükrözte.

### 5. Forgatókönyv: Játék újraindítása
- **Elvárt eredmény:** Az újrajátszás gomb megnyomásával a játék kezdődik elölről, tiszta állapottal.
- **Teszt eredmény:** Sikeres
- **Megjegyzés:** Először egy hiba miatt kifagyott, majd kijavítás után már a játék indult. 

## Hibajegyzék
| Azonosító | Hiba Leírása                    | Prioritás  | Állapot     |
|-------------|-------------------------------|------------|-------------|
| H001        | Játék újraindítás hiba        | Magas      | Javítva     |


## Összegzés
Az alkalmazás tesztelése során 1 hibát azonosítotam, amelyek közül 1 került kijavításra. Az általános működés megfelel az elvárásoknak.

