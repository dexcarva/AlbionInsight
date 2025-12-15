# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** — це крос-платформний (Linux, Windows, macOS) інструмент аналізу статистики для гри Albion Online, переписаний на **Python** з використанням фреймворку **Flet**. Він призначений для відстеження статистики в грі в реальному часі, включаючи срібло, славу та бойові дані (лічильник шкоди), шляхом аналізу мережевого трафіку.

Цей проєкт є сучасною, відкритою альтернативою оригінальному інструменту `AlbionOnline-StatisticsAnalysis` на базі C#/WPF, з акцентом на багатоплатформну сумісність та простоту використання.

## Можливості

*   **Крос-платформна сумісність:** Працює нативно на Linux, Windows та macOS.
*   **Відстеження в реальному часі:** Використовує бібліотеку `Scapy` для перехоплення UDP-пакетів на портах Albion Online (5055, 5056, 5058).
*   **Структура лічильника шкоди:** Включає необхідні структури даних та інтерфейс для відображення бойової статистики в реальному часі (завдана шкода, вилікована шкода, DPS).
*   **Сучасний інтерфейс:** Створений за допомогою Flet, забезпечуючи швидкий, нативний вигляд настільної програми.
*   **Керування сесіями:** Дозволяє запускати, зупиняти, скидати та зберігати статистику сесії.

## Передумови

*   Python 3.8+
*   Бібліотеки **Flet** та **Scapy**.
*   **Права root/адміністратора:** Необхідні для захоплення мережевих пакетів.

## Встановлення та налаштування

### Варіант 1: Швидке встановлення (Linux - Рекомендовано)

Для користувачів Linux ми надаємо автоматизовані скрипти встановлення:

```bash
# 1. Клонуйте репозиторій
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Запустіть скрипт встановлення
./install.sh

# 3. Запустіть програму
./run.sh
```

