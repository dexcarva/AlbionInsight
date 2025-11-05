# Guia de Uso do Albion Insight

Este guia explica como usar a interface do **Albion Insight** para rastrear e analisar suas estatísticas de jogo.

## Interface Principal

A interface do Albion Insight é dividida em três seções principais:

1.  **Controles de Sessão:** Para iniciar, parar e gerenciar a captura de dados.
2.  **Status e Duração:** Exibe o estado atual do rastreador e o tempo de sessão.
3.  **Medidor de Dano (Damage Meter):** A tabela principal que exibe as estatísticas de combate.

## 1. Controles de Sessão

| Elemento | Função |
| :--- | :--- |
| **Network Interface (Dropdown)** | Selecione a interface de rede que está sendo usada para se conectar ao Albion Online. **Importante:** Se você estiver usando VPN, selecione a interface da VPN. |
| **Start Sniffing** | Inicia a captura de pacotes de rede. O aplicativo começará a processar os dados em tempo real. |
| **Stop Sniffing** | Pausa a captura de pacotes. As estatísticas atuais permanecem na tela. |
| **Reset Session** | Limpa todas as estatísticas de dano, cura e duração da sessão. |
| **Save Session** | Salva as estatísticas atuais em um arquivo (geralmente um arquivo JSON ou CSV, dependendo da implementação futura) para análise posterior. |

## 2. Status e Duração

*   **Status:** Indica o estado atual do rastreador (Pronto, Sniffing, Parado, Erro).
*   **Duration:** Exibe o tempo decorrido desde o início da sessão de rastreamento no formato HH:MM:SS.

## 3. Medidor de Dano (Damage Meter)

A tabela exibe as estatísticas de combate para cada jogador (incluindo você) que o rastreador conseguiu identificar e processar eventos de combate.

| Coluna | Descrição |
| :--- | :--- |
| **Player** | O nome do jogador ou entidade que causou o dano/cura. |
| **Damage** | O total de dano causado por este jogador durante a sessão. |
| **DPS** | Dano por Segundo (Damage Per Second), calculado com base na duração da sessão. |
| **Healing** | O total de cura realizada por este jogador durante a sessão. |

### Como o DPS é Calculado

O DPS é calculado dividindo o **Dano Total** pelo **Tempo de Duração da Sessão** (em segundos).

$$
\text{DPS} = \frac{\text{Dano Total}}{\text{Duração da Sessão (segundos)}}
$$

**Nota:** Se a sessão estiver parada, o DPS exibido será o valor final da sessão. Se a sessão estiver em andamento, o valor é atualizado a cada segundo.

## Dicas de Uso

*   **Execução como Administrador/Root:** Lembre-se de que o aplicativo **deve** ser executado com privilégios elevados para funcionar corretamente.
*   **Seleção de Interface:** Se você tiver várias interfaces de rede (Wi-Fi, Ethernet, VPN), certifique-se de selecionar a correta no dropdown antes de iniciar o rastreamento.
*   **Decodificação Contínua:** O Albion Insight está em desenvolvimento. Se você notar que alguns eventos de combate não estão sendo rastreados, isso pode significar que o código de decodificação para aquele evento específico ainda não foi implementado. Considere [contribuir](Contribution-Guide) com a decodificação!
