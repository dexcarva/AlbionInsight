# Decodificação do Protocolo Photon

O Albion Insight depende da decodificação correta do protocolo de rede do Albion Online, que é baseado no **Photon Engine**. Esta página da Wiki serve como um guia para entender como a decodificação funciona e como os contribuidores podem ajudar a expandir a funcionalidade do aplicativo.

## O que é o Photon Engine?

O Photon Engine é uma solução de rede em tempo real amplamente utilizada em jogos multiplayer. Ele usa um sistema de eventos, operações e respostas para sincronizar o estado do jogo entre o servidor e os clientes.

No Albion Insight, o código de decodificação (`PhotonParser` em `albion_insight.py`) é uma tradução do `Protocol16Deserializer` do projeto original em C#.

## Estrutura da Mensagem Photon

As mensagens do Photon são estruturadas em torno de três tipos principais:

1.  **Eventos (`EventData`):** Usados pelo servidor para notificar os clientes sobre mudanças no estado do jogo (ex: `UpdateMoney`, `KilledPlayer`, eventos de combate).
2.  **Requisições de Operação (`OperationRequest`):** Enviadas pelo cliente ao servidor (ex: mover-se, usar uma habilidade).
3.  **Respostas de Operação (`OperationResponse`):** Enviadas pelo servidor em resposta a uma requisição de operação.

Cada mensagem contém um **código** que identifica o evento ou operação específica, e uma **tabela de parâmetros** (um dicionário) que contém os dados relevantes.

## Como Contribuir com a Decodificação

A maior parte do trabalho de expansão do Albion Insight reside em identificar e decodificar novos eventos e operações.

### 1. Captura de Dados

Para identificar novos eventos, você precisa capturar o tráfego de rede enquanto realiza a ação no jogo.

*   **Ferramenta:** Use o próprio Albion Insight ou ferramentas como **Wireshark** com o filtro `udp port 5055 or 5056 or 5058`.
*   **Ação:** Realize a ação que você deseja decodificar (ex: usar uma habilidade específica, coletar um recurso, negociar).
*   **Isolamento:** Tente isolar a ação o máximo possível para reduzir o ruído no tráfego.

### 2. Análise de Pacotes

Após a captura, o pacote UDP precisa ser analisado para encontrar a mensagem Photon.

*   **Payload:** O payload do pacote UDP (após o cabeçalho Enet/Photon) é o que o `PhotonParser` tenta decodificar.
*   **Identificação:** Procure por mensagens do tipo **EventData** (código 101) ou **OperationResponse** (código 112) que ocorrem imediatamente após a ação.

### 3. Mapeamento de Códigos e Parâmetros

O objetivo é mapear o **código do evento/operação** para a ação no jogo e entender o significado de cada **parâmetro** na tabela.

| Exemplo de Evento | Código (Byte) | Parâmetros Chave | Significado |
| :--- | :--- | :--- | :--- |
| `UpdateMoney` | `~2` (Exemplo) | `1: (int) SilverAmount` | Quantidade de prata atualizada. |
| `CastHit` | `~5` (Exemplo) | `2: (int) TargetID`, `3: (float) Damage` | Dano causado a um alvo. |

**Se você identificar um novo evento:**

1.  **Documente** o código do evento e os parâmetros que você conseguiu identificar.
2.  **Implemente** a lógica de processamento no método `NetworkTracker._process_photon_message` em `albion_insight.py`.
3.  **Abra um Pull Request** com suas descobertas e implementações.

## Estrutura de Dados em Python

O `PhotonParser` usa os seguintes métodos para desserializar os tipos de dados do Photon:

*   `deserialize_byte()` -> `Byte`
*   `deserialize_short()` -> `Short` (2 bytes)
*   `deserialize_integer()` -> `Integer` (4 bytes)
*   `deserialize_long()` -> `Long` (8 bytes)
*   `deserialize_string()` -> `String`
*   `deserialize_hashtable()` -> `Dictionary/Hashtable`

Ao analisar os pacotes, o tipo de dado de cada parâmetro é crucial para a decodificação correta.

**Sua contribuição é vital para expandir a funcionalidade do Albion Insight!**
