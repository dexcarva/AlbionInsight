# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** è uno strumento di analisi statistica multipiattaforma (Linux, Windows, macOS) per il gioco Albion Online, re-implementato in **Python** utilizzando il framework **Flet**. È progettato per tracciare statistiche di gioco in tempo reale, inclusi argento, fama e dati di combattimento (Damage Meter), analizzando il traffico di rete.

Questo progetto è un'alternativa moderna e open-source allo strumento originale `AlbionOnline-StatisticsAnalysis` basato su C#/WPF, focalizzato sulla compatibilità multipiattaforma e sulla facilità d'uso.

## Caratteristiche

*   **Compatibilità Multipiattaforma:** Funziona nativamente su Linux, Windows e macOS.
*   **Tracciamento in Tempo Reale:** Utilizza la libreria `Scapy` per sniffare i pacchetti UDP sulle porte di Albion Online (5055, 5056, 5058).
*   **Struttura del Damage Meter:** Include le strutture dati e l'interfaccia utente necessarie per visualizzare le statistiche di combattimento in tempo reale (Danno Inflitto, Guarigione Effettuata, DPS).
*   **Interfaccia Utente Moderna:** Costruita con Flet, fornisce un'applicazione desktop veloce e dall'aspetto nativo.
*   **Gestione Sessione:** Consente di avviare, interrompere, reimpostare e salvare le statistiche della sessione.

## Prerequisiti

*   Python 3.8+
*   Librerie **Flet** e **Scapy**.
*   **Privilegi di Root/Amministratore:** Necessari per la cattura dei pacchetti di rete.

## Installazione e Configurazione

### Opzione 1: Installazione Rapida (Linux - Consigliata)

Per gli utenti Linux, forniamo script di installazione automatizzati:

\`\`\`bash
# 1. Clona il repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Esegui lo script di installazione
./install.sh

# 3. Esegui l'applicazione
./run.sh
\`\`\`

Lo script `install.sh` provvederà a:
- Installare le dipendenze di sistema (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Creare un ambiente virtuale Python
- Installare tutte le librerie Python richieste (Flet, Scapy)

Lo script `run.sh` richiederà automaticamente i privilegi di root ed eseguirà l'applicazione.

### Opzione 2: Installazione Manuale

#### 1. Installa le Dipendenze di Sistema

**Su Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Su Windows:**

Installa Python 3.8+ da [python.org](https://www.python.org/downloads/)

#### 2. Installa le Dipendenze Python

**Su Linux (utilizzando l'ambiente virtuale - consigliato):**

\`\`\`bash
# Crea l'ambiente virtuale
python3 -m venv venv

# Attiva l'ambiente virtuale
source venv/bin/activate

# Installa le dipendenze
pip install flet scapy
\`\`\`

**Su Linux (installazione a livello di sistema):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Su Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Esecuzione dell'Applicazione

Poiché lo sniffing di rete richiede privilegi elevati, è necessario eseguire l'applicazione come root o amministratore.

**Su Linux (con ambiente virtuale):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Su Linux (installazione a livello di sistema):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Su Windows (Esegui Prompt dei Comandi/PowerShell come Amministratore):**

\`\`\`bash
python -m albion_insight
\`\`\`

L'applicazione si aprirà in una finestra desktop nativa.

## Come Creare un Eseguibile

L'applicazione può essere impacchettata in un eseguibile autonomo utilizzando **PyInstaller**. Ciò consente agli utenti di eseguire l'applicazione senza installare Python o le sue dipendenze.

Per istruzioni dettagliate sulla creazione di eseguibili per Linux, Windows e macOS, consulta la guida **[PACKAGING.md](PACKAGING.md)**.

### Creazione Rapida (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

L'eseguibile si troverà nella cartella `dist/`.

## Struttura del Progetto

L'applicazione è strutturata in componenti modulari per una migliore manutenibilità e scalabilità:

| File | Descrizione |
| :--- | :--- |
| `albion_insight/core/` | Logica centrale, tracciamento di rete, modelli di dati e decodifica del protocollo. |
| `albion_insight/ui/` | Componenti dell'interfaccia utente costruiti con Flet. |
| `albion_insight/utils/` | Funzioni di utilità, configurazione e logging. |
| `albion_insight/__main__.py` | Punto di ingresso per l'applicazione. |
| `README.md` | Questo file di documentazione. |
| `CONTRIBUTING.md` | Linee guida per contribuire al progetto. |
| `CODE_OF_CONDUCT.md` | Il Codice di Condotta del progetto. |
| `SECURITY.md` | Politica per la segnalazione di vulnerabilità di sicurezza. |

## Stato Attuale (Dati in Tempo Reale)

L'applicazione ora include la logica di **Decodifica del Protocollo Photon**, tradotta dal progetto C# originale. Ciò consente all'applicazione di elaborare eventi in tempo reale come `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` direttamente dal traffico di rete.

**Nota:** La traduzione completa di ogni singolo evento di combattimento (come `CastHit`, `Attack`) è uno sforzo in corso. L'implementazione attuale si concentra sulle statistiche di base e sulla struttura per il Damage Meter. Il calcolo del DPS del Damage Meter si basa sugli eventi decodificati.

## Contribuire

Accogliamo con favore i contributi della comunità! Che tu sia uno sviluppatore, un designer o semplicemente un appassionato di Albion Online, ci sono molti modi per aiutare a migliorare Albion Insight.

Si prega di leggere le nostre [Linee Guida per Contribuire](CONTRIBUTING.md) per informazioni dettagliate su come contribuire a questo progetto.

### Avvio Rapido per i Contributori:

1.  Fork del repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clona il tuo fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Crea un nuovo branch: `git checkout -b feature/your-feature-name`
4.  Apporta le tue modifiche e fai il commit: `git commit -m "Aggiungi la tua funzionalità"`
5.  Fai il push al tuo fork: `git push origin feature/your-feature-name`
6.  Apri una Pull Request sul repository principale

## Licenza

Questo progetto è concesso in licenza con la Licenza MIT - consulta il file [LICENSE](LICENSE) per i dettagli.

## Riconoscimenti

- Progetto originale: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) di Triky313
- Costruito con il framework [Flet](https://flet.dev/)
- Analisi di rete alimentata da [Scapy](https://scapy.net/)

---
*Una soluzione multipiattaforma per la comunità di Albion Online.*
