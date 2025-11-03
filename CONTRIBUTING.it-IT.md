# Contribuire ad Albion Insight

**[Read in English](CONTRIBUTING.md)**
**[Leia em Português](CONTRIBUTING.pt-BR.md)**
**[Leer en Español](CONTRIBUTING.es-ES.md)**
**[Lire en Français](CONTRIBUTING.fr-FR.md)**

Prima di tutto, grazie per aver considerato di contribuire ad Albion Insight! Sono persone come te che rendono Albion Insight uno strumento incredibile per la comunità di Albion Online.

## Indice

- [Codice di Condotta](#codice-di-condotta)
- [Come Posso Contribuire?](#come-posso-contribuire)
  - [Segnalazione di Bug](#segnalazione-di-bug)
  - [Suggerimento di Funzionalità](#suggerimento-di-funzionalità)
  - [Contributi di Codice](#contributi-di-codice)
  - [Documentazione](#documentazione)
- [Configurazione dell'Ambiente di Sviluppo](#configurazione-dellambiente-di-sviluppo)
- [Standard di Codice](#standard-di-codice)
- [Messaggi di Commit](#messaggi-di-commit)
- [Processo di Pull Request](#processo-di-pull-request)

## Codice di Condotta

Questo progetto e tutti coloro che vi partecipano sono regolati dal nostro Codice di Condotta. Partecipando, ci si aspetta che tu sostenga questo codice. Si prega di segnalare comportamenti inaccettabili ai manutentori del progetto.

## Come Posso Contribuire?

### Segnalazione di Bug

Prima di creare segnalazioni di bug, verifica le issue esistenti per evitare duplicati. Quando crei una segnalazione di bug, includi quanti più dettagli possibile utilizzando il template di segnalazione bug.

**Le buone segnalazioni di bug includono:**
- Un titolo chiaro e descrittivo
- Passaggi esatti per riprodurre il problema
- Comportamento atteso vs comportamento effettivo
- Screenshot se applicabile
- Dettagli del tuo ambiente (SO, versione Python, ecc.)
- Log o messaggi di errore pertinenti

### Suggerimento di Funzionalità

I suggerimenti di funzionalità sono benvenuti! Utilizza il template di richiesta di funzionalità e fornisci:
- Una descrizione chiara della funzionalità
- Il problema che risolve
- Possibili approcci di implementazione
- Alternative che hai considerato

### Contributi di Codice

Adoriamo i contributi di codice! Ecco come iniziare:

1. **Fai un fork del repository** e crea il tuo branch dalla `master`
2. **Configura il tuo ambiente di sviluppo** (vedi Configurazione dell'Ambiente sotto)
3. **Apporta le tue modifiche** seguendo i nostri standard di codice
4. **Testa le tue modifiche** completamente
5. **Aggiorna la documentazione** se necessario
6. **Invia una pull request** utilizzando il nostro template di PR

### Documentazione

I miglioramenti alla documentazione sono sempre apprezzati! Ciò include:
- File README
- Pagine Wiki
- Commenti nel codice
- Tutorial e guide
- Traduzioni in altre lingue

## Configurazione dell'Ambiente di Sviluppo

### Prerequisiti

- Python 3.8 o superiore
- Git
- Privilegi di Root/Amministratore (per la cattura dei pacchetti)

### Configurazione del Tuo Ambiente

```bash
# Clona il tuo fork
git clone https://github.com/TUO_UTENTE/AlbionInsight.git
cd AlbionInsight

# Crea un ambiente virtuale
python3 -m venv venv

# Attiva l'ambiente virtuale
# Su Linux/macOS:
source venv/bin/activate
# Su Windows:
venv\Scripts\activate

# Installa le dipendenze
pip install -r requirements.txt

# Installa le dipendenze di sviluppo
pip install pylint flake8 black pytest
```

### Esecuzione dell'Applicazione

```bash
# Su Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# Su Windows (come Amministratore):
python albion_insight.py
```

## Standard di Codice

Seguiamo le linee guida di stile PEP 8 per il codice Python. Assicurati che il tuo codice aderisca a questi standard:

- Usa 4 spazi per l'indentazione (niente tabulazioni)
- Lunghezza massima della riga di 100 caratteri
- Usa nomi significativi per variabili e funzioni
- Aggiungi docstring a tutte le funzioni e classi
- Includi type hints quando appropriato
- Mantieni le funzioni focalizzate e concise

**Strumenti per aiutare:**
```bash
# Formatta il tuo codice con black
black albion_insight.py

# Controlla i problemi di stile
flake8 albion_insight.py

# Esegui il linter
pylint albion_insight.py
```

## Messaggi di Commit

Scrivi messaggi di commit chiari e significativi:

- Usa il tempo presente ("Aggiunge funzionalità" non "Ha aggiunto funzionalità")
- Usa il modo imperativo ("Sposta il cursore su..." non "Sposta il cursore su...")
- Limita la prima riga a 72 caratteri
- Fai riferimento a issue e pull request quando pertinente

**Esempi:**
```
Aggiunge funzionalità di esportazione del damage meter

Corregge il parsing dei pacchetti di rete per le connessioni IPv6

Aggiorna README con istruzioni di installazione per macOS

Closes #123
```

## Processo di Pull Request

1. **Aggiorna la documentazione** per eventuali modifiche alla funzionalità
2. **Aggiungi test** per nuove funzionalità o correzioni di bug
3. **Assicurati che tutti i test passino** prima di inviare
4. **Aggiorna il README.md** se necessario
5. **Compila completamente il template di PR**
6. **Collega le issue correlate** nella descrizione del tuo PR
7. **Richiedi la revisione** ai manutentori
8. **Rispondi al feedback** prontamente e professionalmente

### Checklist PR

Prima di inviare il tuo PR, assicurati che:
- [ ] Il codice segua le linee guida di stile del progetto
- [ ] Auto-revisione completata
- [ ] Commenti aggiunti alle sezioni di codice complesse
- [ ] Documentazione aggiornata
- [ ] Nessun nuovo avviso generato
- [ ] Test aggiunti e superati
- [ ] Le modifiche dipendenti sono state unite

## Domande?

Non esitare a fare domande! Puoi:
- Aprire una issue con l'etichetta "question"
- Partecipare alle discussioni della comunità
- Contattare i manutentori

Grazie per aver contribuito ad Albion Insight! I tuoi sforzi aiutano a rendere questo strumento migliore per l'intera comunità di Albion Online.
