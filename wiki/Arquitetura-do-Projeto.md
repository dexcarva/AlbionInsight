# Arquitetura do Projeto

O projeto Albion Insight segue um design modular para separar as preocupações de interface do usuário, lógica de rede e gerenciamento de dados.

### Estrutura de Módulos

| Arquivo | Responsabilidade | Detalhes |
| :--- | :--- | :--- |
| `albion_insight/main.py` | **Interface do Usuário (UI)** | Contém a lógica de inicialização do aplicativo Flet e a construção de todos os componentes visuais (botões, listas, medidores). Ele interage com o `NetworkTracker` para obter dados e atualizar a tela. |
| `albion_insight/core/network_tracker.py` | **Rastreamento de Rede e Protocolo** | Responsável por iniciar e parar o *sniffing* de pacotes (`scapy`), aplicar filtros BPF e decodificar o protocolo **Photon** usado pelo Albion Online. Ele traduz pacotes brutos em eventos de jogo (dano, cura, novos jogadores). |
| `albion_insight/core/models.py` | **Modelos de Dados** | Contém as classes de dados puras, como `PlayerStats` (estatísticas individuais de dano/cura) e `SessionStats` (gerenciamento de todas as estatísticas da sessão, duração, salvamento). Isso garante que a lógica de dados seja independente da UI e da rede. |

### Fluxo de Dados

1.  **`albion_insight/main.py`** (UI) chama `tracker.start_sniffing(interface)`.
2.  **`albion_insight/core/network_tracker.py`** inicia um *thread* de *sniffing* que captura pacotes UDP.
3.  Os pacotes são processados pelo `PhotonParser` para extrair eventos de jogo.
4.  Eventos de combate atualizam as instâncias de `PlayerStats` dentro de `SessionStats` (em `albion_insight/core/models.py`).
5.  O `network_tracker.py` chama o `update_callback` (que é `AlbionInsightApp.update_ui` em `albion_insight/main.py`).
6.  A UI (`albion_insight/main.py`) solicita os dados formatados de `tracker.get_damage_meter_data()` e atualiza a exibição.