Скрипт `install.sh` виконає:
- Встановлення системних залежностей (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Створення віртуального середовища Python
- Встановлення всіх необхідних пакетів Python (Flet, Scapy)

Скрипт `run.sh` автоматично запитає права root та запустить програму.

### Варіант 2: Ручне встановлення

#### 1. Встановлення системних залежностей

**На Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**На Windows:**

Встановіть Python 3.8+ з [python.org](https://www.python.org/downloads/)

#### 2. Встановлення залежностей Python

**На Linux (з використанням віртуального середовища - рекомендовано):**

```bash
# Створіть віртуальне середовище
python3 -m venv venv

# Активуйте віртуальне середовище
source venv/bin/activate

# Встановіть залежності
pip install flet scapy
```

**На Linux (системне встановлення):**

```bash
pip3 install flet scapy --break-system-packages
```

**На Windows:**

```bash
pip install flet scapy
```

#### 3. Запуск програми

Оскільки для перехоплення мережевого трафіку потрібні підвищені привілеї, ви повинні запускати програму як root або адміністратор.

**На Linux (з віртуальним середовищем):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**На Linux (системне встановлення):**

```bash
sudo python3 -m albion_insight
```

**На Windows (запустіть Командний рядок/PowerShell від імені адміністратора):**

```bash
python -m albion_insight
```

Програма відкриється у нативному вікні робочого столу.

## Як створити виконуваний файл

Програму можна упакувати в автономний виконуваний файл за допомогою **PyInstaller**. Це дозволяє користувачам запускати програму без встановлення Python або його залежностей.

Детальні інструкції зі створення виконуваних файлів для Linux, Windows та macOS дивіться у посібнику **[PACKAGING.md](PACKAGING.md)**.

### Швидка збірка (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Виконуваний файл буде розташований у папці `dist/`.

## Структура проєкту

Програма структурована на модульні компоненти для кращої підтримки та масштабованості:

| Файл | Опис |
| :--- | :--- |
| `albion_insight/core/` | Основна логіка, відстеження мережі, моделі даних та декодування протоколу. |
| `albion_insight/ui/` | Компоненти інтерфейсу користувача, створені за допомогою Flet. |
| `albion_insight/utils/` | Утиліти, конфігурація та логування. |
| `albion_insight/__main__.py` | Точка входу для програми. |
| `README.md` | Цей файл документації. |
| `CONTRIBUTING.md` | Настанови щодо внеску в проєкт. |
| `CODE_OF_CONDUCT.md` | Кодекс поведінки проєкту. |
| `SECURITY.md` | Політика повідомлення про вразливості безпеки. |
| `README.it-IT.md` | Documentazione in italiano. |
| `README.pt-BR.md` | Documentação em português do Brasil. |
| `README.ru-RU.md` | Документация на русском языке. |
| `README.fr-FR.md` | Documentation en français. |
| `README.zh-CN.md` | 简体中文文档 (Simplified Chinese documentation). |
| `README.ko-KR.md` | 한국어 문서 (Korean documentation). |
| `README.es-ES.md` | Documentación en español (Spanish documentation). |
| `README.de-DE.md` | Dokumentation in deutscher Sprache (German documentation). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Polish documentation). |
| `README.sv-SE.md` | Dokumentation på svenska (Swedish documentation). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (Vietnamese documentation). |
| `README.ar-SA.md` | توثيق باللغة العربية (Arabic documentation). |
| `README.pt-PT.md` | Documentação em português europeu. |
| `README.hi-IN.md` | Hindi में दस्तावेज़ीकरण (Hindi documentation). |
| `README.hu-HU.md` | Dokumentáció magyar nyelven (Hungarian documentation). |
| `README.th-TH.md` | เอกสารประกอบภาษาไทย (Thai documentation). |
| `README.ja-JP.md` | 日本語のドキュメント (Japanese documentation). |
| `README.tr-TR.md` | Türkçe dokümantasyon (Turkish documentation). |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia. |
| `README.sk-SK.md` | Dokumentácia v slovenčine (Slovak documentation). |
| `README.cs-CZ.md` | Dokumentace v češtině (Czech documentation). |
| `README.fi-FI.md` | Dokumentaatio suomeksi (Finnish documentation). |
| `README.nl-NL.md` | Documentatie in het Nederlands (Dutch documentation). |
| `README.zh-TW.md` | 繁體中文文件 (Traditional Chinese documentation). |
| `README.el-GR.md` | Τεκμηρίωση στα Ελληνικά (Greek documentation). |
| `README.fa-IR.md` | مستندات به زبان فارسی (Persian documentation). |
| `README.uk-UA.md` | Документація українською мовою (Ukrainian documentation). |

## Поточний стан (Дані в реальному часі)

Програма тепер включає логіку **Декодування Протоколу Photon**, перекладену з оригінального проєкту C#. Це дозволяє програмі обробляти події в реальному часі, такі як `UpdateMoney`, `UpdateFame`, `KilledPlayer` та `Died`, безпосередньо з мережевого трафіку.

**Примітка:** Повний переклад кожної окремої бойової події (наприклад, `CastHit`, `Attack`) є поточним завданням. Поточна реалізація зосереджена на основній статистиці та структурі для лічильника шкоди. Розрахунок DPS лічильника шкоди базується на декодованих подіях.

## Внесок

Ми вітаємо внесок від спільноти! Незалежно від того, чи є ви розробником, дизайнером або просто ентузіастом Albion Online, є багато способів допомогти покращити Albion Insight.

Будь ласка, прочитайте наші [Настанови щодо внеску](CONTRIBUTING.md) для отримання детальної інформації про те, як зробити внесок у цей проєкт.

### Швидкий старт для учасників:

1.  Створіть форк репозиторію: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Клонуйте свій форк: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Створіть нову гілку: `git checkout -b feature/your-feature-name`
4.  Внесіть свої зміни та зафіксуйте їх: `git commit -m "Add your feature"`
5.  Надішліть зміни до свого форку: `git push origin feature/your-feature-name`
6.  Відкрийте Pull Request у головному репозиторії

## Ліцензія

Цей проєкт ліцензовано за ліцензією MIT - дивіться файл [LICENSE](LICENSE) для отримання детальної інформації.

## Подяки

- Оригінальний проєкт: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) від Triky313
- Створено за допомогою фреймворку [Flet](https://flet.dev/)
- Мережевий аналіз забезпечується [Scapy](https://scapy.net/)

---
*Крос-платформне рішення для спільноти Albion Online.*
