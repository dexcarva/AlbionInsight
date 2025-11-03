# Albion Insight

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Plateforme](https://img.shields.io/badge/plateforme-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Bienvenues](https://img.shields.io/badge/contributions-bienvenues-brightgreen.svg)](CONTRIBUTING.fr-FR.md)

**[Read this in English (Lire en Anglais)](README.md)**
**[Leia em Português (Lire en Portugais)](README.pt-BR.md)**
**[Leer en Español (Lire en Espagnol)](README.es-ES.md)**

**Albion Insight** est un outil d'analyse statistique multiplateforme (Linux, Windows, macOS) pour le jeu Albion Online, réimplémenté en **Python** en utilisant le framework **Flet**. Il est conçu pour suivre les statistiques du jeu en temps réel, y compris l'argent, la renommée et les données de combat (Compteur de Dégâts), en analysant le trafic réseau.

Ce projet est une alternative moderne et open-source à l'outil original `AlbionOnline-StatisticsAnalysis` basé sur C#/WPF, se concentrant sur la compatibilité multiplateforme et la facilité d'utilisation.

## Fonctionnalités

*   **Compatibilité Multiplateforme:** Fonctionne nativement sur Linux, Windows et macOS.
*   **Suivi en Temps Réel:** Utilise la bibliothèque `Scapy` pour capturer les paquets UDP sur les ports d'Albion Online (5055, 5056, 5058).
*   **Structure du Compteur de Dégâts:** Inclut les structures de données et l'interface nécessaires pour afficher les statistiques de combat en direct (Dégâts Infligés, Soins Réalisés, DPS).
*   **Interface Moderne:** Construit avec Flet, offrant une application de bureau rapide et d'apparence native.
*   **Gestion de Session:** Permet de démarrer, arrêter, réinitialiser et sauvegarder les statistiques de session.

## Prérequis

*   Python 3.8+
*   Bibliothèques **Flet** et **Scapy**.
*   **Privilèges Root/Administrateur:** Nécessaires pour la capture de paquets réseau.

## Installation et Configuration

### Option 1: Installation Rapide (Linux - Recommandé)

Pour les utilisateurs Linux, nous fournissons des scripts d'installation automatisés:

```bash
# 1. Cloner le dépôt
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Exécuter le script d'installation
./install.sh

# 3. Exécuter l'application
./run.sh
```

Le script `install.sh` va:
- Installer les dépendances système (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Créer un environnement virtuel Python
- Installer tous les paquets Python requis (Flet, Scapy)

Le script `run.sh` demandera automatiquement les privilèges root et exécutera l'application.

### Option 2: Installation Manuelle

#### 1. Installer les Dépendances Système

**Sur Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Sur Windows:**

Installer Python 3.8+ depuis [python.org](https://www.python.org/downloads/)

#### 2. Installer les Dépendances Python

**Sur Linux (en utilisant un environnement virtuel - recommandé):**

```bash
# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
pip install flet scapy
```

**Sur Linux (installation à l'échelle du système):**

```bash
pip3 install flet scapy --break-system-packages
```

**Sur Windows:**

```bash
pip install flet scapy
```

#### 3. Exécuter l'Application

Étant donné que la capture réseau nécessite des privilèges élevés, vous devez exécuter l'application en tant que root ou administrateur.

**Sur Linux (avec environnement virtuel):**

```bash
sudo venv/bin/python3 albion_insight.py
```

**Sur Linux (installation à l'échelle du système):**

```bash
sudo python3 albion_insight.py
```

**Sur Windows (Exécuter l'Invite de Commandes/PowerShell en tant qu'Administrateur):**

```bash
python albion_insight.py
```

L'application s'ouvrira dans une fenêtre de bureau native.

## Comment Créer un Exécutable

L'application peut être empaquetée dans un exécutable autonome en utilisant **PyInstaller**. Cela permet aux utilisateurs d'exécuter l'application sans installer Python ou ses dépendances.

Pour des instructions détaillées sur la création d'exécutables pour Linux, Windows et macOS, consultez le guide **[PACKAGING.md](PACKAGING.md)** (en anglais).

### Build Rapide (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight.py
```

L'exécutable sera situé dans le dossier `dist/`.

## Structure du Projet

L'application entière est contenue dans un seul fichier pour la simplicité:

| Fichier | Description |
| :--- | :--- |
| `albion_insight.py` | Le fichier principal de l'application contenant toute la logique (Modèles, Traqueur Réseau, Interface Flet). |
| `README.md` | Ce fichier de documentation (en anglais). |
| `README.pt-BR.md` | Ce fichier de documentation (en portugais). |
| `README.es-ES.md` | Ce fichier de documentation (en espagnol). |
| `README.fr-FR.md` | Ce fichier de documentation (en français). |

## Statut Actuel (Données en Temps Réel)

L'application inclut maintenant la logique de **Décodage du Protocole Photon**, traduite du projet C# original. Cela permet à l'application de traiter les événements en temps réel comme `UpdateMoney`, `UpdateFame`, `KilledPlayer` et `Died` directement à partir du trafic réseau.

**Note:** La traduction complète de chaque événement de combat (comme `CastHit`, `Attack`) est un effort continu. L'implémentation actuelle se concentre sur les statistiques de base et la structure du Compteur de Dégâts. Le calcul de DPS du Compteur de Dégâts est basé sur les événements décodés.

## Contribuer

Nous accueillons les contributions de la communauté! Que vous soyez développeur, designer ou simplement un passionné d'Albion Online, il existe de nombreuses façons d'aider à améliorer Albion Insight.

Veuillez lire nos [Directives de Contribution](CONTRIBUTING.fr-FR.md) pour des informations détaillées sur la façon de contribuer à ce projet.

### Démarrage Rapide pour les Contributeurs:

1.  Forker le dépôt: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Cloner votre fork: `git clone https://github.com/VOTRE_NOM_UTILISATEUR/AlbionInsight.git`
3.  Créer une nouvelle branche: `git checkout -b feature/nom-de-votre-fonctionnalite`
4.  Faire vos changements et commiter: `git commit -m "Ajout de votre fonctionnalité"`
5.  Pousser vers votre fork: `git push origin feature/nom-de-votre-fonctionnalite`
6.  Ouvrir une Pull Request sur le dépôt principal

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

- Projet original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) par Triky313
- Construit avec le framework [Flet](https://flet.dev/)
- Analyse réseau propulsée par [Scapy](https://scapy.net/)

---
*Une solution multiplateforme pour la communauté d'Albion Online.*
