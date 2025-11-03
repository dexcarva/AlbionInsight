# Contribuer à Albion Insight

**[Read this in English](CONTRIBUTING.md)**
**[Leer en Español](CONTRIBUTING.es-ES.md)**

Tout d'abord, merci d'envisager de contribuer à Albion Insight ! Ce sont des personnes comme vous qui font d'Albion Insight un outil si précieux pour la communauté d'Albion Online.

## Table des Matières

- [Code de Conduite](#code-de-conduite)
- [Comment Puis-je Contribuer ?](#comment-puis-je-contribuer)
  - [Signaler des Bugs](#signaler-des-bugs)
  - [Suggérer des Fonctionnalités](#suggérer-des-fonctionnalités)
  - [Contributions de Code](#contributions-de-code)
  - [Documentation](#documentation)
- [Configuration de l'Environnement de Développement](#configuration-de-lenvironnement-de-développement)
- [Normes de Codage](#normes-de-codage)
- [Messages de Commit](#messages-de-commit)
- [Processus de Demande de Tirage (Pull Request)](#processus-de-demande-de-tirage-pull-request)

## Code de Conduite

Ce projet et tous ceux qui y participent sont régis par notre Code de Conduite. En participant, vous êtes censé respecter ce code. Veuillez signaler tout comportement inacceptable aux mainteneurs du projet.

## Comment Puis-je Contribuer ?

### Signaler des Bugs

Avant de créer des rapports de bugs, veuillez vérifier les problèmes existants pour éviter les doublons. Lorsque vous créez un rapport de bug, incluez autant de détails que possible en utilisant le modèle de rapport de bug.

**Les bons rapports de bugs incluent :**
- Un titre clair et descriptif
- Les étapes exactes pour reproduire le problème
- Le comportement attendu par rapport au comportement réel
- Des captures d'écran si applicable
- Les détails de votre environnement (OS, version Python, etc.)
- Les journaux ou messages d'erreur pertinents

### Suggérer des Fonctionnalités

Les suggestions de fonctionnalités sont les bienvenues ! Veuillez utiliser le modèle de demande de fonctionnalité et fournir :
- Une description claire de la fonctionnalité
- Le problème qu'elle résout
- Les approches d'implémentation possibles
- Toute alternative que vous avez envisagée

### Contributions de Code

Nous aimons les contributions de code ! Voici comment commencer :

1. **Forkez le dépôt** et créez votre branche à partir de `master`
2. **Configurez votre environnement de développement** (voir Configuration de l'Environnement de Développement ci-dessous)
3. **Faites vos changements** en suivant nos normes de codage
4. **Testez vos changements** de manière approfondie
5. **Mettez à jour la documentation** si nécessaire
6. **Soumettez une demande de tirage (Pull Request)** en utilisant notre modèle de PR

### Documentation

Les améliorations à la documentation sont toujours appréciées ! Cela inclut :
- Les fichiers README
- Les pages Wiki
- Les commentaires de code
- Les tutoriels et guides
- Les traductions vers d'autres langues

## Configuration de l'Environnement de Développement

### Prérequis

- Python 3.8 ou supérieur
- Git
- Privilèges Root/Administrateur (pour la capture de paquets)

### Configuration de Votre Environnement

```bash
# Cloner votre fork
git clone https://github.com/VOTRE_NOM_UTILISATEUR/AlbionInsight.git
cd AlbionInsight

# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
# Sur Linux/macOS:
source venv/bin/activate
# Sur Windows:
venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Installer les dépendances de développement
pip install pylint flake8 black pytest
```

### Exécuter l'Application

```bash
# Sur Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# Sur Windows (en tant qu'Administrateur):
python albion_insight.py
```

## Normes de Codage

Nous suivons les directives de style PEP 8 pour le code Python. Veuillez vous assurer que votre code adhère à ces normes :

- Utilisez 4 espaces pour l'indentation (pas de tabulations)
- Longueur maximale de ligne de 100 caractères
- Utilisez des noms de variables et de fonctions significatifs
- Ajoutez des docstrings à toutes les fonctions et classes
- Incluez des indications de type (type hints) lorsque cela est approprié
- Gardez les fonctions ciblées et concises

**Outils pour vous aider :**
```bash
# Formater votre code avec black
black albion_insight.py

# Vérifier les problèmes de style
flake8 albion_insight.py

# Exécuter le linter
pylint albion_insight.py
```

## Messages de Commit

Rédigez des messages de commit clairs et significatifs :

- Utilisez le présent de l'indicatif ("Ajouter fonctionnalité" et non "Ajouté fonctionnalité")
- Utilisez le mode impératif ("Déplacer le curseur vers..." et non "Déplace le curseur vers...")
- Limitez la première ligne à 72 caractères
- Référencez les issues et les pull requests lorsque cela est pertinent

**Exemples :**
```
Ajouter la fonctionnalité d'exportation du compteur de dégâts

Corriger l'analyse des paquets réseau pour les connexions IPv6

Mettre à jour le README avec les instructions d'installation macOS

Clôture #123
```

## Processus de Demande de Tirage (Pull Request)

1. **Mettez à jour la documentation** pour tout changement de fonctionnalité
2. **Ajoutez des tests** pour les nouvelles fonctionnalités ou les corrections de bugs
3. **Assurez-vous que tous les tests passent** avant de soumettre
4. **Mettez à jour le README.md** si nécessaire
5. **Remplissez complètement le modèle de PR**
6. **Liez les issues connexes** dans la description de votre PR
7. **Demandez une révision** aux mainteneurs
8. **Traitez les commentaires** rapidement et professionnellement

### Liste de Contrôle de la PR

Avant de soumettre votre PR, assurez-vous que :
- [ ] Le code suit les directives de style du projet
- [ ] L'auto-révision est terminée
- [ ] Des commentaires sont ajoutés aux sections de code complexes
- [ ] La documentation est mise à jour
- [ ] Aucun nouvel avertissement n'est généré
- [ ] Les tests sont ajoutés et passent
- [ ] Les changements dépendants sont fusionnés

## Des Questions ?

N'hésitez pas à poser des questions ! Vous pouvez :
- Ouvrir une issue avec l'étiquette "question"
- Rejoindre nos discussions communautaires
- Contacter les mainteneurs

Merci de contribuer à Albion Insight ! Vos efforts aident à rendre cet outil meilleur pour toute la communauté d'Albion Online.
