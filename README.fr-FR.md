# Albion Insight

**Albion Insight** est un outil d'analyse statistique multiplateforme (Linux, Windows, macOS) pour le jeu Albion Online, réimplémenté en **Python** à l'aide du framework **Flet**. Il est conçu pour suivre les statistiques en temps réel dans le jeu, y compris l'argent, la renommée et les données de combat (Damage Meter), en analysant le trafic réseau.

Ce projet est une alternative moderne et open source à l'outil original  basé sur C#/WPF, se concentrant sur la compatibilité multiplateforme et la facilité d'utilisation.

## Fonctionnalités

*   **Compatibilité Multiplateforme:** Fonctionne nativement sur Linux, Windows et macOS.
*   **Suivi en Temps Réel:** Utilise la bibliothèque  pour sniffer les paquets UDP sur les ports d'Albion Online (5055, 5056, 5058).
*   **Structure du Compteur de Dégâts:** Inclut les structures de données et l'interface utilisateur nécessaires pour afficher les statistiques de combat en direct (Dégâts Infligés, Soins Effectués, DPS).
*   **Interface Utilisateur Moderne:** Construit avec Flet, offrant une application de bureau rapide et d'apparence native.
*   **Gestion de Session:** Permet de démarrer, arrêter, réinitialiser et enregistrer les statistiques de session.

## Prérequis

*   Python 3.8+
*   Bibliothèques **Flet** et **Scapy**.
*   **Privilèges Root/Administrateur:** Nécessaires pour la capture de paquets réseau.

## Installation et Configuration

### Option 1: Installation Rapide (Linux - Recommandé)

Pour les utilisateurs Linux, nous fournissons des scripts d'installation automatisés :

```shell
# 1. Cloner le dépôt
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Exécuter le script d'installation
./install.sh

# 3. Exécuter l'application
./run.sh
```

Le script `install.sh` va :

*   Installer les dépendances système (`libpcap-dev`, `python3-pip`, `python3-venv`)
*   Créer un environnement virtuel Python
*   Installer tous les paquets Python requis (Flet, Scapy)

Le script `run.sh` demandera automatiquement les privilèges root et exécutera l'application.

### Option 2: Installation Manuelle

#### 1. Installer les Dépendances Système

**Sur Linux (Debian/Ubuntu):**

```shell
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Sur Windows:**

Installer Python 3.8+ depuis [python.org]()

#### 2. Installer les Dépendances Python

**Sur Linux (en utilisant un environnement virtuel - recommandé):**

```shell
# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
pip install flet scapy
```

**Sur Linux (installation à l'échelle du système):**

```shell
pip3 install flet scapy --break-system-packages
```

**Sur Windows:**

```shell
pip install flet scapy
```

#### 3. Exécuter l'Application

Étant donné que le sniffing réseau nécessite des privilèges élevés, vous devez exécuter l'application en tant que root ou administrateur.

**Sur Linux (avec environnement virtuel):**

```shell
sudo venv/bin/python3 albion_insight/main.py
```

**Sur Linux (installation à l'échelle du système):**

```shell
sudo python3 albion_insight/main.py
```

**Sur Windows (Exécuter l'Invite de Commandes/PowerShell en tant qu'Administrateur):**

```shell
python albion_insight/main.py
```

L'application s'ouvrira dans une fenêtre de bureau native.

## Comment Construire un Exécutable

L'application peut être empaquetée dans un exécutable autonome à l'aide de **PyInstaller**. Cela permet aux utilisateurs d'exécuter l'application sans installer Python ou ses dépendances.

Pour des instructions détaillées sur la construction d'exécutables pour Linux, Windows et macOS, consultez le guide **[PACKAGING.md]()**.

### Construction Rapide (Linux)

```shell
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

L'exécutable se trouvera dans le dossier `dist/`.

## Structure du Projet

L'application entière est contenue dans un seul fichier pour la simplicité :

| Fichier | Description |
| :-- | :-- |
| `albion_insight/main.py` | Le fichier d'application principal contenant toute la logique (Modèles, Suivi Réseau, Interface Utilisateur Flet). |
| `README.md` | Le fichier de documentation principal en anglais. |
| `README.pt-BR.md` | Ce fichier de documentation en portugais brésilien. |
| `README.fr-FR.md` | Ce fichier de documentation en français. |
| `CONTRIBUTING.md` | Lignes directrices pour contribuer au projet. |
| `CODE_OF_CONDUCT.md` | Le Code de Conduite du projet. |
| `SECURITY.md` | Politique de signalement des vulnérabilités de sécurité. |

## Statut Actuel (Données en Temps Réel)

L'application inclut désormais la logique de **Décodage du Protocole Photon**, traduite du projet C# original. Cela permet à l'application de traiter les événements en temps réel comme `UpdateMoney`, `UpdateFame`, `KilledPlayer` et `Died` directement à partir du trafic réseau.

**Note:** La traduction complète de chaque événement de combat (comme `CastHit`, `Attack`) est un effort continu. L'implémentation actuelle se concentre sur les statistiques de base et la structure pour le Compteur de Dégâts. Le calcul du DPS du Compteur de Dégâts est basé sur les événements décodés.

## Contribuer

Nous accueillons les contributions de la communauté ! Que vous soyez développeur, designer ou simplement un passionné d'Albion Online, il existe de nombreuses façons d'aider à améliorer Albion Insight.

Veuillez lire nos [Lignes Directrices de Contribution]() pour des informations détaillées sur la façon de contribuer à ce projet.

### Démarrage Rapide pour les Contributeurs:

1.  Forker le dépôt: [github.com/dexcarva/AlbionInsight]()
2.  Cloner votre fork: `git clone https://github.com/VOTRE_NOM_UTILISATEUR/AlbionInsight.git`
3.  Créer une nouvelle branche: `git checkout -b feature/votre-nom-de-fonctionnalite`
4.  Faire vos changements et commiter: `git commit -m "Ajouter votre fonctionnalité"`
5.  Pousser vers votre fork: `git push origin feature/votre-nom-de-fonctionnalite`
6.  Ouvrir une Pull Request sur le dépôt principal

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE]() pour plus de détails.

## Remerciements

*   Projet original: [AlbionOnline-StatisticsAnalysis]() par Triky313
*   Construit avec le framework [Flet]()
*   Analyse réseau alimentée par [Scapy]()

_Une solution multiplateforme pour la communauté Albion Online._

## À Propos

Albion Insight est un outil d'analyse statistique multiplateforme (Linux, Windows, macOS) pour le jeu Albion Online, réimplémenté en Python à l'aide du framework Flet. Il est conçu pour suivre les statistiques en temps réel dans le jeu, y compris l'argent, la renommée et les données de combat (Damage Meter), en analysant le trafic réseau.
