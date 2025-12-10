# Melhores Práticas de Projetos GitHub no Albion Insight

O projeto Albion Insight adota um conjunto de melhores práticas de desenvolvimento e gestão de projetos para garantir a qualidade do código, a colaboração eficiente e a sustentabilidade a longo prazo.

## 1. Qualidade de Código e Padrões

A consistência e a qualidade do código são mantidas através da automação e de padrões rigorosos.

| Prática | Ferramenta | Benefício |
| :--- | :--- | :--- |
| **Formatação Automática** | `Black` e `isort` | Garante um estilo de código unificado, eliminando discussões sobre formatação. |
| **Análise Estática (Linting)** | `Flake8` e `mypy` | Identifica erros de sintaxe, estilo e tipagem antes da execução, aumentando a robustez. |
| **Hooks de Pré-Commit** | `pre-commit` | Executa formatadores e linters automaticamente antes de cada commit, garantindo que apenas código limpo entre no histórico. |
| **Testes Automatizados** | `pytest` e `pytest-cov` | Garante que novas funcionalidades não quebrem as existentes e mede a cobertura de testes. |

## 2. Fluxo de Trabalho de Contribuição

Adotamos um fluxo de trabalho claro para facilitar a contribuição de novos desenvolvedores.

### 2.1. Mensagens de Commit (Conventional Commits)

Utilizamos a especificação **Conventional Commits** para categorizar e estruturar as mensagens de commit. Isso permite:
*   **Histórico Limpo:** Facilita a leitura do histórico do projeto.
*   **Geração Automática de Changelog:** Permite que ferramentas gerem automaticamente o `CHANGELOG.md`.
*   **Tipos Principais:** `feat` (nova funcionalidade), `fix` (correção de bug), `docs` (documentação), `refactor` (refatoração).

### 2.2. Gestão de Issues e Pull Requests

*   **Templates:** Utilizamos templates de Issues (Bug Report, Feature Request) e Pull Requests para garantir que todas as informações necessárias sejam fornecidas.
*   **Revisão de Código:** Todos os Pull Requests requerem revisão de código por um mantenedor.
*   **Fechamento de Issues:** Issues só são fechadas após a confirmação da solução pelo usuário (quando aplicável), garantindo uma **resposta humanizada** e a satisfação do usuário.

## 3. Documentação e Localização

*   **README Multi-idioma:** O projeto mantém múltiplos arquivos `README` (ex: `README.pt-BR.md`, `README.es-ES.md`) para atender à comunidade global de Albion Online.
*   **Wiki Detalhada:** A Wiki é usada para documentação mais aprofundada, como guias de instalação segura (`setcap` no Linux), arquitetura do projeto e guias de contribuição técnica (Decodificação do Protocolo Photon).

## 4. Segurança

*   **Instalação Segura no Linux:** O projeto utiliza o utilitário `setcap` para conceder ao binário do Python apenas as permissões de rede necessárias, evitando a execução como `sudo` e mitigando riscos de segurança.

Para mais detalhes sobre como contribuir, consulte o [[Guia de Contribuição Geral]].
