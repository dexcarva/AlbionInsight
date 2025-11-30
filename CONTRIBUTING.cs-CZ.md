# Přispívání do Albion Insight

**[Přečtěte si v Angličtině](CONTRIBUTING.md)** | **[Přečtěte si v Portugalštině (Brazílie)](CONTRIBUTING.pt-BR.md)** | **[Přečtěte si v Portugalštině (Portugalsko)](CONTRIBUTING.pt-PT.md)**
<!-- Zde budou přidány další odkazy na překlady -->

Nejprve děkujeme, že zvažujete přispět do Albion Insight! Jsou to lidé jako vy, kteří dělají z Albion Insight tak skvělý nástroj pro komunitu Albion Online.

## Obsah
	
- [Kodex chování](#kodex-chování)
- [Jak mohu přispět?](#jak-mohu-přispět)
  - [Hlášení chyb](#hlášení-chyb)
  - [Navrhování funkcí](#navrhování-funkcí)
  - [Příspěvky kódu](#příspěvky-kódu)
  - [Dokumentace](#dokumentace)
- [Nastavení pro vývoj](#nastavení-pro-vývoj)
- [Standardy kódování](#standardy-kódování)
- [Zprávy commitů](#zprávy-commitů)
- [Proces Pull Requestu](#proces-pull-requestu)

## Kodex chování

Tento projekt a všichni, kdo se na něm podílejí, se řídí naším Kodexem chování. Očekává se, že se budete tímto kodexem řídit. Nahlaste prosím nepřijatelné chování správcům projektu.

## Jak mohu přispět?

### Hlášení chyb

Před vytvořením hlášení o chybě zkontrolujte existující problémy, abyste se vyhnuli duplicitám. Při vytváření hlášení o chybě uveďte co nejvíce podrobností pomocí šablony pro hlášení chyb.

**Dobré hlášení o chybě zahrnuje:**
- Jasný a popisný název
- Přesné kroky k reprodukci problému
- Očekávané vs. skutečné chování
- Snímky obrazovky, pokud jsou relevantní
- Podrobnosti o vašem prostředí (OS, verze Pythonu atd.)
- Relevantní protokoly nebo chybové zprávy

### Navrhování funkcí

Návrhy funkcí jsou vítány! Použijte prosím šablonu pro požadavek na funkci a uveďte:
- Jasný popis funkce
- Problém, který řeší
- Možné přístupy k implementaci
- Jakékoli alternativy, které jste zvážili

### Příspěvky kódu

Milujeme příspěvky kódu! Zde je návod, jak začít:

1. **Forkněte repozitář** a vytvořte svou větev z `master`
2. **Nastavte si vývojové prostředí** (viz Nastavení pro vývoj níže)
3. **Proveďte své změny** podle našich standardů kódování
4. **Důkladně otestujte své změny**
5. **Aktualizujte dokumentaci**, pokud je to potřeba
6. **Odešlete pull request** pomocí naší šablony PR

### Dokumentace

Vylepšení dokumentace jsou vždy vítána! To zahrnuje:
- Soubory README
- Stránky Wiki
- Komentáře ke kódu
- Návody a průvodce
- Překlady do jiných jazyků

## Nastavení pro vývoj

### Předpoklady

- Python 3.8 nebo vyšší
- Git
- Oprávnění root/administrátora (pro zachytávání paketů)

### Nastavení vašeho prostředí

```bash
# Naklonujte svůj fork
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Vytvořte virtuální prostředí
python3 -m venv venv

# Aktivujte virtuální prostředí
# Na Linuxu/macOS:
source venv/bin/activate
# Na Windows:
venv\Scripts\activate

# Nainstalujte závislosti
pip install -r requirements.txt

# Nainstalujte vývojové závislosti
pip install pylint flake8 black pytest
```

### Spuštění aplikace

```bash
# Na Linuxu/macOS:
sudo venv/bin/python3 albion_insight.py

# Na Windows (jako Administrátor):
python albion_insight.py
```

## Standardy kódování

Řídíme se stylovými pokyny PEP 8 pro kód Pythonu. Ujistěte se, že váš kód dodržuje tyto standardy:

- Použijte 4 mezery pro odsazení (žádné tabulátory)
- Maximální délka řádku 100 znaků
- Použijte smysluplné názvy proměnných a funkcí
- Přidejte docstringy ke všem funkcím a třídám
- Použijte typové nápovědy, kde je to vhodné
- Udržujte funkce zaměřené a stručné

**Nástroje, které vám pomohou:**
```bash
# Formátujte svůj kód pomocí black
black albion_insight.py

# Zkontrolujte problémy se stylem
flake8 albion_insight.py

# Spusťte linter
pylint albion_insight.py
```

## Zprávy commitů

Pište jasné a smysluplné zprávy commitů:

- Použijte přítomný čas ("Přidat funkci" ne "Přidal funkci")
- Použijte rozkazovací způsob ("Přesunout kurzor na..." ne "Přesouvá kurzor na...")
- Omezte první řádek na 72 znaků
- Odkazujte na problémy a pull requesty, když je to relevantní

**Příklady:**
```
Přidat funkcionalitu exportu poškození
	
Opravit parsování síťových paketů pro připojení IPv6
	
Aktualizovat README s pokyny pro instalaci na macOS
	
Uzavírá #123
```

## Proces Pull Requestu

1. **Aktualizujte dokumentaci** pro jakékoli změny funkcionality
2. **Přidejte testy** pro nové funkce nebo opravy chyb
3. **Ujistěte se, že všechny testy projdou** před odesláním
4. **Aktualizujte README.md**, pokud je to potřeba
5. **Kompletně vyplňte šablonu PR**
6. **Propojte související problémy** ve svém popisu PR
7. **Požádejte o kontrolu** od správců
8. **Řešte zpětnou vazbu** rychle a profesionálně

### Kontrolní seznam PR

Před odesláním vašeho PR se ujistěte, že:
- [ ] Kód dodržuje stylové pokyny projektu
- [ ] Vlastní kontrola dokončena
- [ ] Komentáře přidány ke složitým sekcím kódu
- [ ] Dokumentace aktualizována
- [ ] Nebyla vygenerována žádná nová varování
- [ ] Testy přidány a procházejí
- [ ] Závislé změny sloučeny

## Dotazy?

Neváhejte se zeptat! Můžete:
- Otevřít problém se štítkem "question"
- Připojit se k našim komunitním diskusím
- Kontaktovat správce

Děkujeme, že přispíváte do Albion Insight! Vaše úsilí pomáhá zlepšit tento nástroj pro celou komunitu Albion Online.
