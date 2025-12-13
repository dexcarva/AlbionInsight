# Arquitetura Modular do Albion Insight

O **Albion Insight** foi projetado com uma arquitetura modular para garantir **manutenibilidade**, **escalabilidade** e **separação de preocupações** (Separation of Concerns). A estrutura é dividida em três componentes principais: Core, UI e Utilities.

## 1. Visão Geral da Arquitetura

| Componente | Diretório | Responsabilidade Principal | Tecnologias Chave |
| :--- | :--- | :--- | :--- |
| **Core** | `albion_insight/core/` | Lógica de Negócio, Decodificação de Protocolo, Modelos de Dados. | Python, Scapy, Modelos de Dados (Classes Python) |
| **UI (User Interface)** | `albion_insight/ui/` | Apresentação de Dados, Interação com o Usuário, Layout. | Flet Framework |
| **Utilities** | `albion_insight/utils/` | Funções Auxiliares, Configuração, Logging, Gerenciamento de Sessão. | Python Padrão, Logging Module |

## 2. Fluxo de Dados e Decodificação do Protocolo Photon

O coração do Albion Insight é a capacidade de analisar o tráfego de rede do jogo.

### A. Captura de Pacotes (Scapy)

1.  A biblioteca **Scapy** é inicializada com privilégios de `root`/administrador.
2.  Ela "cheira" (sniffs) pacotes UDP nas portas 5055, 5056 e 5058, que são as portas usadas pelo protocolo **Photon** do Albion Online.
3.  Os pacotes capturados são passados para o módulo de decodificação.

### B. Decodificação do Protocolo Photon

*   O módulo de decodificação (`albion_insight/core/protocol_decoder.py`) é responsável por traduzir os dados binários do protocolo Photon em eventos e dados estruturados legíveis.
*   Esta lógica foi portada do projeto original em C# para Python, garantindo a compatibilidade com a estrutura de dados do jogo.
*   **Eventos Decodificados:** O sistema é capaz de identificar e processar eventos cruciais em tempo real, como:
    *   `UpdateMoney` (Atualização de Prata)
    *   `UpdateFame` (Atualização de Fama)
    *   `KilledPlayer` (Jogador Abatido)
    *   `Died` (Morte do Jogador)
    *   *Nota:* A tradução completa de todos os eventos de combate (`CastHit`, `Attack`) está em andamento.

### C. Modelos de Dados (Core)

*   Os dados decodificados são armazenados em **Modelos de Dados** (classes Python) que representam entidades do jogo (ex: `Player`, `SessionStats`, `CombatLogEntry`).
*   Esses modelos garantem que os dados sejam consistentes e fáceis de manipular pela lógica de negócio.

## 3. Camada de Interface (Flet)

*   A camada de UI (`albion_insight/ui/`) consome os dados processados pelo Core.
*   O framework **Flet** é usado para construir uma interface de desktop moderna e nativa, que funciona em Linux, Windows e macOS.
*   O UI é responsável por:
    *   Exibir o **Damage Meter** em tempo real.
    *   Mostrar as estatísticas de sessão (Prata, Fama).
    *   Gerenciar a interação do usuário (botões de Iniciar/Parar/Resetar).

## 4. Logging e Configuração (Utilities)

*   O módulo `albion_insight/utils/` lida com tarefas não-funcionais, como:
    *   **Logging:** Registro de eventos e erros para facilitar a depuração.
    *   **Configuração:** Carregamento de configurações do usuário e do sistema.
    *   **Persistência:** Lógica para salvar e carregar estatísticas de sessão.
