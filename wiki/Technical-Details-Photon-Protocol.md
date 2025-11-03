# Detalhes Técnicos: Protocolo Photon

O Albion Insight opera analisando o tráfego de rede do jogo Albion Online, que utiliza o **Photon Engine** para comunicação. Esta página detalha a lógica de decodificação e serve como referência para desenvolvedores.

## O Protocolo Photon

O Photon é um motor de rede que utiliza um sistema de mensagens baseado em:

*   **Eventos:** Mensagens enviadas do servidor para o cliente (ex: `UpdateMoney`, eventos de combate).
*   **Operações:** Mensagens enviadas do cliente para o servidor (ex: `Move`, `CastSpell`).
*   **Respostas:** Mensagens do servidor em resposta a uma Operação.

Cada mensagem é composta por um **código** (identificador da ação) e uma **tabela de parâmetros** (dados da ação).

## Lógica de Decodificação

A lógica de decodificação do Albion Insight está contida na classe `PhotonParser` (localizada em `network_tracker.py` após a refatoração). Esta classe é uma tradução do `Protocol16Deserializer` do projeto original em C#.

### Tipos de Dados do Protocolo 16

O `PhotonParser` desserializa os dados com base em códigos de tipo (Type Codes), como:

| Código | Tipo de Dado | Método de Desserialização |
| :--- | :--- | :--- |
| `98` | Byte | `deserialize_byte()` |
| `107` | Short (2 bytes) | `deserialize_short()` |
| `105` | Integer (4 bytes) | `deserialize_integer()` |
| `108` | Long (8 bytes) | `deserialize_long()` |
| `115` | String | `deserialize_string()` |
| `104` | Hashtable (Dicionário) | `deserialize_hashtable()` |
| `101` | EventData | `deserialize_event_data()` |
| `112` | OperationResponse | `deserialize_operation_response()` |
| `113` | OperationRequest | `deserialize_operation_request()` |

### O Processo de Análise

1.  **Captura:** O `NetworkTracker` usa `scapy` para capturar pacotes UDP nas portas 5055, 5056 e 5058.
2.  **Verificação do Cabeçalho:** O `PhotonParser.parse_photon_message` verifica o cabeçalho Enet/Photon (geralmente 1 byte) e o remove.
3.  **Desserialização:** O parser lê o código de tipo da mensagem e chama o método de desserialização apropriado (ex: `deserialize_event_data`).
4.  **Processamento:** O `NetworkTracker` recebe o dicionário de dados decodificados e atualiza o estado do jogo (ex: adiciona dano ao jogador).

## Como Expandir a Decodificação

Para adicionar suporte a novos eventos (ex: novos feitiços de combate, novos eventos de coleta), os contribuidores devem:

1.  **Capturar o Tráfego:** Usar o Wireshark ou o próprio Albion Insight para capturar o tráfego durante a ação desejada.
2.  **Identificar o Evento:** Localizar o pacote UDP que contém a mensagem Photon relevante.
3.  **Mapear:** Identificar o **código do evento** e o **significado dos parâmetros** na tabela de dados.
4.  **Implementar:** Adicionar a lógica de processamento no método `_process_photon_message` do `NetworkTracker` para extrair os dados relevantes.

**Sua ajuda na decodificação é crucial para a funcionalidade completa do Damage Meter!**
