# Hozzájárulás az Albion Insight-hoz

**[Read in English (Angolul olvasni)](CONTRIBUTING.md)** | **[Leia em Português (Brazíliai portugálul olvasni)](CONTRIBUTING.pt-BR.md)** | **[Leer en Español (Spanyolul olvasni)](CONTRIBUTING.es-ES.md)** | **[Lire en Français (Franciául olvasni)](CONTRIBUTING.fr-FR.md)**

Először is, köszönjük, hogy fontolóra veszi a hozzájárulást az Albion Insight-hoz! Az Albion Insight-ot az Albion Online közösség számára nagyszerű eszközzé tevő emberek, mint Ön.

## Tartalomjegyzék

- [Magatartási Kódex](#magatartási-kódex)
- [Hogyan járulhatok hozzá?](#hogyan-járulhatok-hozzá)
  - [Hibák Jelentése](#hibák-jelentése)
  - [Funkciók Javaslata](#funkciók-javaslata)
  - [Kód Hozzájárulások](#kód-hozzájárulások)
  - [Dokumentáció](#dokumentáció)
- [Fejlesztési Környezet Beállítása](#fejlesztési-környezet-beállítása)
- [Kódolási Szabványok](#kódolási-szabványok)
- [Commit Üzenetek](#commit-üzenetek)
- [Pull Request Folyamat](#pull-request-folyamat)

## Magatartási Kódex

Ezt a projektet és minden résztvevőjét a Magatartási Kódexünk szabályozza. A részvétellel elvárható, hogy betartsa ezt a kódexet. Kérjük, jelentse a nem elfogadható viselkedést a projekt karbantartóinak.

## Hogyan járulhatok hozzá?

### Hibák Jelentése

Mielőtt hibajelentést készítene, kérjük, ellenőrizze a meglévő hibákat a duplikáció elkerülése érdekében. Amikor hibajelentést készít, a hibajelentési sablon segítségével a lehető legtöbb részletet adja meg.

**A jó hibajelentések tartalmazzák:**
- Világos és leíró cím
- A probléma reprodukálásának pontos lépései
- Várható vs. tényleges viselkedés
- Képernyőképek, ha alkalmazható
- Az Ön környezeti adatai (OS, Python verzió stb.)
- Releváns naplók vagy hibaüzenetek

### Funkciók Javaslata

A funkciójavaslatokat szívesen fogadjuk! Kérjük, használja a funkciókérési sablont, és adja meg:
- A funkció világos leírását
- A problémát, amit megold
- Lehetséges megvalósítási megközelítéseket
- Bármely alternatívát, amit fontolóra vett

### Kód Hozzájárulások

Szeretjük a kód hozzájárulásokat! Íme, hogyan kezdheti el:

1. **Forkolja a tárolót** és hozza létre az ágát a `master` ágból.
2. **Állítsa be a fejlesztési környezetét** (lásd alább a Fejlesztési Környezet Beállítása részt).
3. **Végezze el a változtatásokat** a kódolási szabványaink szerint.
4. **Tesztelje a változtatásait** alaposan.
5. Szükség esetén **frissítse a dokumentációt**.
6. **Küldjön be egy Pull Requestet** a PR sablonunk segítségével.

### Dokumentáció

A dokumentáció javítását mindig nagyra értékeljük! Ez magában foglalja:
- README fájlok
- Wiki oldalak
- Kód megjegyzések
- Oktatóanyagok és útmutatók
- Fordítások más nyelvekre

## Fejlesztési Környezet Beállítása

### Előfeltételek

- Python 3.8 vagy újabb
- Git
- Root/Rendszergazdai jogosultságok (csomag rögzítéshez)

### Környezet Beállítása

```bash
# Klónozza a forkot
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Hozzon létre egy virtuális környezetet
python3 -m venv venv

# Aktiválja a virtuális környezetet
# Linuxon/macOS-en:
source venv/bin/activate
# Windowson:
venv\Scripts\activate

# Függőségek telepítése
pip install -r requirements.txt

# Fejlesztési függőségek telepítése
pip install pylint flake8 black pytest
```

### Az Alkalmazás Futtatása

```bash
# Linuxon/macOS-en:
sudo venv/bin/python3 albion_insight.py

# Windowson (Rendszergazdaként):
python albion_insight.py
```

## Kódolási Szabványok

A Python kódra a PEP 8 stílusirányelveket követjük. Kérjük, győződjön meg róla, hogy a kódja megfelel ezeknek a szabványoknak:

- 4 szóközt használjon a behúzáshoz (nincs tabulátor)
- Maximális sorhossz 100 karakter
- Használjon értelmes változó- és függvénynéveket
- Adjon hozzá docstringeket minden függvényhez és osztályhoz
- Használjon típus-tippeket, ahol megfelelő
- Tartsa a függvényeket fókuszáltnak és tömörnek

**Segítő eszközök:**
```bash
# Formázza a kódját black-kel
black albion_insight.py

# Ellenőrizze a stílusproblémákat
flake8 albion_insight.py

# Futtassa a lintert
pylint albion_insight.py
```

## Commit Üzenetek

Írjon világos és értelmes commit üzeneteket:

- Használja a jelen időt ("Add feature" ne "Added feature")
- Használja a felszólító módot ("Move cursor to..." ne "Moves cursor to...")
- Korlátozza az első sort 72 karakterre
- Hivatkozzon a releváns hibákra és Pull Requestekre

**Példák:**
```
Sebzésmérő exportálási funkció hozzáadása

Hálózati csomag elemzés javítása IPv6 kapcsolatokhoz

README frissítése macOS telepítési utasításokkal

Closes #123
```

## Pull Request Folyamat

1. **Frissítse a dokumentációt** a funkcionalitás bármely változásához.
2. **Adjon hozzá teszteket** az új funkciókhoz vagy hibajavításokhoz.
3. **Győződjön meg róla, hogy minden teszt sikeres** a beküldés előtt.
4. Szükség esetén **frissítse a README.md-t**.
5. **Töltse ki a PR sablont** teljesen.
6. **Kapcsolja össze a kapcsolódó hibákat** a PR leírásában.
7. **Kérjen felülvizsgálatot** a karbantartóktól.
8. **Kezelje a visszajelzéseket** gyorsan és professzionálisan.

### PR Ellenőrzőlista

A PR beküldése előtt győződjön meg róla:
- [ ] A kód követi a projekt stílusirányelveit
- [ ] Az önellenőrzés befejeződött
- [ ] Megjegyzések hozzáadva a komplex kódszakaszokhoz
- [ ] A dokumentáció frissítve
- [ ] Nincs új figyelmeztetés generálva
- [ ] Tesztek hozzáadva és sikeresek
- [ ] Függő változtatások egyesítve

## Kérdések?

Ne habozzon kérdezni! A következőket teheti:
- Nyisson egy hibát "question" címkével
- Csatlakozzon a közösségi beszélgetéseinkhez
- Vegye fel a kapcsolatot a karbantartókkal

Köszönjük, hogy hozzájárul az Albion Insight-hoz! Az Ön erőfeszítései segítenek abban, hogy ez az eszköz jobb legyen az egész Albion Online közösség számára.
