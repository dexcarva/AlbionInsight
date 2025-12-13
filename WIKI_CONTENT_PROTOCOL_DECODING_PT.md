# Decodificação do Protocolo Photon no Albion Insight

O **Albion Insight** opera como um *sniffer* de pacotes de rede, interceptando o tráfego de dados entre o cliente do jogo **Albion Online** e seus servidores. A chave para a funcionalidade da ferramenta reside na sua capacidade de **decodificar** o protocolo de comunicação utilizado pelo jogo, que é baseado no **Photon Engine**.

## O que é o Photon Engine?

O Photon Engine é uma solução de *middleware* de rede popularmente usada em jogos *multiplayer* para gerenciar a comunicação em tempo real. Ele utiliza um protocolo binário otimizado para baixa latência, o que o torna eficiente, mas também opaco para ferramentas externas.

No contexto do Albion Online, o Photon é usado para transmitir eventos de jogo, como:
*   Movimentação de jogadores.
*   Atualizações de inventário e moedas.
*   Eventos de combate (dano, cura, mortes).
*   Interações com o mundo (coleta, *crafting*).

## O Processo de Decodificação

A decodificação do protocolo Photon no Albion Insight é uma tradução e adaptação da lógica de engenharia reversa aplicada no projeto original em C# (`AlbionOnline-StatisticsAnalysis`). O processo segue as seguintes etapas:

### 1. Captura de Pacotes (Scapy)

O Albion Insight utiliza a biblioteca **Scapy** para capturar pacotes UDP nas portas específicas do Albion Online (geralmente 5055, 5056 e 5058). A Scapy é uma ferramenta poderosa que permite a manipulação e análise de pacotes de rede.

### 2. Identificação do Protocolo Photon

Cada pacote capturado é inspecionado para confirmar se ele contém dados do Photon. O protocolo Photon tem uma estrutura de cabeçalho bem definida que permite à ferramenta identificar o início e o fim de uma mensagem de jogo.

### 3. Desserialização dos Dados

O Photon utiliza um formato de serialização binária para compactar os dados antes da transmissão. A lógica de decodificação do Albion Insight é responsável por:
*   **Desserializar** os dados binários de volta para estruturas de dados legíveis (como dicionários e listas em Python).
*   **Identificar o Código de Operação (OpCode):** Cada mensagem de jogo tem um `OpCode` que indica o tipo de evento que está sendo transmitido (ex: `OpCode 1` pode ser "Login", `OpCode 10` pode ser "UpdateMoney").
*   **Mapear Parâmetros:** O corpo da mensagem contém parâmetros (chaves e valores) que são mapeados para as informações relevantes do jogo (ex: `Key 2` pode ser o valor da prata, `Key 3` pode ser o valor da fama).

### 4. Extração de Estatísticas

Uma vez que o pacote é desserializado e o `OpCode` é identificado, o Albion Insight extrai as informações de interesse e as armazena em seus modelos de dados internos.

| Evento Decodificado | Informação Extraída | Aplicação na Ferramenta |
| :--- | :--- | :--- |
| `UpdateMoney` | Valor atual de Prata | Atualização do saldo financeiro do jogador. |
| `UpdateFame` | Valor de Fama | Cálculo de Fama por Hora (FPH). |
| `KilledPlayer` | ID do jogador morto, ID do assassino | Registro de Kills e Deaths na sessão. |
| `Died` | ID do jogador que morreu | Registro de Kills e Deaths na sessão. |
| `CastHit` / `Attack` | Dano/Cura causado, alvo | **Base para o Medidor de Dano (DPS/HPS).** |

## Desafios e Desenvolvimento Contínuo

A decodificação do protocolo é um esforço contínuo, pois o Albion Online pode receber atualizações que alteram a estrutura dos pacotes ou os `OpCodes`.

*   **Tradução de Eventos de Combate:** A tradução completa de todos os eventos de combate (como `CastHit` e `Attack`) é a área de maior desenvolvimento, pois é crucial para a precisão do Medidor de Dano.
*   **Manutenção:** A comunidade deve estar atenta a grandes atualizações do jogo que possam quebrar a lógica de decodificação, exigindo engenharia reversa e adaptação contínuas.

Este guia serve como um ponto de partida para desenvolvedores que desejam contribuir para a lógica de decodificação do `albion_insight/core/` e garantir que a ferramenta permaneça funcional e precisa.
