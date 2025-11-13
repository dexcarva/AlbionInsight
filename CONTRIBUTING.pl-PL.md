# Współpraca nad Albion Insight

**[Czytaj w Angielskim](CONTRIBUTING.md)**
**[Czytaj w Niemieckim](CONTRIBUTING.de-DE.md)**
**[Czytaj w Portugalskim](CONTRIBUTING.pt-BR.md)**
**[Czytaj w Hiszpańskim](CONTRIBUTING.es-ES.md)**
**[Czytaj w Francuskim](CONTRIBUTING.fr-FR.md)**
**[Czytaj w Arabskim (اقرأ بالعربية)](CONTRIBUTING.ar-SA.md)**

Przede wszystkim, dziękujemy za rozważenie współpracy nad Albion Insight! To dzięki takim osobom jak ty, że Albion Insight jest takim wspaniałym narzędziem dla społeczności Albion Online.

## Spis Treści

- [Kodeks Postępowania](#kodeks-postępowania)
- [Jak Mogę Współpracować?](#jak-mogę-współpracować)
  - [Zgłaszanie Błędów](#zgłaszanie-błędów)
  - [Sugerowanie Funkcji](#sugerowanie-funkcji)
  - [Wkład w Kod](#wkład-w-kod)
  - [Dokumentacja](#dokumentacja)
- [Konfiguracja Środowiska Programistycznego](#konfiguracja-środowiska-programistycznego)
- [Standardy Kodowania](#standardy-kodowania)
- [Wiadomości Commita](#wiadomości-commita)
- [Proces Pull Request](#proces-pull-request)

## Kodeks Postępowania

Ten projekt i wszyscy jego uczestnicy podlegają naszemu Kodeksowi Postępowania. Uczestnicząc, zobowiązujesz się do przestrzegania tego kodeksu. Prosimy zgłaszać niedopuszczalne zachowanie opiekunom projektu.

## Jak Mogę Współpracować?

### Zgłaszanie Błędów

Przed utworzeniem raportu o błędzie, sprawdź istniejące problemy, aby uniknąć duplikatów. Kiedy tworzysz raport o błędzie, dołącz jak najwięcej szczegółów, korzystając z szablonu raportu o błędzie.

**Dobre raporty o błędach zawierają:**
- Jasny i opisowy tytuł
- Dokładne kroki do odtworzenia problemu
- Oczekiwane vs rzeczywiste zachowanie
- Zrzuty ekranu, jeśli dotyczy
- Szczegóły Twojego środowiska (OS, wersja Pythona, itp.)
- Istotne logi lub komunikaty błędów

### Sugerowanie Funkcji

Sugestie funkcji są mile widziane! Prosimy użyć szablonu żądania funkcji i podać:
- Jasny opis funkcji
- Problem, który rozwiązuje
- Możliwe podejścia do implementacji
- Wszelkie rozważane alternatywy

### Wkład w Kod

Uwielbiam wkład w kod! Oto jak zacząć:

1. **Utwórz fork repozytorium** i utwórz swoją gałąź z `master`
2. **Skonfiguruj swoje środowisko programistyczne** (zobacz Konfiguracja Środowiska Programistycznego poniżej)
3. **Wprowadź swoje zmiany** zgodnie z naszymi standardami kodowania
4. **Dokładnie przetestuj swoje zmiany**
5. **Zaktualizuj dokumentację**, jeśli jest to konieczne
6. **Prześlij pull request** korzystając z naszego szablonu PR

### Dokumentacja

Ulepszenia dokumentacji są zawsze mile widziane! Obejmuje to:
- Pliki README
- Strony Wiki
- Komentarze w kodzie
- Samouczki i przewodniki
- Tłumaczenia na inne języki

## Konfiguracja Środowiska Programistycznego

### Wymagania Wstępne

- Python 3.8 lub wyżej
- Git
- Uprawnienia Root/Administratora (do przechwytywania pakietów)

### Konfiguracja Twojego Środowiska

```bash
# Sklonuj swój fork
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Utwórz wirtualne środowisko
python3 -m venv venv

# Aktywuj wirtualne środowisko
# Na Linuksie/macOS:
source venv/bin/activate
# Na Windowsie:
venv\Scripts\activate

# Zainstaluj zależności
pip install -r requirements.txt

# Zainstaluj zależności programistyczne
pip install pylint flake8 black pytest
```

### Uruchamianie Aplikacji

```bash
# Na Linuksie/macOS:
sudo venv/bin/python3 albion_insight.py

# Na Windowsie (jako Administrator):
python albion_insight.py
```

## Standardy Kodowania

Postępujemy zgodnie z wytycznymi stylu PEP 8 dla kodu Pythona. Prosimy upewnij się, że Twój kod spełnia te standardy:

- Używaj 4 spacji do wcięcia (bez tabulatorów)
- Maksymalna długość linii 100 znaków
- Używaj znaczących nazw zmiennych i funkcji
- Dodaj docstringi do wszystkich funkcji i klas
- Dołącz wskazówki typów, gdzie to odpowiednie
- Utrzymuj funkcje skoncentrowane i zwięzłe

**Narzędzia, które mogą pomóc:**
```bash
# Sformatuj swój kod za pomocą black
black albion_insight.py

# Sprawdź problemy ze stylem
flake8 albion_insight.py

# Uruchom linter
pylint albion_insight.py
```

## Wiadomości Commita

Napisz jasne i znaczące wiadomości commita:

- Używaj czasu teraźniejszego ("Dodaj funkcję" a nie "Dodałem funkcję")
- Używaj trybu rozkazującego ("Przenieś kursor do..." a nie "Przenosi kursor do...")
- Ogranicz pierwszą linię do 72 znaków
- Odwołaj się do problemów i pull requestów, gdy jest to istotne

**Przykłady:**
```
Dodaj funkcjonalność eksportu miernika obrażeń

Napraw analizę pakietów sieciowych dla połączeń IPv6

Zaktualizuj README z instrukcjami instalacji na macOS

Zamyka #123
```

## Proces Pull Request

1. **Zaktualizuj dokumentację** dla wszelkich zmian w funkcjonalności
2. **Dodaj testy** dla nowych funkcji lub poprawek błędów
3. **Upewnij się, że wszystkie testy przechodzą** przed przesłaniem
4. **Zaktualizuj README.md**, jeśli jest to konieczne
5. **Wypełnij szablon PR** całkowicie
6. **Powiąż powiązane problemy** w opisie PR
7. **Poproś o przegląd** od opiekunów
8. **Odpowiedz na opinie** szybko i profesjonalnie

### Checklist PR

Przed przesłaniem PR upewnij się:
- [ ] Kod podąża za wytycznymi stylu projektu
- [ ] Samoocena ukończona
- [ ] Komentarze dodane do złożonych sekcji kodu
- [ ] Dokumentacja zaktualizowana
- [ ] Brak nowych ostrzeżeń
- [ ] Testy dodane i przechodzą
- [ ] Zmiany zależne scalone

## Pytania?

Nie wahaj się pytać! Możesz:
- Otworzyć problem z etykietą "question"
- Dołączyć do naszych dyskusji społeczności
- Skontaktować się z opiekunami

Dziękujemy za współpracę nad Albion Insight! Twoje wysiłki pomagają uczynić to narzędzie lepszym dla całej społeczności Albion Online.
