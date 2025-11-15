# Conteúdo Sugerido para a Wiki do Albion Insight

## Home

**Albion Insight** é uma ferramenta de análise de estatísticas multiplataforma para o jogo Albion Online, reimplementada em **Python** usando o framework **Flet**. O projeto nasceu da necessidade de modernizar e tornar acessível à comunidade um projeto anterior, que estava limitado ao ambiente Windows.

### Contexto do Projeto

O **Albion Insight** é um *port* do projeto original **AlbionOnline-StatisticsAnalysis** (originalmente em C#/WPF), que se destacava por sua capacidade de rastrear dados de combate e economia analisando o tráfego de rede do jogo.

| Projeto | Linguagem/Framework | Plataformas | Foco |
| :--- | :--- | :--- | :--- |
| **AlbionOnline-StatisticsAnalysis** | C#/WPF | Windows | Funcionalidade, mas limitado a uma plataforma. |
| **Albion Insight** | Python/Flet | Linux, Windows, macOS | Modernização, portabilidade e modularidade. |
| **Documentação (ja-JP)** | Markdown | N/A | Suporte à comunidade japonesa. |

O objetivo principal do Albion Insight é fornecer uma alternativa **open-source** e **cross-platform** para que jogadores de todas as plataformas possam ter acesso a um Damage Meter e rastreador de estatísticas confiável.

### Páginas da Wiki

*   [Arquitetura do Projeto](#arquitetura-do-projeto)
*   [Guia de Contribuição](#guia-de-contribuição)\n*   [Melhores Práticas de Código](#melhores-práticas-de-código)
*   [Solução de Problemas Comuns](#solução-de-problemas-comuns)

---

## Arquitetura do Projeto

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

---

## Melhores Práticas de Código

Para garantir a qualidade e a manutenibilidade do projeto, pedimos que todos os colaboradores sigam as seguintes diretrizes:

1.  **Tipagem Estática (Type Hinting):** Todos os novos códigos e funções modificadas devem usar *type hints* do Python (PEP 484) para melhorar a legibilidade e permitir a verificação estática de tipos com ferramentas como `mypy`.
2.  **Padrão de Nomenclatura:**
    *   Variáveis e funções: `snake_case` (ex: `calculate_damage`).
    *   Classes: `PascalCase` (ex: `NetworkTracker`).
    *   Constantes: `UPPER_CASE_SNAKE_CASE` (ex: `MAX_PLAYERS`).
3.  **Docstrings:** Todas as funções e classes devem ter *docstrings* no formato **Google Style** para documentação clara e geração automática de documentação.
4.  **Testes Unitários:** Sempre que possível, inclua testes unitários para novas funcionalidades ou correções de bugs. Os testes devem ser colocados no diretório `tests/`.
5.  **Separação de Preocupações:** Mantenha a lógica de UI, rede e dados estritamente separada, conforme definido na seção **Arquitetura do Projeto**.

---

## Guia de Contribuição

Agradecemos todas as contribuições! Para garantir um processo de desenvolvimento suave, siga estas diretrizes.

### 1. Configuração do Ambiente

1.  **Fork** o repositório: `https://github.com/dexcarva/AlbionInsight`
2.  **Clone** seu fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Crie um **Virtual Environment** (Recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Desenvolvimento

*   **Separação de Preocupações:** Mantenha a lógica de dados em `core/models.py`, a lógica de rede em `core/network_tracker.py` e a UI em `main.py`.
*   **Testes:** Embora não haja testes automatizados no momento, teste suas alterações executando o aplicativo com privilégios de administrador/root.
*   **Decodificação Photon:** Se estiver trabalhando na decodificação de novos eventos, consulte a documentação do protocolo Photon e adicione a lógica de *parsing* em `core/network_tracker.py`.

### 3. Submissão de Código

1.  Crie uma nova *branch* para sua funcionalidade ou correção:
    ```bash
    git checkout -b feature/minha-nova-funcionalidade
    ```
2.  Faça *commit* de suas alterações com mensagens claras e descritivas.
3.  Envie para o seu fork:
    ```bash
    git push origin feature/minha-nova-funcionalidade
    ```
4.  Abra um **Pull Request** para a *branch* `main` do repositório principal.

---

## Solução de Problemas Comuns

| Problema | Causa Mais Comum | Solução |
| :--- | :--- | :--- |
| **"Permission denied" ou "No interfaces found"** | O rastreamento de rede (sniffing) requer privilégios elevados. | **Linux/macOS:** Execute o aplicativo com `sudo`. Ex: `sudo venv/bin/python3 albion_insight/main.py`. **Windows:** Execute o Prompt de Comando ou PowerShell como **Administrador**. |
| **O medidor de dano não atualiza** | O filtro BPF pode estar incorreto ou o Albion Online está usando portas diferentes. | Verifique se o filtro BPF em `core/network_tracker.py` (`udp and (port 5055 or port 5056 or port 5058)`) ainda é válido. Certifique-se de que o jogo está em execução. |
| **Erro de importação de módulo** | O ambiente virtual não está ativado ou as dependências não foram instaladas. | Ative o ambiente virtual (`source venv/bin/activate`) e execute `pip install -r requirements.txt`. |
| **O aplicativo não fecha corretamente** | O *thread* de *sniffing* não foi encerrado. | A função `on_close` em `albion_insight/main.py` agora garante que o `NetworkTracker` seja parado. Se o problema persistir, verifique se o processo `scapy` foi encerrado. |
| **Problemas de UI no Linux** | Dependências do Flet/GTK ausentes. | Certifique-se de que as dependências do sistema para Flet (como `libgtk-3-dev` ou equivalentes) estejam instaladas. |
