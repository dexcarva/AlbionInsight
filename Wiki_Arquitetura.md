# Arquitetura do Projeto Albion Insight

O Albion Insight foi projetado com uma arquitetura modular para garantir a separação de responsabilidades, facilidade de manutenção e escalabilidade. A estrutura é dividida em três componentes principais: **Core (Núcleo)**, **UI (Interface do Usuário)** e **Utils (Utilitários)**.

## 1. Core (Núcleo)

O módulo `core` contém a lógica de negócios e a funcionalidade principal da aplicação, que é o rastreamento e decodificação do tráfego de rede do Albion Online.

| Componente | Descrição | Responsabilidade Principal |
| :--- | :--- | :--- |
| `network_tracker.py` | Gerencia a captura de pacotes de rede usando `Scapy`. | Iniciar e parar a captura, filtrar pacotes relevantes. |
| `sniffer_process.py` | Processo separado que executa a captura de pacotes com privilégios de root. | Execução segura da lógica de captura de rede. |
| `models.py` | Define as estruturas de dados para estatísticas (e.g., Silver, Fame, Damage Meter), usando classes Python padrão. | Manter o estado da sessão e os dados do jogo. |
| `main_logic.py` | Ponto de orquestração que inicializa o `Core` e a UI. | Coordenação entre os módulos. |

## 2. UI (Interface do Usuário)

O módulo `ui` é responsável pela apresentação visual da aplicação, construída com o framework Flet.

| Componente | Descrição | Responsabilidade Principal |
| :--- | :--- | :--- |
| `app.py` | Define a estrutura principal da aplicação Flet. | Configuração da janela, temas e rotas. |
| `main_window.py` | Contém a janela principal e a lógica de layout. | Gerenciamento da interface principal. |
| `components/` | Contém os componentes visuais reutilizáveis (e.g., botões de controle, exibição do Damage Meter). | Interação com o usuário e exibição de dados. |

## 3. Utils (Utilitários)

O módulo `utils` contém funções auxiliares e configurações globais.

| Componente | Descrição | Responsabilidade Principal |
| :--- | :--- | :--- |
| `config.py` | Classe que gerencia configurações como diretórios de log, portas de rede e nível de debug. | Fornecer configurações centralizadas e garantir a existência de diretórios. |
| `logger.py` | Configuração centralizada do sistema de logging. | Gerenciamento de logs para depuração e monitoramento. |
| `helpers.py` | Funções auxiliares genéricas (e.g., formatação de números e tempo). | Reutilização de código e simplificação de tarefas comuns. |

## Fluxo de Execução

1. O script de entrada (`run.sh` ou `__main__.py`) chama a lógica principal em `albion_insight/core/main_logic.py`.
2. O `main_logic` inicializa a configuração (`config.py`) e o logger (`logger.py`).
3. O `main_logic` inicia a interface Flet chamando `app.py`.
4. A UI interage com o `main_logic` para iniciar ou parar o processo de captura de pacotes (`network_tracker.py`).
5. O `sniffer_process.py` (executado com `sudo`) captura e decodifica os pacotes, enviando os dados de volta para o `main_logic` (e, consequentemente, para a UI) via comunicação entre processos (IPC).
6. A UI atualiza os modelos de dados e exibe as estatísticas em tempo real para o usuário.

---

# Albion Insight Project Architecture (English Translation)

The Albion Insight project is designed with a modular architecture to ensure separation of concerns, ease of maintenance, and scalability. The structure is divided into three main components: **Core**, **UI (User Interface)**, and **Utils (Utilities)**.

## 1. Core

The `core` module contains the business logic and the main functionality of the application, which is the tracking and decoding of Albion Online network traffic.

| Component | Description | Primary Responsibility |
| :--- | :--- | :--- |
| `network_tracker.py` | Manages network packet capture using `Scapy`. | Start and stop capture, filter relevant packets. |
| `sniffer_process.py` | Separate process that executes packet capture with root privileges. | Secure execution of network sniffing logic. |
| `models.py` | Defines data structures for statistics (e.g., Silver, Fame, Damage Meter), using standard Python classes. | Maintain session state and game data. |
| `main_logic.py` | Orchestration point that initializes the `Core` and the UI. | Coordination between modules. |

## 2. UI (User Interface)

The `ui` module is responsible for the visual presentation of the application, built with the Flet framework.

| Component | Description | Primary Responsibility |
| :--- | :--- | :--- |
| `app.py` | Defines the main structure of the Flet application. | Window configuration, themes, and routes. |
| `main_window.py` | Contains the main window and layout logic. | Management of the primary interface. |
| `components/` | Contains reusable visual components (e.g., control buttons, Damage Meter display). | User interaction and data display. |

## 3. Utils (Utilities)

The `utils` module contains auxiliary functions and global configurations.

| Component | Description | Primary Responsibility |
| :--- | :--- | :--- |
| `config.py` | Class that manages configurations such as log directories, network ports, and debug level. | Provide centralized configuration and ensure directory existence. |
| `logger.py` | Centralized configuration of the logging system. | Management of logs for debugging and monitoring. |
| `helpers.py` | Generic auxiliary functions (e.g., number and time formatting). | Code reuse and simplification of common tasks. |

## Execution Flow

1. The entry script (`run.sh` or `__main__.py`) calls the main logic in `albion_insight/core/main_logic.py`.
2. `main_logic` initializes the configuration (`config.py`) and the logger (`logger.py`).
3. `main_logic` starts the Flet interface by calling `app.py`.
4. The UI interacts with `main_logic` to start or stop the packet capture process (`network_tracker.py`).
5. `sniffer_process.py` (executed with `sudo`) captures and decodes packets, sending the data back to `main_logic` (and consequently to the UI) via Inter-Process Communication (IPC).
6. The UI updates the data models and displays real-time statistics to the user.
