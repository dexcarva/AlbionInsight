# Albion Online Statistics Analysis - Versão Python/Flet

Este projeto é uma reimplementação do programa original **AlbionOnline-StatisticsAnalysis** (C#/WPF) em **Python** utilizando o framework **Flet** para garantir a compatibilidade multiplataforma (Linux, Windows e macOS).

A lógica central do programa foi adaptada para utilizar a biblioteca **Scapy** para a captura e análise de pacotes de rede, replicando a funcionalidade de rastreamento de estatísticas em tempo real.

## Funcionalidades Atuais

*   **Rastreamento de Rede:** Utiliza `Scapy` para capturar pacotes UDP nas portas do Albion Online (5055, 5056, 5058).
*   **Simulação de Estatísticas:** Simula a extração e o processamento de eventos (Silver, Fame, Kills, Deaths, Looted Chests) a partir dos pacotes, demonstrando a arquitetura para a lógica de decodificação real.
*   **Interface Gráfica (Flet):**
    *   Dashboard com estatísticas em tempo real (Silver, Fame, Kills, Deaths, Looted Chests).
    *   Cálculo de estatísticas por hora.
    *   Controles de Iniciar/Parar Rastreamento, Resetar Estatísticas e Salvar Sessão.
    *   Seleção de Interface de Rede.
    *   Log de Eventos.
*   **Compatibilidade:** A aplicação é totalmente funcional em ambientes Linux e pode ser executada em Windows e macOS com as dependências corretas.

## Requisitos

*   Python 3.8+
*   **Flet**
*   **Scapy**
*   **Privilégios de Administrador/Root:** Necessário para a captura de pacotes de rede.

## Como Executar

### 1. Instalação de Dependências

Certifique-se de ter o Python instalado. Em seguida, instale as bibliotecas necessárias:

```bash
pip3 install flet scapy
```

Em sistemas Linux, você também pode precisar instalar o `libpcap` ou `tcpdump` (dependendo da sua distribuição) para que o Scapy funcione corretamente.

### 2. Execução

A captura de pacotes requer permissões elevadas.

**No Linux:**

```bash
sudo python3 albion_stats_analysis_expanded.py
```

**No Windows (como Administrador):**

```bash
python albion_stats_analysis_expanded.py
```

A aplicação será iniciada em uma janela de desktop nativa.

## Estrutura do Código

O código está contido no arquivo `albion_stats_analysis_expanded.py` e segue uma arquitetura modular:

| Módulo | Descrição |
| :--- | :--- |
| `LiveStats` | Modelo de dados para armazenar as estatísticas em tempo real. |
| `NetworkTracker` | Lógica de rastreamento de rede (`Scapy`) e simulação de processamento de pacotes Photon. |
| `AlbionStatsApp` | A classe principal que gerencia a interface do usuário (Flet) e a interação com o `NetworkTracker`. |

## Próximos Passos (Desenvolvimento Futuro)

1.  **Decodificação Real de Pacotes Photon:** Substituir a lógica de simulação de `_simulate_stat_update` pela decodificação real dos pacotes do protocolo Photon para extrair dados precisos dos eventos do jogo.
2.  **Persistência de Dados:** Implementar o carregamento e salvamento de dados de forma mais robusta.
3.  **Implementação Completa da UI:** Adicionar as abas e funcionalidades restantes presentes no projeto original (Trade Monitoring, Gathering, Party, etc.).

---

**Nota:** Esta versão é um protótipo funcional que demonstra a viabilidade da migração para Python/Flet e a arquitetura para o rastreamento de rede. O código-fonte completo da reimplementação está disponível no arquivo `albion_stats_analysis_expanded.py`.

