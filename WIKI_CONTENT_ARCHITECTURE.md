# Arquitetura Modular do Albion Insight

Este documento descreve a arquitetura modular do projeto Albion Insight, que foi reestruturado para facilitar a manutenção, o desenvolvimento de novas funcionalidades e a contribuição da comunidade.

## 1. Visão Geral da Arquitetura

O Albion Insight adota uma arquitetura limpa e modular, separando claramente as responsabilidades em três grandes áreas: **Core (Núcleo)**, **UI (Interface do Usuário)** e **Utils (Utilitários)**.

| Módulo | Responsabilidade Principal | Tecnologias Chave |
| :--- | :--- | :--- |
| **Core** | Lógica de negócio, análise de rede, modelos de dados. | Python, Scapy, Pydantic |
| **UI** | Apresentação de dados, interação com o usuário, gerenciamento de estado. | Python, Flet |
| **Utils** | Funções de suporte, logging, configuração. | Python, logging |

## 2. Detalhamento dos Módulos

### 2.1. Módulo `core`

Este é o coração da aplicação, responsável por toda a lógica de negócio e a interação de baixo nível com o sistema.

| Arquivo | Descrição |
| :--- | :--- |
| `core/models.py` | Define os modelos de dados (ex: `Player`, `SessionStats`) usando **Pydantic** para validação e tipagem. |
| `core/network_tracker.py` | Contém a lógica de decodificação de pacotes e o processamento de eventos do jogo (ex: `UpdateMoney`, `KilledPlayer`). |
| `core/sniffer_process.py` | Implementa o processo de captura de pacotes usando **Scapy**. Executado em um processo separado para não bloquear a UI. |
| `core/sniffer_manager.py` | Gerencia o ciclo de vida do `sniffer_process.py` (iniciar, parar, reiniciar) e a comunicação entre o sniffer e a UI. |
| `core/main_logic.py` | Orquestra a inicialização do `SnifferManager` e da UI. |
| `core/exceptions.py` | Define exceções personalizadas para o módulo `core`. |

### 2.2. Módulo `ui`

Responsável pela apresentação visual e pela interação com o usuário. Utiliza o framework **Flet** para criar uma aplicação desktop nativa.

| Arquivo | Descrição |
| :--- | :--- |
| `ui/main_window.py` | Define a estrutura principal da janela da aplicação e o layout geral. |
| `ui/app.py` | Contém a função de inicialização do Flet (`ft.app`). |
| `ui/components/` | Diretório para componentes reutilizáveis da UI (ex: `DamageMeterView`, `SessionControls`). |

### 2.3. Módulo `utils`

Contém funções de suporte que são usadas em toda a aplicação.

| Arquivo | Descrição |
| :--- | :--- |
| `utils/logger.py` | Configuração centralizada do sistema de logging. |
| `utils/config.py` | Gerencia as configurações da aplicação (ex: portas de rede, caminhos de arquivo). |
| `utils/helpers.py` | Funções auxiliares diversas (ex: formatação de números, conversão de tempo). |

## 3. Fluxo de Execução

1.  **Início:** O script `__main__.py` chama `core.main_logic.main()`.
2.  **Gerenciamento:** `main()` inicializa o `core.sniffer_manager.SnifferManager`.
3.  **UI:** `main()` chama `ui.main_window.run_app()`, que inicia a interface Flet.
4.  **Comunicação:** A UI interage com o `SnifferManager` para iniciar ou parar a captura de pacotes.
5.  **Captura:** Quando iniciado, o `SnifferManager` lança o `core.sniffer_process.SnifferProcess` em um processo separado.
6.  **Análise:** O `SnifferProcess` usa `Scapy` para capturar pacotes e o `core.network_tracker.NetworkTracker` para decodificar e processar os dados do jogo.
7.  **Atualização:** Os dados processados são comunicados de volta ao `SnifferManager` (geralmente via *queues* ou *pipes* em Python) e, em seguida, atualizam o estado da UI.

Esta separação garante que a UI permaneça responsiva, mesmo durante a intensa atividade de captura e processamento de pacotes de rede.
