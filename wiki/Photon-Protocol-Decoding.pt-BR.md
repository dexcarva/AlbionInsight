# Decodificação do Protocolo Photon

**[Read in English](Photon-Protocol-Decoding.md)**

## Visão Geral

Albion Online usa o motor de rede **Photon**, especificamente o **Protocolo 1.6**, para comunicação cliente-servidor. A função central do Albion Insight é decodificar esses pacotes proprietários para extrair estatísticas de jogo significativas.

A lógica de decodificação é implementada na classe `PhotonParser` dentro de `albion_insight.py`, que é uma tradução direta do `Protocol16Deserializer` em C# do projeto original AlbionOnline-StatisticsAnalysis.

## A Classe `PhotonParser`

O `PhotonParser` é responsável por ler o payload de bytes brutos de um pacote de rede e convertê-lo em tipos de dados estruturados do Python (dicionários, listas, inteiros, strings).

### Métodos Chave

| Método | Descrição |
| :--- | :--- |
| `deserialize()` | O ponto de entrada principal. Lê o código de tipo e chama o método de desserialização apropriado. |
| `_deserialize(type_code)` | Lida com a desserialização recursiva com base no código de tipo. |
| `deserialize_byte()`, `deserialize_short()`, etc. | Métodos para ler tipos de dados primitivos usando o módulo `struct` do Python para a ordem de bytes correta (`>h`, `>i`, etc.). |
| `deserialize_dictionary()` | Lida com tipos complexos como `Dictionary` (pares chave/valor tipados). |
| `deserialize_hashtable()` | Lida com o tipo `Hashtable` (pares chave/valor não tipados, usados para parâmetros de evento). |
| `deserialize_event_data()` | Decodifica um Evento Photon completo, que contém um código de evento e uma tabela de parâmetros. |
| `deserialize_parameter_table()` | Decodifica os pares chave-valor que compõem os parâmetros do evento. |

## Estrutura do Evento

Um pacote de evento Photon típico, após a remoção dos cabeçalhos da camada de transporte, segue esta estrutura:

1.  **Código de Tipo**: Um único byte indicando o tipo de mensagem (por exemplo, `101` para `EventData`).
2.  **Código de Evento**: Um único byte identificando o evento de jogo específico (por exemplo, `1` para `UpdateMoney`, `10` para `KilledPlayer`).
3.  **Tabela de Parâmetros**: Uma `Hashtable` contendo os dados do evento.

### Exemplo: Evento `UpdateMoney`

O evento `UpdateMoney` (Código de Evento `1`) é um evento crucial para rastrear prata. Sua tabela de parâmetros tipicamente contém:

| Chave do Parâmetro (Byte) | Tipo de Valor | Descrição |
| :--- | :--- | :--- |
| `1` | `Integer` | A quantidade de prata ganha ou perdida. |
| `2` | `Integer` | O novo total de prata. |
| `3` | `Byte` | O tipo de moeda (por exemplo, `1` para Prata). |

O `NetworkTracker` processa esses dados decodificados para atualizar o modelo `LiveStats`.

## Limitações e Trabalho Futuro

A implementação atual é funcional, mas possui limitações herdadas da tradução do projeto original:

1.  **Cobertura Parcial de Eventos de Combate**: Embora os eventos centrais sejam tratados, muitas habilidades e efeitos de combate específicos ainda não estão totalmente mapeados e decodificados. É por isso que o medidor de dano é atualmente rotulado como "(Simulado)" na UI.
2.  **Simplificação da Camada de Transporte**: O método `PhotonParser.parse_photon_message` faz uma suposição simplificadora sobre os cabeçalhos de transporte Enet/Photon. Uma implementação mais robusta exigiria uma pilha de protocolo Enet/Photon completa para lidar com fragmentação e entrega confiável.
3.  **Tipos Ausentes**: Alguns tipos Photon complexos ou menos usados (por exemplo, `Array`, `CustomType`) podem não estar totalmente implementados ou testados.

Contribuições da comunidade são altamente encorajadas para ajudar a mapear e implementar os códigos de evento Photon restantes para maior precisão. Consulte as [Diretrizes de Contribuição](../CONTRIBUTING.pt-BR.md) para mais informações.
