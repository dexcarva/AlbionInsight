# Melhores Práticas de Código

Para garantir a qualidade e a manutenibilidade do projeto, pedimos que todos os colaboradores sigam as seguintes diretrizes:

1.  **Tipagem Estática (Type Hinting):** Todos os novos códigos e funções modificadas devem usar *type hints* do Python (PEP 484) para melhorar a legibilidade e permitir a verificação estática de tipos com ferramentas como `mypy`.
2.  **Padrão de Nomenclatura:**
    *   Variáveis e funções: `snake_case` (ex: `calculate_damage`).
    *   Classes: `PascalCase` (ex: `NetworkTracker`).
    *   Constantes: `UPPER_CASE_SNAKE_CASE` (ex: `MAX_PLAYERS`).
3.  **Docstrings:** Todas as funções e classes devem ter *docstrings* no formato **Google Style** para documentação clara e geração automática de documentação.
4.  **Testes Unitários:** Sempre que possível, inclua testes unitários para novas funcionalidades ou correções de bugs. Os testes devem ser colocados no diretório `tests/`.
5.  **Separação de Preocupações:** Mantenha a lógica de UI, rede e dados estritamente separada, conforme definido na seção **Arquitetura do Projeto**.

## Ferramentas de Qualidade de Código

O projeto utiliza as seguintes ferramentas para garantir a consistência e a qualidade do código. É obrigatório executar estas ferramentas antes de submeter um Pull Request:

| Ferramenta | Função | Comando de Execução |
| :--- | :--- | :--- |
| **Black** | Formatador de código Python (opinião forte) | `black albion_insight` |
| **isort** | Ordenador de imports | `isort albion_insight` |
| **Flake8** | Linter para verificar erros de estilo e sintaxe | `flake8 albion_insight` |
| **Mypy** | Verificador de tipos estático | `mypy albion_insight` |

## Padrão de Mensagem de Commit

Utilizamos o padrão **Conventional Commits** para manter um histórico de commits limpo e informativo.

**Formato:** `<tipo>(<escopo>): <descrição>`

| Tipo | Descrição | Exemplo |
| :--- | :--- | :--- |
| `feat` | Nova funcionalidade | `feat: Adicionar suporte para novo tipo de pacote` |
| `fix` | Correção de bug | `fix(network): Corrigir erro de decodificação de string` |
| `docs` | Alterações na documentação | `docs(readme): Atualizar seção de instalação` |
| `style` | Alterações de estilo (formatação, ponto e vírgula, etc.) | `style: Aplicar formatação black` |
| `refactor` | Refatoração de código sem mudança de funcionalidade | `refactor(core): Mover lógica de sessão para módulo dedicado` |
| `test` | Adição ou correção de testes | `test: Adicionar testes unitários para SessionStats` |
| `chore` | Tarefas de manutenção (build, dependências, etc.) | `chore(deps): Atualizar flet para 0.28.3` |
| `perf` | Melhoria de performance | `perf(network): Otimizar filtro BPF` |
| `ci` | Alterações nos arquivos de CI/CD | `ci: Adicionar workflow para testes automáticos` |

**Exemplo de Commit:**
```
feat(ui): Adicionar painel de estatísticas em tempo real

O novo painel utiliza o componente DamageMeter para exibir o DPS e a cura por segundo.
```

---
*Esta página foi atualizada como parte de um esforço de manutenção e aplicação de melhores práticas de projeto.*
