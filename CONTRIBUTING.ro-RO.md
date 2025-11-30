# Contribuind la Albion Insight

**[Citiți în Engleză](CONTRIBUTING.md)** | **[Citiți în Portugheză (Brazilia)](CONTRIBUTING.pt-BR.md)** | **[Citiți în Portugheză (Portugalia)](CONTRIBUTING.pt-PT.md)**
<!-- Aici vor fi adăugate mai multe linkuri de traducere -->

În primul rând, vă mulțumim că luați în considerare să contribuiți la Albion Insight! Oameni ca voi fac din Albion Insight un instrument atât de grozav pentru comunitatea Albion Online.

## Cuprins
	
- [Codul de Conduită](#codul-de-conduită)
- [Cum pot contribui?](#cum-pot-contribui)
  - [Raportarea Erorilor](#raportarea-erorilor)
  - [Sugestii de Funcționalități](#sugestii-de-funcționalități)
  - [Contribuții de Cod](#contribuții-de-cod)
  - [Documentație](#documentație)
- [Configurarea pentru Dezvoltare](#configurarea-pentru-dezvoltare)
- [Standarde de Codare](#standarde-de-codare)
- [Mesaje de Commit](#mesaje-de-commit)
- [Procesul de Pull Request](#procesul-de-pull-request)

## Codul de Conduită

Acest proiect și toți cei care participă la el sunt guvernați de Codul nostru de Conduită. Prin participare, se așteaptă să respectați acest cod. Vă rugăm să raportați comportamentul inacceptabil către întreținătorii proiectului.

## Cum pot contribui?

### Raportarea Erorilor

Înainte de a crea rapoarte de erori, vă rugăm să verificați problemele existente pentru a evita duplicarea. Când creați un raport de eroare, includeți cât mai multe detalii posibil folosind șablonul de raport de eroare.

**Rapoartele de erori bune includ:**
- Un titlu clar și descriptiv
- Pași exacți pentru a reproduce problema
- Comportamentul așteptat versus cel real
- Capturi de ecran, dacă este cazul
- Detaliile mediului dumneavoastră (OS, versiunea Python, etc.)
- Jurnale sau mesaje de eroare relevante

### Sugestii de Funcționalități

Sugestiile de funcționalități sunt binevenite! Vă rugăm să utilizați șablonul de solicitare de funcționalitate și să furnizați:
- O descriere clară a funcționalității
- Problema pe care o rezolvă
- Abordări posibile de implementare
- Orice alternative pe care le-ați luat în considerare

### Contribuții de Cod

Ne plac contribuțiile de cod! Iată cum să începeți:

1. **Fork-uiți depozitul** și creați ramura voastră din `master`
2. **Configurați mediul de dezvoltare** (vezi Configurarea pentru Dezvoltare mai jos)
3. **Faceți modificările** urmând standardele noastre de codare
4. **Testați modificările** temeinic
5. **Actualizați documentația** dacă este necesar
6. **Trimiteți un pull request** folosind șablonul nostru de PR

### Documentație

Îmbunătățirile aduse documentației sunt întotdeauna apreciate! Aceasta include:
- Fișiere README
- Pagini Wiki
- Comentarii de cod
- Tutoriale și ghiduri
- Traduceri în alte limbi

## Configurarea pentru Dezvoltare

### Cerințe Prealabile

- Python 3.8 sau mai nou
- Git
- Privilegii de Root/Administrator (pentru capturarea pachetelor)

### Configurarea Mediului Vostru

```bash
# Clonați fork-ul vostru
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Creați un mediu virtual
python3 -m venv venv

# Activați mediul virtual
# Pe Linux/macOS:
source venv/bin/activate
# Pe Windows:
venv\Scripts\activate

# Instalați dependențele
pip install -r requirements.txt

# Instalați dependențele de dezvoltare
pip install pylint flake8 black pytest
```

### Rularea Aplicației

```bash
# Pe Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# Pe Windows (ca Administrator):
python albion_insight.py
```

## Standarde de Codare

Urmăm ghidurile de stil PEP 8 pentru codul Python. Vă rugăm să vă asigurați că codul vostru aderă la aceste standarde:

- Folosiți 4 spații pentru indentare (fără tab-uri)
- Lungimea maximă a liniei de 100 de caractere
- Folosiți nume semnificative pentru variabile și funcții
- Adăugați docstrings la toate funcțiile și clasele
- Includeți sugestii de tip (type hints) acolo unde este cazul
- Păstrați funcțiile concentrate și concise

**Instrumente de ajutor:**
```bash
# Formatați codul vostru cu black
black albion_insight.py

# Verificați problemele de stil
flake8 albion_insight.py

# Rulați linter-ul
pylint albion_insight.py
```

## Mesaje de Commit

Scrieți mesaje de commit clare și semnificative:

- Folosiți timpul prezent ("Adaugă funcționalitate" nu "A adăugat funcționalitate")
- Folosiți modul imperativ ("Mută cursorul la..." nu "Mută cursorul la...")
- Limitați prima linie la 72 de caractere
- Faceți referire la probleme și pull request-uri atunci când sunt relevante

**Exemple:**
```
Adaugă funcționalitatea de export a contorului de daune
	
Repară parsarea pachetelor de rețea pentru conexiunile IPv6
	
Actualizează README cu instrucțiunile de instalare macOS
	
Închide #123
```

## Procesul de Pull Request

1. **Actualizați documentația** pentru orice modificări ale funcționalității
2. **Adăugați teste** pentru funcționalități noi sau remedieri de erori
3. **Asigurați-vă că toate testele trec** înainte de trimitere
4. **Actualizați README.md** dacă este necesar
5. **Completați șablonul PR** în întregime
6. **Legați problemele conexe** în descrierea PR-ului vostru
7. **Solicitați revizuirea** de la întreținători
8. **Adresați feedback-ul** prompt și profesional

### Lista de Verificare PR

Înainte de a trimite PR-ul vostru, asigurați-vă că:
- [ ] Codul respectă ghidurile de stil ale proiectului
- [ ] Auto-revizuirea este finalizată
- [ ] Comentariile sunt adăugate la secțiunile de cod complexe
- [ ] Documentația este actualizată
- [ ] Nu au fost generate avertismente noi
- [ ] Testele sunt adăugate și trec
- [ ] Modificările dependente sunt îmbinate

## Întrebări?

Nu ezitați să puneți întrebări! Puteți:
- Deschide un problemă cu eticheta "question"
- Vă alăturați discuțiilor comunității noastre
- Contactați întreținătorii

Vă mulțumim pentru contribuția la Albion Insight! Eforturile voastre ajută la îmbunătățirea acestui instrument pentru întreaga comunitate Albion Online.
