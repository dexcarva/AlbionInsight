# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Read this in German (Lesen Sie dies auf Deutsch)](README.de-DE.md)**
**[Read this in Portuguese (Leia em Português)](README.pt-BR.md)**
**[Read this in Spanish (Leer en Español)](README.es-ES.md)**
**[Read this in French (Lire en Français)](README.fr-FR.md)**
**[Read this in Italian (Leggi in Italiano)](README.it-IT.md)**
**[Read this in Simplified Chinese (阅读简体中文)](README.zh-CN.md)**
**[Read this in Russian (Прочитать на русском)](README.ru-RU.md)**
**[Read this in Japanese (日本語で読む)](README.ja-JP.md)**
**[Read this in Arabic (اقرأ هذا بالعربية)](README.ar-SA.md)**
**[Read this in Turkish (Türkçe Oku)](README.tr-TR.md)**
**[Read this in Korean (한국어로 읽기)](README.ko-KR.md)**
**[Read this in Dutch (Lees dit in het Nederlands)](README.nl-NL.md)**
**[Read this in Polish (Czytaj po polsku)](README.pl-PL.md)**
**[Read this in Hindi (इसे हिंदी में पढ़ें)](README.hi-IN.md)**
**[Read this in Swedish (Läs detta på svenska)](README.sv-SE.md)**
**[Read this in Vietnamese (Đọc bằng tiếng Việt)](README.vi-VN.md)**
**[Read this in Greek (Διαβάστε στα Ελληνικά)](README.el-GR.md)**

**Το Albion Insight** είναι ένα εργαλείο ανάλυσης στατιστικών πολλαπλών πλατφορμών (Linux, Windows, macOS) για το παιχνίδι Albion Online, επανεφαρμοσμένο σε **Python** χρησιμοποιώντας το πλαίσιο **Flet**. Έχει σχεδιαστεί για να παρακολουθεί στατιστικά στοιχεία εντός του παιχνιδιού σε πραγματικό χρόνο, συμπεριλαμβανομένων των silver, fame και δεδομένων μάχης (Damage Meter), αναλύοντας την κίνηση του δικτύου.

Αυτό το έργο είναι μια σύγχρονη, ανοιχτού κώδικα εναλλακτική λύση στο αρχικό εργαλείο `AlbionOnline-StatisticsAnalysis` που βασιζόταν σε C#/WPF, εστιάζοντας στη συμβατότητα πολλαπλών πλατφορμών και την ευκολία χρήσης.

## Χαρακτηριστικά

*   **Συμβατότητα Πολλαπλών Πλατφορμών:** Λειτουργεί εγγενώς σε Linux, Windows και macOS.
*   **Παρακολούθηση σε Πραγματικό Χρόνο:** Χρησιμοποιεί τη βιβλιοθήκη `Scapy` για να ανιχνεύει πακέτα UDP στις θύρες του Albion Online (5055, 5056, 5058).
*   **Δομή Μετρητή Ζημιάς:** Περιλαμβάνει τις απαραίτητες δομές δεδομένων και διεπαφή χρήστη για την εμφάνιση ζωντανών στατιστικών μάχης (Προκληθείσα Ζημιά, Θεραπεία, DPS).
*   **Σύγχρονη Διεπαφή Χρήστη (UI):** Κατασκευασμένο με Flet, παρέχοντας μια γρήγορη, εγγενή εφαρμογή επιφάνειας εργασίας.
*   **Διαχείριση Συνεδριών:** Επιτρέπει την έναρξη, διακοπή, επαναφορά και αποθήκευση στατιστικών συνεδρίας.

## Προαπαιτούμενα

*   Python 3.8+
*   Βιβλιοθήκες **Flet** και **Scapy**.
*   **Προνόμια Root/Διαχειριστή:** Απαραίτητα για τη λήψη πακέτων δικτύου.

## Εγκατάσταση και Ρύθμιση

### Επιλογή 1: Γρήγορη Εγκατάσταση (Linux - Συνιστάται)

Για τους χρήστες Linux, παρέχουμε αυτοματοποιημένα σενάρια εγκατάστασης:

```bash
# 1. Κλωνοποιήστε το αποθετήριο
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Εκτελέστε το σενάριο εγκατάστασης
./install.sh

# 3. Εκτελέστε την εφαρμογή
./run.sh
```

