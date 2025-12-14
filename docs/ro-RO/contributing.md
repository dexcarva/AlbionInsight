# Contribuind la Albion Insight

**[Citește în Română](contributing.md)** | **[Read in English](../en/contributing.md)**

În primul rând, îți mulțumim că iei în considerare să contribui la Albion Insight! Oameni ca tine fac din Albion Insight un instrument atât de grozav pentru comunitatea Albion Online.

## Cuprins

- [Codul de Conduită](#codul-de-conduită)
- [Cum Pot Contribui?](#cum-pot-contribui)
  - [Raportarea Erorilor (Bugs)](#raportarea-erorilor-bugs)
  - [Sugestii de Funcționalități](#sugestii-de-funcționalități)
  - [Contribuții de Cod](#contribuții-de-cod)
  - [Documentație](#documentație)
- [Configurare pentru Dezvoltare](#configurare-pentru-dezvoltare)
- [Standarde de Codare](#standarde-de-codare)
- [Mesaje de Commit](#mesaje-de-commit)
- [Procesul de Pull Request](#procesul-de-pull-request)

## Codul de Conduită

Acest proiect și toți cei care participă la el sunt guvernați de Codul nostru de Conduită. Prin participare, se așteaptă să susțineți acest cod. Vă rugăm să raportați comportamentul inacceptabil către menținătorii proiectului.

## Cum Pot Contribui?

### Raportarea Erorilor (Bugs)

Înainte de a crea rapoarte de erori, vă rugăm să verificați problemele existente pentru a evita duplicarea. Când creați un raport de eroare, includeți cât mai multe detalii posibil folosind șablonul de raport de eroare.

**Rapoartele de erori bune includ:**
- Un titlu clar și descriptiv
- Pași exacți pentru a reproduce problema
- Comportamentul așteptat versus cel real
- Capturi de ecran, dacă este cazul
- Detaliile mediului dumneavoastră (Sistem de Operare, versiunea Python, etc.)
- Jurnale sau mesaje de eroare relevante

### Sugestii de Funcționalități

Sugestiile de funcționalități sunt binevenite! Vă rugăm să utilizați șablonul de cerere de funcționalitate și să furnizați:
- O descriere clară a funcționalității
- Problema pe care o rezolvă
- Abordări posibile de implementare
- Orice alternative pe care le-ați luat în considerare

### Contribuții de Cod

Ne plac contribuțiile de cod! Iată cum să începeți:

1. **Fork-uiți depozitul** și creați-vă ramura din `master`
2. **Configurați mediul de dezvoltare** (vezi Configurare pentru Dezvoltare mai jos)
3. **Faceți modificările** urmând standardele noastre de codare
4. **Testați-vă modificările** în detaliu
5. **Actualizați documentația** dacă este necesar
6. **Trimiteți un pull request** folosind șablonul nostru de PR

### Documentație

Îmbunătățirile aduse documentației sunt întotdeauna apreciate! Aceasta include:
- Fișierele README
- Paginile Wiki
- Comentariile de cod
- Tutoriale și ghiduri
- Traduceri în alte limbi

## Configurare pentru Dezvoltare

### Pre-condiții

- Python 3.8 sau o versiune mai nouă
- Git
- Privilegii de Root/Administrator (pentru capturarea pachetelor)

### Configurarea Mediului Dumneavoastră

\`\`\`bash
# Clonează fork-ul tău
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Creează un mediu virtual
python3 -m venv venv

# Activează mediul virtual
# Pe Linux/macOS:
source venv/bin/activate
# Pe Windows:
venv\Scripts\activate

# Instalează dependențele
pip install -r requirements.txt

# Instalează dependențele de dezvoltare
pip install -r requirements-dev.txt

# Configurează hook-urile pre-commit (opțional, dar recomandat)
pre-commit install
\`\`\`

### Rularea Aplicației

\`\`\`bash
# Pe Linux/macOS:
sudo venv/bin/python3 -m albion_insight

# Pe Windows (ca Administrator):
python -m albion_insight
\`\`\`

## Standarde de Codare

Urmăm ghidurile de stil PEP 8 pentru codul Python. Vă rugăm să vă asigurați că codul dumneavoastră respectă aceste standarde:

- Utilizați 4 spații pentru indentare (fără tab-uri)
- Lungimea maximă a liniei de 100 de caractere
- Utilizați nume de variabile și funcții semnificative
- Adăugați docstrings la toate funcțiile și clasele
- Includeți sugestii de tip (type hints) acolo unde este cazul
- Păstrați funcțiile concentrate și concise

**Instrumente de ajutor (rulați-le înainte de a comite):**

\`\`\`bash
# Formatează-ți codul cu black și isort
black albion_insight/
isort albion_insight/

# Verifică problemele de stil
flake8 albion_insight/

# Rulează verificarea tipurilor
mypy albion_insight/

# Rulează linter-ul
pylint albion_insight/
\`\`\`

**Verificări Automate de Calitate:**

Folosim hook-uri `pre-commit` pentru a verifica automat calitatea codului înainte de commit-uri. Dacă ați instalat hook-urile pre-commit, acestea vor rula automat la `git commit`. Pentru a le rula manual:

\`\`\`bash
pre-commit run --all-files
\`\`\`

## Mesaje de Commit

Urmăm specificația **Conventional Commits** pentru mesaje de commit clare și structurate:

**Format:**
\`\`\`
<tip>(<domeniu>): <subiect>

<body>

<footer>
\`\`\`

**Tipuri:**
- `feat:` O nouă funcționalitate
- `fix:` O corecție de eroare
- `docs:` Modificări de documentație
- `style:` Modificări de stil de cod (formatare, punct și virgulă lipsă, etc.)
- `refactor:` Refactorizare de cod fără modificări de funcționalitate
- `perf:` Îmbunătățiri de performanță
- `test:` Adăugarea sau actualizarea testelor
- `chore:` Modificări ale procesului de construire, dependențelor sau instrumentelor

**Exemple:**
\`\`\`
feat(damage-meter): Adaugă funcționalitate de export pentru rapoartele DPS

Implementează funcționalitatea de export CSV pentru datele contorului de daune,
permițând utilizatorilor să salveze statisticile de luptă pentru analiză.

Closes #123

fix(network): Rezolvă problema de parsare a pachetelor IPv6

Actualizează parserul de pachete pentru a gestiona corect adresele IPv6
în analiza traficului de rețea.

docs(readme): Adaugă instrucțiuni de instalare pentru macOS

style(code): Formatează importurile cu isort

refactor(core): Reorganizează modulul de urmărire a rețelei
\`\`\`

## Procesul de Pull Request

1. **Actualizați documentația** pentru orice modificări aduse funcționalității
2. **Adăugați teste** pentru funcționalități noi sau corecții de erori
3. **Asigurați-vă că toate testele trec** înainte de a trimite
4. **Actualizați README.md** dacă este necesar
5. **Completați șablonul de PR** în întregime
6. **Legați problemele conexe** în descrierea PR-ului dumneavoastră
7. **Solicitați revizuirea** de la menținători
8. **Abordați feedback-ul** prompt și profesional

### Lista de Verificare PR

Înainte de a trimite PR-ul dumneavoastră, asigurați-vă că:
- [ ] Codul respectă ghidurile de stil ale proiectului
- [ ] Auto-revizuirea este finalizată
- [ ] Comentarii adăugate la secțiunile de cod complexe
- [ ] Documentația este actualizată
- [ ] Nu sunt generate avertismente noi
- [ ] Testele sunt adăugate și trec
- [ ] Modificările dependente sunt îmbinate

## Întrebări?

Nu ezitați să puneți întrebări! Puteți:
- Deschide o problemă cu eticheta "question"
- Vă alăturați discuțiilor comunității noastre
- Contactați menținătorii

Vă mulțumim pentru contribuția la Albion Insight! Eforturile dumneavoastră ajută la îmbunătățirea acestui instrument pentru întreaga comunitate Albion Online.
