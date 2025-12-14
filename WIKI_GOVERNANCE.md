# Governança e Melhores Práticas do Projeto Albion Insight

Este guia detalha as políticas de governança e as melhores práticas adotadas pelo projeto Albion Insight para garantir a qualidade, a sustentabilidade e a colaboração eficaz da comunidade.

## 1. Padrões de Qualidade de Código

Adotamos ferramentas de qualidade de código para manter a consistência e reduzir erros:

| Ferramenta | Propósito | Execução |
| :--- | :--- | :--- |
| **Black** | Formatação de código Python (estilo não-configurável). | `pre-commit` hook |
| **isort** | Ordenação e organização de imports. | `pre-commit` hook |
| **Flake8** | Verificação de estilo e erros de sintaxe (linting). | `pre-commit` hook |
| **mypy** | Verificação de tipos estática (type checking). | `pre-commit` hook |

**Requisito:** Todo Pull Request deve passar por todas as verificações de `pre-commit` antes de ser considerado para merge.

## 2. Gestão de Issues e Suporte Comunitário

Nossa política de gestão de Issues visa um ambiente de suporte **humanizado** e **responsivo**.

### 2.1. Resposta Humanizada e Idiomas

*   **Regra de Ouro:** Responder na língua em que a Issue foi postada (Português, Inglês, Francês, etc.).
*   **Tom:** Manter um tom profissional, amigável e de agradecimento pela contribuição.

### 2.2. Fechamento de Issues

*   **Fechamento Seguro:** **NUNCA** fechar uma Issue de bug ou funcionalidade sem a **confirmação explícita do usuário** de que a solução proposta funcionou.
*   **Inatividade:** Issues sem resposta do usuário por mais de **7 dias** serão marcadas com o rótulo `inativo` e receberão uma notificação final. Se a inatividade persistir por mais de 30 dias, a Issue será fechada, mas com a nota de que pode ser reaberta a qualquer momento.

### 2.3. Rótulos (Labels) Essenciais

| Rótulo | Descrição | Uso |
| :--- | :--- | :--- |
| `bug` | Algo que não está funcionando como esperado. | Issues de erro |
| `enhancement` | Nova funcionalidade ou solicitação de melhoria. | Issues de sugestão |
| `awaiting-user-feedback` | Aguardando a confirmação do usuário sobre uma solução proposta. | Issues em fase de teste |
| `inativo` | Issue sem atividade do usuário por mais de 7 dias. | Issues que serão fechadas por inatividade |
| `docs` | Relacionado à documentação. | Issues de documentação |

## 3. Fluxo de Pull Requests (PRs)

### 3.1. Padrão de Commit

Utilizamos o **Conventional Commits** para garantir um histórico de commits limpo e para permitir a geração automática de `CHANGELOG.md`.

*   **Formato:** `<tipo>(<escopo opcional>): <descrição>`
*   **Exemplos de Tipos:** `feat`, `fix`, `docs`, `refactor`, `style`, `test`, `build`, `ci`, `chore`.

### 3.2. Revisão e Merge

*   **Revisão:** Todo PR deve ser revisado por pelo menos um mantenedor.
*   **Aprovação:** PRs que adicionam novas funcionalidades ou corrigem bugs críticos devem ser testados e aprovados.
*   **Sugestões:** Se um PR não se encaixa nos padrões, o mantenedor deve fornecer sugestões claras de como o contribuidor pode ajustá-lo.

## 4. Estrutura da Wiki

A Wiki é o ponto central para documentação aprofundada.

*   **Conteúdo:** Deve conter guias detalhados de instalação, uso, arquitetura e governança.
*   **Manutenção:** O conteúdo da Wiki deve ser mantido em arquivos Markdown no repositório (`WIKI_*.md`) para facilitar a contribuição via Pull Request.

---
*Este documento é um guia vivo e pode ser atualizado para refletir as necessidades do projeto.*
