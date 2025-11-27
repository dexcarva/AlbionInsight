# Albion Insight Wiki - Tópicos Avançados

Esta seção da Wiki é dedicada a usuários avançados, desenvolvedores e contribuidores que desejam se aprofundar na arquitetura e nos mecanismos internos do Albion Insight.

## 1. Arquitetura do Projeto

O Albion Insight segue uma arquitetura modular, separando a lógica de negócios (decodificação de pacotes) da interface do usuário (Flet).

| Componente | Descrição | Tecnologias Chave |
| :--- | :--- | :--- |
| **`albion_insight/core/`** | Contém a lógica central do aplicativo. É aqui que a decodificação do protocolo Photon e o gerenciamento de dados em tempo real ocorrem. | Python, Scapy, Protocolo Photon (Reverse-Engineered) |
| **`albion_insight/ui/`** | Responsável pela interface gráfica do usuário. Utiliza o framework Flet para criar uma aplicação desktop nativa e responsiva. | Python, Flet |
| **`albion_insight/utils/`** | Funções de utilidade, como configuração, logging e manipulação de arquivos. | Python, Logging |
| **`albion_insight/__main__.py`** | O ponto de entrada principal do aplicativo. Inicializa o *sniffing* de pacotes e a interface do usuário. | Python |

## 2. Decodificação do Protocolo Photon

O Albion Online utiliza o **Protocolo Photon** para comunicação entre o cliente e o servidor. O Albion Insight intercepta e decodifica esses pacotes para extrair dados do jogo.

### 2.1. Como Funciona o Sniffing

O aplicativo utiliza a biblioteca **Scapy** para monitorar o tráfego UDP nas portas específicas do Albion Online: **5055, 5056 e 5058**.

1.  **Filtro de Pacotes:** O Scapy é configurado para capturar apenas pacotes UDP de entrada e saída nessas portas.
2.  **Extração de Dados:** O payload do pacote UDP é extraído.
3.  **Decodificação Photon:** O payload é passado para a lógica de decodificação, que traduz os bytes brutos em eventos e dados estruturados do jogo (ex: `UpdateMoney`, `KilledPlayer`).

### 2.2. Estrutura de Dados de Combate

O Medidor de Dano (Damage Meter) é alimentado por eventos decodificados. Os dados são armazenados em estruturas otimizadas para cálculo em tempo real:

*   **`Combatant`:** Representa um jogador ou criatura, rastreando Dano Causado, Dano Recebido, Cura Realizada e DPS.
*   **`Session`:** Contém o estado atual da sessão de jogo, incluindo a lista de `Combatant` e estatísticas globais (prata, fama).

## 3. Diretrizes para Contribuição de Código

Para manter a qualidade e a manutenibilidade do projeto, os contribuidores devem seguir as seguintes diretrizes:

*   **Padrão de Código:** O código Python deve ser formatado usando **Black** e as importações organizadas com **isort**.
*   **Testes:** Novas funcionalidades ou correções de bugs devem ser acompanhadas de testes unitários relevantes na pasta `tests/`.
*   **Conventional Commits:** As mensagens de commit devem seguir o padrão [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), utilizando prefixos como `feat:`, `fix:`, `docs:`, `refactor:`, etc.
*   **Pull Requests:** Todo Pull Request deve ser aberto contra a branch `master` e incluir uma descrição clara das alterações e referências às Issues relacionadas.

## 4. Próximos Passos e Roadmap

O desenvolvimento do Albion Insight é contínuo. As prioridades atuais incluem:

*   **Decodificação Completa de Eventos de Combate:** Finalizar a tradução de todos os eventos de combate do protocolo Photon para uma precisão de Medidor de Dano de 100%.
*   **Persistência de Dados:** Implementar o salvamento e carregamento de sessões de estatísticas em um formato leve (ex: JSON ou SQLite).
*   **Configurações Avançadas de Sniffing:** Permitir que o usuário selecione a interface de rede (NIC) para o *sniffing* em ambientes com múltiplas conexões.
*   **Melhorias na UI:** Adicionar gráficos e visualizações de dados mais ricas usando o Flet.

Para acompanhar o progresso e sugerir novas funcionalidades, consulte a seção [Issues](https://github.com/dexcarva/AlbionInsight/issues) do repositório.