Το σενάριο `install.sh` θα:
- Εγκαταστήσει εξαρτήσεις συστήματος (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Δημιουργήσει ένα εικονικό περιβάλλον Python
- Εγκαταστήσει όλα τα απαιτούμενα πακέτα Python (Flet, Scapy)

Το σενάριο `run.sh` θα ζητήσει αυτόματα προνόμια root και θα εκτελέσει την εφαρμογή.

### Επιλογή 2: Χειροκίνητη Εγκατάσταση

#### 1. Εγκαταστήστε Εξαρτήσεις Συστήματος

**Σε Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Σε Windows:**

Εγκαταστήστε το Python 3.8+ από το [python.org](https://www.python.org/downloads/)

#### 2. Εγκαταστήστε Εξαρτήσεις Python

**Σε Linux (χρησιμοποιώντας εικονικό περιβάλλον - συνιστάται):**

```bash
# Δημιουργήστε εικονικό περιβάλλον
python3 -m venv venv

# Ενεργοποιήστε το εικονικό περιβάλλον
source venv/bin/activate

# Εγκαταστήστε εξαρτήσεις
pip install flet scapy
```

**Σε Linux (εγκατάσταση σε όλο το σύστημα):**

```bash
pip3 install flet scapy --break-system-packages
```

**Σε Windows:**

```bash
pip install flet scapy
```

#### 3. Εκτέλεση της Εφαρμογής

Δεδομένου ότι η ανίχνευση δικτύου απαιτεί αυξημένα προνόμια, πρέπει να εκτελέσετε την εφαρμογή ως root ή διαχειριστής.

**Σε Linux (με εικονικό περιβάλλον):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**Σε Linux (εγκατάσταση σε όλο το σύστημα):**

```bash
sudo python3 albion_insight/main.py
```

**Σε Windows (Εκτελέστε τη Γραμμή Εντολών/PowerShell ως Διαχειριστής):**

```bash
python albion_insight/main.py
```

Η εφαρμογή θα ανοίξει σε ένα εγγενές παράθυρο επιφάνειας εργασίας.

## Πώς να Δημιουργήσετε ένα Εκτελέσιμο

Η εφαρμογή μπορεί να συσκευαστεί σε ένα αυτόνομο εκτελέσιμο χρησιμοποιώντας το **PyInstaller**. Αυτό επιτρέπει στους χρήστες να εκτελούν την εφαρμογή χωρίς να εγκαταστήσουν το Python ή τις εξαρτήσεις του.

Για λεπτομερείς οδηγίες σχετικά με τη δημιουργία εκτελέσιμων για Linux, Windows και macOS, ανατρέξτε στον οδηγό **[PACKAGING.md](PACKAGING.md)**.

### Γρήγορη Δημιουργία (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Το εκτελέσιμο θα βρίσκεται στο φάκελο `dist/`.

## Δομή Έργου

Ολόκληρη η εφαρμογή περιέχεται σε ένα μόνο αρχείο για απλότητα:

| Αρχείο | Περιγραφή |
| :--- | :--- |
| `albion_insight/main.py` | Το κύριο αρχείο εφαρμογής που περιέχει όλη τη λογική (Μοντέλα, Network Tracker, Flet UI). |
| `README.md` | Αυτό το αρχείο τεκμηρίωσης. |
| `README.el-GR.md` | Αυτό το αρχείο τεκμηρίωσης στα Ελληνικά. |
| `CONTRIBUTING.md` | Οδηγίες για τη συνεισφορά στο έργο. |
| `CODE_OF_CONDUCT.md` | Ο Κώδικας Δεοντολογίας του έργου. |
| `SECURITY.md` | Πολιτική για την αναφορά ευπαθειών ασφαλείας. |

## Τρέχουσα Κατάσταση (Δεδομένα σε Πραγματικό Χρόνο)

Η εφαρμογή περιλαμβάνει τώρα τη λογική **Αποκωδικοποίησης Πρωτοκόλλου Photon**, μεταφρασμένη από το αρχικό έργο C#. Αυτό επιτρέπει στην εφαρμογή να επεξεργάζεται συμβάντα σε πραγματικό χρόνο όπως `UpdateMoney`, `UpdateFame`, `KilledPlayer` και `Died` απευθείας από την κίνηση του δικτύου.

**Σημείωση:** Η πλήρης μετάφραση κάθε μεμονωμένου συμβάντος μάχης (όπως `CastHit`, `Attack`) είναι μια συνεχιζόμενη προσπάθεια. Η τρέχουσα υλοποίηση εστιάζει στα βασικά στατιστικά στοιχεία και τη δομή για τον Μετρητή Ζημιάς. Ο υπολογισμός DPS του Μετρητή Ζημιάς βασίζεται στα αποκωδικοποιημένα συμβάντα.

## Συνεισφορά

Χαιρετίζουμε τις συνεισφορές από την κοινότητα! Είτε είστε προγραμματιστής, σχεδιαστής, είτε απλά λάτρης του Albion Online, υπάρχουν πολλοί τρόποι για να βοηθήσετε στη βελτίωση του Albion Insight.

Διαβάστε τις [Οδηγίες Συνεισφοράς](CONTRIBUTING.md) για λεπτομερείς πληροφορίες σχετικά με τον τρόπο συνεισφοράς σε αυτό το έργο.

### Γρήγορη Εκκίνηση για Συνεισφέροντες:

1.  Κλωνοποιήστε το αποθετήριο: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Κλωνοποιήστε το fork σας: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Δημιουργήστε ένα νέο branch: `git checkout -b feature/your-feature-name`
4.  Κάντε τις αλλαγές σας και commit: `git commit -m "Add your feature"`
5.  Push στο fork σας: `git push origin feature/your-feature-name`
6.  Ανοίξτε ένα Pull Request στο κύριο αποθετήριο

## Άδεια

Αυτό το έργο διαθέτει άδεια MIT - δείτε το αρχείο [LICENSE](LICENSE) για λεπτομέρειες.

## Ευχαριστίες

- Αρχικό έργο: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) από τον Triky313
- Κατασκευασμένο με το πλαίσιο [Flet](https://flet.dev/)
- Ανάλυση δικτύου με την υποστήριξη του [Scapy](https://scapy.net/)

---
*Μια λύση πολλαπλών πλατφορμών για την κοινότητα του Albion Online.*
