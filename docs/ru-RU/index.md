# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Read this in English (Прочитать на английском)](README.md)**
**[Read this in German (Прочитать на немецком)](README.de-DE.md)**
**[Read this in Portuguese (Прочитать на португальском)](README.pt-BR.md)**
**[Read this in Spanish (Прочитать на испанском)](README.es-ES.md)**
**[Read this in French (Прочитать на французском)](README.fr-FR.md)**
**[Read this in Italian (Прочитать на итальянском)](README.it-IT.md)**
**[Read this in Simplified Chinese (Прочитать на упрощенном китайском)](README.zh-CN.md)**
**[Read this in Russian (Прочитать на русском)](README.ru-RU.md)**

**Albion Insight** — это кроссплатформенный (Linux, Windows, macOS) инструмент для анализа статистики в игре Albion Online, переписанный на **Python** с использованием фреймворка **Flet**. Он предназначен для отслеживания внутриигровой статистики в реальном времени, включая серебро, славу и боевые данные (Damage Meter), путем анализа сетевого трафика.

Этот проект является современной, открытой альтернативой оригинальному инструменту `AlbionOnline-StatisticsAnalysis` на базе C#/WPF, с акцентом на мультиплатformidade e простоту использования.

## Возможности

*   **Кроссплатформенность:** Работает нативно на Linux, Windows и macOS.
*   **Отслеживание в реальном времени:** Использует библиотеку `Scapy` для перехвата UDP-пакетов на портах Albion Online (5055, 5056, 5058).
*   **Структура Измерителя Урона (Damage Meter):** Включает необходимые структуры данных и пользовательский интерфейс для отображения статистики боя в реальном времени (Нанесенный Урон, Исцеление, DPS).
*   **Современный Пользовательский Интерфейс:** Создан с помощью Flet, обеспечивая быстрое, нативное настольное приложение.
*   **Управление Сессиями:** Позволяет запускать, останавливать, сбрасывать и сохранять статистику сессий.

## Предварительные требования

*   Python 3.8+
*   Библиотеки **Flet** и **Scapy**.
*   **Права Root/Администратора:** Необходимы для захвата сетевых пакетов.

## Установка и Настройка

### Вариант 1: Быстрая Установка (Linux - Рекомендуется)

Для пользователей Linux мы предоставляем автоматизированные скрипты установки:

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Запустите скрипт установки
./install.sh

# 3. Запустите приложение
./run.sh
```

Скрипт `install.sh` выполнит:
- Установку системных зависимостей (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Создание виртуального окружения Python
- Установку всех необходимых пакетов Python (Flet, Scapy)

Скрипт `run.sh` автоматически запросит права root и запустит приложение.

### Вариант 2: Ручная Установка

#### 1. Установите Системные Зависимости

**На Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**На Windows:**

Установите Python 3.8+ с [python.org](https://www.python.org/downloads/)

#### 2. Установите Зависимости Python

**На Linux (используя виртуальное окружение - рекомендуется):**

```bash
# Создайте виртуальное окружение
python3 -m venv venv

# Активируйте виртуальное окружение
source venv/bin/activate

# Установите зависимости
pip install flet scapy
```

**На Linux (системная установка):**

```bash
pip3 install flet scapy --break-system-packages
```

**На Windows:**

```bash
pip install flet scapy
```

#### 3. Запуск Приложения

Поскольку для перехвата сетевого трафика требуются повышенные привилегии, вы должны запускать приложение от имени root или администратора.

**На Linux (с виртуальным окружением):**

```bash
sudo venv/bin/python3 albion_insight.py
```

**На Linux (системная установка):**

```bash
sudo python3 albion_insight.py
```

**На Windows (Запустите Командную Строку/PowerShell от имени Администратора):**

```bash
python albion_insight.py
```

Приложение откроется в нативном настольном окне.

## Как Собрать Исполняемый Файл

Приложение может быть упаковано в автономный исполняемый файл с помощью **PyInstaller**. Это позволяет пользователям запускать приложение без установки Python или его зависимостей.

Подробные инструкции по сборке исполняемых файлов для Linux, Windows и macOS смотрите в руководстве **[PACKAGING.md](PACKAGING.md)**.

### Быстрая Сборка (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight.py
```

Исполняемый файл будет находиться в папке `dist/`.

## Структура Проекта

Все приложение содержится в одном файле для простоты:

| Файл | Описание |
| :--- | :--- |
| `albion_insight.py` | Основной файл приложения, содержащий всю логику (Модели, Сетевой Трекер, Пользовательский Интерфейс Flet). |
| `README.md` | Этот файл документации. |

## Текущий Статус (Данные в Реальном Времени)

Приложение теперь включает логику **Декодирования Протокола Photon**, переведенную с оригинального проекта на C#. Это позволяет приложению обрабатывать события в реальном времени, такие как `UpdateMoney`, `UpdateFame`, `KilledPlayer` и `Died`, непосредственно из сетевого трафика.

**Примечание:** Полный перевод каждого боевого события (например, `CastHit`, `Attack`) — это продолжающаяся работа. Текущая реализация сосредоточена на основной статистике и структуре для Измерителя Урона. Расчет DPS Измерителя Урона основан на декодированных событиях.

## Вклад в Проект

Мы приветствуем вклад сообщества! Независимо от того, являетесь ли вы разработчиком, дизайнером или просто энтузиастом Albion Online, есть много способов помочь улучшить Albion Insight.

Пожалуйста, прочтите наши [Руководящие Принципы Вклада](CONTRIBUTING.md) для получения подробной информации о том, как внести свой вклад в этот проект.

### Быстрый Старт для Участников:

1.  Сделайте форк репозитория: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Клонируйте свой форк: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Создайте новую ветку: `git checkout -b feature/your-feature-name`
4.  Внесите свои изменения и сделайте коммит: `git commit -m "Add your feature"`
5.  Отправьте изменения в свой форк: `git push origin feature/your-feature-name`
6.  Откройте Pull Request в основном репозитории

## Лицензия

Этот проект лицензирован по лицензии MIT - подробности смотрите в файле [LICENSE](LICENSE).

## Благодарности

- Оригинальный проект: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) от Triky313
- Создано с помощью фреймворка [Flet](https://flet.dev/)
- Сетевой анализ обеспечивается [Scapy](https://scapy.net/)

---
*Кроссплатформенное решение для сообщества Albion Online.*
