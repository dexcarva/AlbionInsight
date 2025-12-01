# Wiki: Contribuindo para a Decodificação do Protocolo Photon

O Albion Insight depende da decodificação correta do protocolo de rede do Albion Online (baseado no Photon Engine) para rastrear estatísticas em tempo real. A tradução completa da lógica do projeto original em C# para Python é um esforço contínuo.

Esta página da Wiki serve como um guia para contribuidores interessados em ajudar na engenharia reversa e na implementação de novos eventos do protocolo.

## 1. Entendendo o Protocolo Photon

O Albion Online utiliza o **Photon Engine** para comunicação em rede. O Photon é um framework de rede em tempo real que usa mensagens e operações para sincronizar o estado do jogo.

- **Operações (Operations):** Mensagens enviadas do cliente para o servidor (e vice-versa) para iniciar ações (ex: `CastSpell`, `Move`).
- **Eventos (Events):** Mensagens enviadas pelo servidor para o cliente para notificar sobre mudanças de estado (ex: `UpdateMoney`, `KilledPlayer`).

A decodificação envolve mapear os IDs numéricos dessas operações e eventos para suas respectivas estruturas de dados e lógica de processamento.

## 2. Ferramentas Necessárias

Para contribuir com a decodificação, você precisará de:

| Ferramenta | Propósito |
| :--- | :--- |
| **Wireshark** | Captura e análise de pacotes de rede (UDP). |
| **Albion Insight** | Para verificar como os eventos já implementados são processados. |
| **Projeto Original C#** | A fonte primária de referência para a lógica de decodificação. |
| **Decompilador C#** | Ferramentas como **ILSpy** ou **dnSpy** para inspecionar o código-fonte do projeto original. |

## 3. Processo de Decodificação (Passo a Passo)

### Passo 1: Captura de Tráfego

1.  Inicie o Wireshark e filtre o tráfego para as portas do Albion Online (5055, 5056, 5058).
2.  Execute a ação no jogo que você deseja decodificar (ex: usar uma habilidade, abrir um baú).
3.  Pare a captura e localize o pacote UDP relevante.

### Passo 2: Identificação do Evento/Operação

1.  No Wireshark, identifique o pacote que contém a mensagem do Photon.
2.  O cabeçalho do Photon contém o **ID do Evento** ou **ID da Operação**.
3.  Anote o ID e os dados brutos (payload) da mensagem.

### Passo 3: Engenharia Reversa da Lógica

1.  Abra o código-fonte do projeto original em C# (AlbionOnline-StatisticsAnalysis) em um decompilador.
2.  Procure pela lógica de processamento que corresponde ao ID do Evento/Operação que você identificou.
3.  Analise como os dados brutos (payload) são lidos e mapeados para as variáveis do jogo (ex: qual byte é o valor do dano, qual é o ID do jogador).

### Passo 4: Implementação em Python

1.  No `albion_insight/core/network_tracker.py` ou módulos relacionados, crie uma nova função de decodificação.
2.  Use a biblioteca `scapy` para manipular os pacotes e a lógica de decodificação traduzida do C# para Python.
3.  Mapeie os dados decodificados para os modelos de dados do Albion Insight (ex: `albion_insight/core/models.py`).

### Passo 5: Teste e Validação

1.  Execute o Albion Insight e reproduza a ação no jogo.
2.  Verifique se o seu novo código de decodificação está processando o evento corretamente.
3.  Crie um teste unitário (em `tests/`) para garantir que a decodificação funcione com um pacote de exemplo.

## 4. Eventos de Combate Prioritários

A prioridade atual é completar a decodificação dos eventos de combate para aprimorar o Medidor de Dano:

| Evento (Exemplo C#) | ID (Exemplo) | Descrição | Status no Albion Insight |
| :--- | :--- | :--- | :--- |
| `CastHit` | 42 | Dano causado por uma habilidade. | **Pendente** |
| `Attack` | 43 | Dano causado por ataque básico. | **Pendente** |
| `Heal` | 44 | Cura realizada. | **Pendente** |
| `UpdateMoney` | 1 | Atualização de prata. | **Implementado** |
| `KilledPlayer` | 10 | Um jogador foi morto. | **Implementado** |

## 5. Recursos Adicionais

- [Documentação do Photon Engine](https://doc.photonengine.com/) (Para entender o framework)
- [Repositório Original AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis)
- [Diretrizes de Contribuição do Albion Insight](CONTRIBUTING.md)

---
*Sua contribuição é vital para o sucesso do Albion Insight!*
