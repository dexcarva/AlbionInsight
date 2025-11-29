# Panustamisjuhised (Eesti keeles)

Täname teid huvi eest panustada **Albion Insight** projekti! Teie panus aitab meil luua parima platvormiülese statistikaanalüüsi tööriista Albion Online'i kogukonnale.

Palun lugege need juhised hoolikalt läbi.

## Käitumisjuhend

See projekt järgib [Käitumisjuhendit](CODE_OF_CONDUCT.md). Oodatakse, et kõik osalejad järgivad seda juhendit.

## Kuidas panustada

Panustamiseks on mitu võimalust:

### 1. Vigadest teatamine (Bug Reports)

Kui leiate vea, palun avage [uus probleem (Issue)](https://github.com/dexcarva/AlbionInsight/issues/new/choose) ja valige veateate mall.

*   **Enne uue probleemi avamist** kontrollige, kas sarnane probleem on juba avatud.
*   Lisage võimalikult palju teavet:
    *   Millist operatsioonisüsteemi te kasutate (Linux, Windows, macOS)?
    *   Millist Pythoni versiooni te kasutate?
    *   Täpsed sammud vea reprodutseerimiseks.
    *   Käivitage rakendus silumisrežiimis ja lisage veateade (stack trace).

### 2. Funktsioonide taotlemine (Feature Requests)

Kui teil on idee uue funktsiooni jaoks, palun avage [uus probleem (Issue)](https://github.com/dexcarva/AlbionInsight/issues/new/choose) ja valige funktsioonitaotluse mall.

*   Selgitage selgelt, millist probleemi see funktsioon lahendaks.
*   Kirjeldage, kuidas see peaks töötama.

### 3. Koodi panustamine (Code Contributions)

Ootame koodi panuseid! Järgige palun alltoodud samme:

1.  **Kahvel (Fork)** hoidla.
2.  **Kloonige** oma kahvel: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  **Looge uus haru** oma muudatuste jaoks: `git checkout -b feature/minu-uus-funktsioon` või `git checkout -b fix/vea-parandus`
4.  **Tehke muudatused.** Järgige projekti koodistiili.
5.  **Testige** oma muudatusi.
6.  **Commit'ige** oma muudatused, kasutades selgeid ja kirjeldavaid commit-sõnumeid (vt allpool).
7.  **Lükake** haru oma kahvlisse: `git push origin feature/minu-uus-funktsioon`
8.  **Avage Pull Request (PR)** põhihoidlasse.

#### Commit-sõnumite standardid

Kasutame [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standardit.

*   **`feat`**: Uus funktsioon.
*   **`fix`**: Veaparandus.
*   **`docs`**: Ainult dokumentatsiooni muudatused.
*   **`style`**: Koodi stiili muudatused (nt vormindamine, semikoolonid), mis ei mõjuta koodi tähendust.
*   **`refactor`**: Koodi refaktorimine, mis ei paranda viga ega lisa funktsiooni.
*   **`perf`**: Koodi muudatus, mis parandab jõudlust.
*   **`test`**: Testide lisamine või parandamine.
*   **`chore`**: Muudatused, mis ei mõjuta lähtekoodi ega teste (nt ehitusprotsess, abivahendid).

**Näide:** `feat: Lisab kahjumõõturi funktsionaalsuse`

### 4. Dokumentatsiooni panustamine

Kui märkate vigu dokumentatsioonis või soovite lisada tõlkeid (nagu see fail!), on teie panus teretulnud.

*   **Tõlked:** Kui lisate uue keele, palun veenduge, et tõlgite nii `README.md` kui ka `CONTRIBUTING.md` failid. Lisage oma uus keel ka `README.md` faili keelte loendisse.

Täname teid veel kord, et aitate **Albion Insight** projekti paremaks muuta!
