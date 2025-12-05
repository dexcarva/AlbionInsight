# Guia de Contribuição: Decodificação do Protocolo Photon

A funcionalidade central do **Albion Insight** reside na sua capacidade de analisar o tráfego de rede do jogo para extrair estatísticas em tempo real. Isso é feito através da decodificação do **Protocolo Photon**, que é o protocolo de comunicação proprietário utilizado pelo Albion Online.

Este guia destina-se a colaboradores que desejam ajudar a expandir e manter a precisão da decodificação do protocolo.

## 1. O Desafio do Protocolo Photon

O Photon é um protocolo de rede de alto desempenho, mas é proprietário e não documentado publicamente pela Sandbox Interactive. Além disso, o protocolo pode sofrer alterações com atualizações do jogo, o que exige um esforço contínuo da comunidade para manter a decodificação atualizada.

Nossa implementação atual é baseada em engenharia reversa e na tradução da lógica do projeto original em C#, mas ainda há muitos eventos de combate e de jogo que precisam ser mapeados.

## 2. Pré-requisitos para Contribuição

Para contribuir com a decodificação, é necessário ter:

*   **Conhecimento Básico de Redes:** Entendimento de pacotes UDP e portas de comunicação.
*   **Familiaridade com Python e Scapy:** A biblioteca Scapy é a ferramenta que utilizamos para a captura e manipulação dos pacotes.
*   **Ferramentas de Análise de Tráfego:** **Wireshark** ou **TShark** são essenciais para capturar e inspecionar o tráfego de rede do Albion Online.

## 3. Processo de Decodificação Passo a Passo

O processo de contribuição segue as seguintes etapas:

### Passo 3.1: Captura de Tráfego Relevante

1.  **Inicie o Wireshark/TShark:** Comece a capturar o tráfego de rede na interface que o Albion Online está utilizando.
2.  **Filtro de Portas:** Aplique um filtro para focar apenas nos pacotes do Albion Online. As portas conhecidas são: `udp port 5055 or udp port 5056 or udp port 5058`.
3.  **Execute a Ação no Jogo:** Realize a ação específica que você deseja decodificar (ex: usar uma habilidade, receber um item, matar um mob, etc.).
4.  **Pare a Captura:** Interrompa a captura imediatamente após a ação para isolar o pacote relevante.

### Passo 3.2: Identificação e Isolamento do Pacote

1.  **Localize o Pacote:** No Wireshark, procure o pacote que corresponde ao momento exato da ação.
2.  **Análise do Payload:** O payload (dados) do pacote UDP é o que contém a mensagem do Photon. O Photon utiliza um formato de serialização binária.
3.  **Identifique o Evento:** O primeiro byte ou conjunto de bytes do payload geralmente indica o **ID do Evento** ou o **Código de Operação**. Este é o ponto de partida para mapear a função.

### Passo 3.3: Mapeamento e Implementação no Código

1.  **Crie um Cenário de Teste:** No seu ambiente de desenvolvimento, crie um pequeno script ou utilize a estrutura de testes existente para simular a decodificação do payload capturado.
2.  **Mapeie o ID:** No código do Albion Insight (principalmente em `albion_insight/core/models.py` e `albion_insight/core/main_logic.py`), adicione o mapeamento do ID do evento que você identificou para um nome de evento legível (ex: `EVENT_ID_CAST_HIT = 123`).
3.  **Implemente a Lógica de Extração:** Escreva a lógica de decodificação para extrair os dados relevantes do payload (ex: ID do jogador, valor do dano, tipo de item).

## 4. Submissão da Contribuição

Ao submeter um Pull Request com melhorias na decodificação, inclua:

*   **Descrição Clara:** Explique qual evento ou operação você decodificou.
*   **Amostra do Pacote (Opcional, mas Recomendado):** Se possível, inclua uma amostra do payload binário ou um screenshot da análise do Wireshark para validação.
*   **Testes:** Certifique-se de que a nova lógica de decodificação esteja coberta por testes unitários.

Sua contribuição é vital para o sucesso do Albion Insight! Juntos, podemos fornecer a ferramenta de análise mais precisa e completa para a comunidade Albion Online.
