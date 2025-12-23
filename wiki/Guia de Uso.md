# Primeiros Passos com o Albion Insight

## 1. Captura de Pacotes

O Albion Insight começa a rastrear o tráfego de rede assim que é iniciado com privilégios elevados.

*   **Verificação:** Se a captura estiver funcionando, você verá o status de conexão como **"Conectado"** ou **"Rastreando"** na interface.
*   **Portas:** O rastreamento é focado nas portas 5055, 5056 e 5058, usadas pelo Albion Online.

## 2. Medidor de Dano (Damage Meter)

A aba "Damage Meter" exibe estatísticas de combate em tempo real.

| Métrica | Descrição |
| :--- | :--- |
| **Dano Total** | O dano total causado por você e seu grupo. |
| **Cura Total** | A cura total realizada por você e seu grupo. |
| **DPS (Dano por Segundo)** | A taxa de dano causada no período de tempo da sessão. |
| **Eventos** | Lista de eventos de combate decodificados (em desenvolvimento). |

**Controles de Sessão:**

*   **Iniciar/Parar:** Pausa ou retoma o rastreamento.
*   **Resetar:** Limpa todos os dados da sessão atual.
*   **Salvar:** Exporta os dados da sessão para um arquivo (formato em desenvolvimento).

## 3. Status de Desenvolvimento e Feedback

O Albion Insight está em desenvolvimento ativo. A decodificação do protocolo Photon do Albion Online é um processo contínuo.

*   **O que funciona:** Rastreamento de pacotes, estatísticas básicas (Silver, Fame, Kills, Deaths) e a estrutura do Damage Meter.
*   **O que está em desenvolvimento:** A decodificação completa de **todos** os eventos de combate (como `CastHit`, `Attack`) para uma precisão total do Damage Meter.

**Seu Feedback é Vital:**

Se você encontrar um bug, um evento não decodificado ou tiver uma sugestão de melhoria, por favor, abra uma [Issue no GitHub](https://github.com/dexcarva/AlbionInsight/issues).

[[Home]]
