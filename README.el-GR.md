# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

Το **Albion Insight** είναι ένα εργαλείο ανάλυσης στατιστικών πολλαπλών πλατφορμών (Linux, Windows, macOS) για το παιχνίδι Albion Online, επανα-υλοποιημένο σε **Python** χρησιμοποιώντας το framework **Flet**. Έχει σχεδιαστεί για να παρακολουθεί στατιστικά στοιχεία εντός του παιχνιδιού σε πραγματικό χρόνο, συμπεριλαμβανομένων των silver, fame και δεδομένων μάχης (Damage Meter), αναλύοντας την κίνηση του δικτύου.

Αυτό το έργο είναι μια σύγχρονη, ανοιχτού κώδικα εναλλακτική λύση στο αρχικό εργαλείο `AlbionOnline-StatisticsAnalysis` που βασιζόταν σε C#/WPF, εστιάζοντας στη συμβατότητα πολλαπλών πλατφορμών και την ευκολία χρήσης.

## Χαρακτηριστικά (Features)

*   **Συμβατότητα Πολλαπλών Πλατφορμών:** Λειτουργεί εγγενώς σε Linux, Windows και macOS.
*   **Παρακολούθηση σε Πραγματικό Χρόνο:** Χρησιμοποιεί τη βιβλιοθήκη `Scapy` για να "μυρίζει" πακέτα UDP στις θύρες του Albion Online (5055, 5056, 5058).
*   **Δομή Μετρητή Ζημιάς (Damage Meter):** Περιλαμβάνει τις απαραίτητες δομές δεδομένων και UI για την εμφάνιση ζωντανών στατιστικών μάχης (Ποσότητα Ζημιάς, Ποσότητα Θεραπείας, DPS).
*   **Σύγχρονο UI:** Κατασκευασμένο με το Flet, παρέχοντας μια γρήγορη, εγγενή εμφάνιση εφαρμογής επιφάνειας εργασίας.
*   **Διαχείριση Συνεδριών:** Επιτρέπει την έναρξη, διακοπή, επαναφορά και αποθήκευση στατιστικών συνεδρίας.

## Προαπαιτούμενα (Prerequisites)

*   Python 3.8+
*   Βιβλιοθήκες **Flet** και **Scapy**.
*   **Προνόμια Root/Διαχειριστή:** Απαραίτητα για τη λήψη πακέτων δικτύου.

## Εγκατάσταση και Ρύθμιση (Installation and Setup)

### Επιλογή 1: Γρήγορη Εγκατάσταση (Linux - Συνιστάται)

Για τους χρήστες Linux, παρέχουμε αυτοματοποιημένα σενάρια εγκατάστασης:

\`\`\`bash
# 1. Κλωνοποιήστε το αποθετήριο
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Εκτελέστε το σενάριο εγκατάστασης
./install.sh

# 3. Εκτελέστε την εφαρμογή
./run.sh
\`\`\`

Το σενάριο `install.sh` θα:
- Εγκαταστήσει τις εξαρτήσεις συστήματος (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Δημιουργήσει ένα εικονικό περιβάλλον Python
- Εγκαταστήσει όλα τα απαιτούμενα πακέτα Python (Flet, Scapy)

Το σενάριο `run.sh` θα ζητήσει αυτόματα προνόμια root και θα εκτελέσει την εφαρμογή.

### Επιλογή 2: Χειροκίνητη Εγκατάσταση (Windows/macOS/Linux)

1.  **Κλωνοποιήστε το αποθετήριο:**
    \`\`\`bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    \`\`\`

2.  **Δημιουργήστε και ενεργοποιήστε ένα εικονικό περιβάλλον:**
    \`\`\`bash
    python3 -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    \`\`\`

3.  **Εγκαταστήστε τις εξαρτήσεις:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

4.  **Εκτελέστε την εφαρμογή:**
    \`\`\`bash
    # Windows: Πρέπει να εκτελεστεί ως διαχειριστής
    flet run albion_insight/main.py
    # Linux/macOS: Απαιτούνται προνόμια root/sudo
    sudo flet run albion_insight/main.py
    \`\`\`

## Συνεισφορά (Contributing)

Οι συνεισφορές είναι ευπρόσδεκτες! Μη διστάσετε να αναφέρετε σφάλματα, να ζητήσετε λειτουργίες ή να βελτιώσετε τον κώδικα. Ανατρέξτε στο [CONTRIBUTING.md](CONTRIBUTING.md) για λεπτομέρειες.

## Άδεια (License)

Αυτό το έργο διατίθεται υπό την άδεια MIT. Ανατρέξτε στο αρχείο [LICENSE](LICENSE) για λεπτομέρειες.

## Ευχαριστίες (Acknowledgments)

*   Ευχαριστούμε τον **Triky313**, τον δημιουργό του αρχικού έργου C#/WPF `AlbionOnline-StatisticsAnalysis`.
*   Ευχαριστούμε την ομάδα του **Scapy** για την παροχή της λειτουργικότητας λήψης πακέτων δικτύου.
*   Ευχαριστούμε την ομάδα του **Flet** που κατέστησε δυνατή τη διεπαφή χρήστη πολλαπλών πλατφορμών.
