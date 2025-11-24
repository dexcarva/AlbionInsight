 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Lire en Anglais (Read this in English)](README.md)**
**[Lire en Portugais (Leia em Português)](README.pt-BR.md)**
**[Lire en Espagnol (Leer en Español)](README.es-ES.md)**
**[Lire en Allemand (Lesen Sie dies auf Deutsch)](README.de-DE.md)**
**[Lire en Italien (Leggi in Italiano)](README.it-IT.md)**

# Albion Insight (FR)

**Albion Insight** est un outil d'analyse de statistiques multiplateforme (Linux, Windows, macOS) pour le jeu Albion Online, réimplémenté en **Python** avec le framework **Flet**. Il est conçu pour suivre en temps réel les statistiques du jeu, y compris l'argent, la renommée et les données de combat (Compteur de Dégâts), en analysant le trafic réseau.

Ce projet est une alternative moderne et open-source à l'outil original `AlbionOnline-StatisticsAnalysis` basé sur C#/WPF, axé sur la compatibilité multiplateforme et la facilité d'utilisation.

## Fonctionnalités

*   **Compatibilité Multiplateforme :** Fonctionne nativement sur Linux, Windows et macOS.
*   **Suivi en Temps Réel :** Utilise la bibliothèque `Scapy` pour renifler les paquets UDP sur les ports d'Albion Online (5055, 5056, 5058).
*   **Structure du Compteur de Dégâts :** Inclut les structures de données et l'interface utilisateur nécessaires pour afficher les statistiques de combat en direct (Dégâts Infligés, Soins Effectués, DPS).
*   **Interface Utilisateur Moderne :** Construit avec Flet, offrant une application de bureau rapide et d'apparence native.
*   **Gestion de Session :** Permet de démarrer, arrêter, réinitialiser et sauvegarder les statistiques de session.

## Prérequis

*   Python 3.8+
*   Bibliothèques **Flet** et **Scapy**.
*   **Privilèges Root/Administrateur :** Nécessaires pour la capture de paquets réseau.

## Installation et Configuration

### Option 1 : Installation Rapide (Linux - Recommandé)

Pour les utilisateurs de Linux, nous fournissons des scripts d'installation automatisés :

```bash
# 1. Cloner le dépôt
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Exécuter le script d'installation
./install.sh

# 3. Exécuter l'application
./run.sh
```

Le script `install.sh` va :
- Installer les dépendances système (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Créer un environnement virtuel Python
- Installer tous les paquets Python requis (Flet, Scapy)

Le script `run.sh` demandera automatiquement les privilèges root et exécutera l'application.

### Option 2 : Installation Manuelle

#### 1. Installer les Dépendances Système

**Sur Linux (Debian/Ubuntu) :**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Sur Windows :**

Installez Python 3.8+ depuis [python.org](https://www.python.org/downloads/)

#### 2. Installer les Dépendances Python

**Sur Linux (en utilisant un environnement virtuel - recommandé) :**

```bash
# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
pip install flet scapy
```

**Sur Linux (installation à l'échelle du système) :**

```bash
pip3 install flet scapy --break-system-packages
```

**Sur Windows :**

```bash
pip install flet scapy
```

#### 3. Exécuter l'Application

Étant donné que le reniflage de réseau nécessite des privilèges élevés, vous devez exécuter l'application en tant que root ou administrateur.

**Sur Linux (avec environnement virtuel) :**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**Sur Linux (installation à l'échelle du système) :**

```bash
sudo python3 albion_insight/main.py
```

**Sur Windows (Exécuter l'Invite de Commandes/PowerShell en tant qu'Administrateur) :**

```bash
python albion_insight/main.py
```

L'application s'ouvrira dans une fenêtre de bureau native.

## Comment Créer un Exécutable

L'application peut être empaquetée dans un exécutable autonome à l'aide de **PyInstaller**. Cela permet aux utilisateurs d'exécuter l'application sans installer Python ou ses dépendances.

Pour des instructions détaillées sur la création d'exécutables pour Linux, Windows et macOS, consultez le guide **[PACKAGING.md](PACKAGING.md)**.

### Création Rapide (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

L'exécutable sera situé dans le dossier `dist/`.

## Structure du Projet

L'application est structurée en composants modulaires pour une meilleure maintenabilité et évolutivité :

| Fichier | Description |
| :--- | :--- |
| `albion_insight/core/` | Logique de base, suivi réseau, modèles de données et décodage de protocole. |
| `albion_insight/ui/` | Composants de l'interface utilisateur construits avec Flet. |
| `albion_insight/utils/` | Fonctions utilitaires, configuration et journalisation. |
| `albion_insight/__main__.py` | Point d'entrée de l'application. |
| `README.md` | Ce fichier de documentation. |

## État Actuel (Données en Temps Réel)

L'application inclut désormais la logique de **Décodage du Protocole Photon**, traduite du projet C# original. Cela permet à l'application de traiter des événements en temps réel comme `UpdateMoney`, `UpdateFame`, `KilledPlayer` et `Died` directement à partir du trafic réseau.

**Note :** La traduction complète de chaque événement de combat (comme `CastHit`, `Attack`) est un effort continu. L'implémentation actuelle se concentre sur les statistiques de base et la structure du Compteur de Dégâts. Le calcul du DPS du Compteur de Dégâts est basé sur les événements décodés.

## Contribuer

Nous accueillons les contributions de la communauté ! Que vous soyez développeur, designer ou simplement un passionné d'Albion Online, il existe de nombreuses façons d'aider à améliorer Albion Insight.

Veuillez lire nos [Directives de Contribution](CONTRIBUTING.md) pour des informations détaillées sur la manière de contribuer à ce projet.

### Démarrage Rapide pour les Contributeurs :

1.  Forkez le dépôt : [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clonez votre fork : `git clone https://github.com/VOTRE_NOM_UTILISATEUR/AlbionInsight.git`
3.  Créez une nouvelle branche : `git checkout -b feature/votre-nom-de-fonctionnalite`
4.  Faites vos modifications et commitez : `git commit -m "Ajouter votre fonctionnalité"`
5.  Poussez vers votre fork : `git push origin feature/votre-nom-de-fonctionnalite`
6.  Ouvrez une Pull Request sur le dépôt principal

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

- Projet original : [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) par Triky313
- Construit avec le framework [Flet](https://flet.dev/)
- Analyse réseau optimisée par [Scapy](https://scapy.net/)

---
*Une solution multiplateforme pour la communauté d'Albion Online.*
