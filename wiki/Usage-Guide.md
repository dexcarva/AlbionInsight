# Guia de Uso do Albion Insight

Este guia explica como usar as principais funcionalidades do Albion Insight, focando no Damage Meter e na gestão de sessões.

## 1. Iniciando a Captura de Pacotes

1.  **Selecione a Interface de Rede:** No menu suspenso **"Network Interface"**, escolha a interface de rede correta que o seu computador está usando para se conectar ao Albion Online.
2.  **Clique em "Start Sniffing":** A aplicação começará a monitorar o tráfego de rede nas portas do Albion Online (5055, 5056, 5058).
3.  **Verifique o Status:** O texto de status mudará para **"Status: Sniffing on [Interface]..."** e o cronômetro **"Duration"** começará a contar.

**Importante:** A aplicação deve ser executada com privilégios de administrador/root para que a captura de pacotes funcione.

## 2. O Damage Meter

O Damage Meter exibe estatísticas de combate em tempo real para todos os jogadores que interagem com o tráfego de rede capturado.

| Coluna | Descrição |
| :--- | :--- |
| **Player** | O nome do jogador. |
| **Damage** | O total de dano causado pelo jogador na sessão atual. |
| **DPS** | Dano por Segundo (Damage Per Second), calculado com base na duração da sessão. |
| **Healing** | O total de cura realizada pelo jogador na sessão atual. |

**Interpretação dos Dados:**

*   **DPS:** É uma métrica dinâmica. Se o cronômetro for reiniciado, o DPS será recalculado com base no novo tempo de sessão.
*   **Dados:** Os dados de Dano e Cura são acumulativos para a sessão.

## 3. Gestão de Sessões

O Albion Insight permite que você gerencie a sessão de rastreamento de dados.

### Parar a Captura

*   **Botão "Stop Sniffing":** Interrompe a captura de novos pacotes. O cronômetro para, e as estatísticas permanecem na tela. Você pode inspecionar os dados ou salvar a sessão.

### Reiniciar a Sessão

*   **Botão "Reset Session":** Limpa todos os dados de dano, cura e o cronômetro. O rastreamento **não** é reiniciado automaticamente; você deve clicar em "Start Sniffing" novamente, se desejar.

### Salvar a Sessão

*   **Botão "Save Session":** Salva as estatísticas atuais em um arquivo JSON no diretório do projeto.
    *   **Formato:** O arquivo JSON contém um snapshot dos dados do Damage Meter, incluindo o nome do jogador, dano, cura e a duração total da sessão.
    *   **Localização:** O arquivo será salvo com um nome baseado na data e hora (ex: `session_20251103_153000.json`).

## 4. Decodificação de Eventos

O Albion Insight decodifica eventos de rede para rastrear:

*   **Eventos de Combate:** Dano e Cura (parcialmente implementado, focado nos eventos principais).
*   **Eventos de Economia:** Atualizações de Prata (`UpdateMoney`).
*   **Eventos de Fama:** Atualizações de Fama (`UpdateFame`).
*   **Eventos de Morte:** Morte de jogadores (`Died`) e Abates (`KilledPlayer`).

Para mais detalhes sobre a decodificação do protocolo, consulte a página **[Detalhes Técnicos: Protocolo Photon](Technical-Details-Photon-Protocol)**.
