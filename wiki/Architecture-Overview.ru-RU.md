# Обзор Архитектуры Albion Insight
Albion Insight разработан с использованием модульного подхода на **Python** с фреймворком **Flet** для кроссплатформенного пользовательского интерфейса.
 
## Основные Компоненты
 
1.  **Network Tracker (Scapy):** Отвечает за захват и фильтрацию сетевого трафика Albion Online (UDP-пакеты на портах 5055, 5056, 5058).
2.  **Photon Protocol Decoder:** Переводит бинарные данные из пакетов в структурированные игровые события (например, `UpdateMoney`, `KilledPlayer`).
3.  **Data Models:** Классы Python, представляющие игровые сущности и статистику (например, `Player`, `SessionStats`).
4.  **Flet UI:** Пользовательский интерфейс, отображающий статистику в реальном времени, включая Damage Meter.
 
## Структура Проекта
 
Проект организован в модули для лучшей поддерживаемости:
 
```
AlbionInsight/
├── albion_insight/
│   ├── core/         # Lógica de negócios, modelos de dados, decodificação
│   ├── ui/           # Componentes da interface do usuário Flet
│   └── main.py       # Ponto de entrada e inicialização do aplicativo
├── albion_insight.py # Novo ponto de entrada (wrapper)
└── ...
```
