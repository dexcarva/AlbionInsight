# Guia de Contribuição Geral

Agradecemos o seu interesse em contribuir para o **Albion Insight**! Este guia detalha o processo de contribuição, desde a configuração do ambiente até o envio de um Pull Request.

## 1. Configuração do Ambiente

Siga os passos de instalação manual no [README.md](README.md) para configurar seu ambiente de desenvolvimento.

**Requisitos Adicionais para Contribuidores:**

Para garantir a qualidade do código, utilizamos `pre-commit hooks` que formatam e verificam o código automaticamente antes de cada commit.

\`\`\`bash
# Dentro do diretório AlbionInsight
pip install pre-commit
pre-commit install
\`\`\`

Isso instalará as ferramentas **Black** (formatação), **Flake8** (linting) e **mypy** (verificação de tipos) e as executará automaticamente.

## 2. Padrão de Commits

Adotamos o padrão **Conventional Commits** para manter um histórico de commits limpo e legível.

**Formato:** `<tipo>(<escopo opcional>): <descrição>`

| Tipo | Descrição |
| :--- | :--- |
| `feat` | Uma nova funcionalidade. |
| `fix` | Uma correção de bug. |
| `docs` | Alterações na documentação. |
| `style` | Alterações que não afetam o significado do código (espaços em branco, formatação, ponto e vírgula ausente, etc.). |
| `refactor` | Uma alteração de código que não corrige um bug nem adiciona um recurso. |
| `perf` | Uma alteração de código que melhora o desempenho. |
| `test` | Adição de testes ausentes ou correção de testes existentes. |
| `build` | Alterações que afetam o sistema de construção ou dependências externas (escopos: `deps`, `pyinstaller`). |
| `ci` | Alterações nos arquivos e scripts de configuração de CI (GitHub Actions). |
| `chore` | Outras alterações que não modificam arquivos de código-fonte ou de teste. |

**Exemplos:**

*   `feat: Adiciona suporte para o novo evento de combate 'CastHit'`
*   `fix(ui): Corrige o alinhamento do texto no Damage Meter`
*   `docs: Atualiza o guia de instalação para macOS`
*   `ci: Adiciona verificação de cobertura de código ao workflow`

## 3. Fluxo de Trabalho (Workflow)

1.  **Fork** o repositório.
2.  **Clone** seu fork.
3.  Crie uma nova *branch* para sua contribuição: `git checkout -b <tipo>/<nome-da-feature>`
4.  Faça suas alterações.
5.  Faça o **commit** usando o padrão Conventional Commits.
6.  Envie suas alterações para o seu fork: `git push origin <tipo>/<nome-da-feature>`
7.  Abra um **Pull Request** para a *branch* `master` do repositório principal.

## 4. Diretrizes para Pull Requests

*   Mantenha seus Pull Requests focados em uma única funcionalidade ou correção.
*   Certifique-se de que todos os testes passem e que as verificações de linting do CI estejam verdes.
*   Preencha o template do Pull Request com o máximo de detalhes possível.
*   Se o seu PR fechar uma Issue, use palavras-chave como `Closes #<número-da-issue>` na descrição do PR.
