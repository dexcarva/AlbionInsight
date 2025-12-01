# GitHub Best Practices - Albion Insight

Este documento descreve as melhores práticas implementadas no repositório Albion Insight para garantir qualidade, organização e colaboração eficiente.

## 1. Estrutura do Repositório

### Organização de Diretórios

O projeto segue uma estrutura modular bem definida:

- **`albion_insight/`** - Código-fonte principal da aplicação
  - **`core/`** - Lógica central, rastreamento de rede e modelos de dados
  - **`ui/`** - Componentes de interface de usuário com Flet
  - **`utils/`** - Funções utilitárias, configuração e logging
  - **`__main__.py`** - Ponto de entrada da aplicação

- **`docs/`** - Documentação multilíngue (30+ idiomas)
- **`tests/`** - Testes automatizados
- **`.github/`** - Configurações do GitHub (templates, workflows, CODEOWNERS)

### Arquivos de Configuração

- **`pyproject.toml`** - Configuração do projeto, dependências e ferramentas
- **`requirements.txt`** - Dependências de produção
- **`requirements-dev.txt`** - Dependências de desenvolvimento
- **`.pre-commit-config.yaml`** - Hooks de pre-commit para qualidade de código
- **`mkdocs.yml`** - Configuração da documentação com suporte multilíngue

## 2. Controle de Versão

### Commits

O projeto segue a especificação **Conventional Commits** para mensagens claras e estruturadas:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Tipos de commit:**
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Mudanças na documentação
- `style:` Formatação de código
- `refactor:` Refatoração sem mudança de funcionalidade
- `perf:` Melhorias de performance
- `test:` Adição ou atualização de testes
- `chore:` Alterações de build, dependências ou ferramentas

**Exemplo:**
```
feat(damage-meter): Add export functionality for DPS reports

Implement CSV export feature for damage meter data,
allowing users to save combat statistics for analysis.

Closes #123
```

### Branches

- **`master`** - Branch principal (produção)
- **`feature/*`** - Branches para novas funcionalidades
- **`fix/*`** - Branches para correções de bugs
- **`docs/*`** - Branches para documentação

## 3. Issues

### Política de Issues

- **Resposta humanizada:** Todas as issues recebem resposta em português ou inglês, conforme a língua da pergunta
- **Confirmação de solução:** Issues não são fechadas sem confirmação do usuário de que a solução funcionou
- **Inatividade:** Issues sem resposta há mais de 7 dias recebem um lembrete
- **Descrição clara:** Títulos descritivos e informações detalhadas são obrigatórios

### Templates de Issues

O projeto utiliza templates para:
- **Bug Report** - Relatório de erros estruturado
- **Feature Request** - Solicitação de novas funcionalidades
- **Question** - Perguntas gerais

## 4. Pull Requests

### Processo de PR

1. Fork do repositório
2. Criar branch a partir de `master`
3. Fazer alterações seguindo os padrões de código
4. Executar testes e verificações de qualidade
5. Submeter PR com descrição detalhada
6. Aguardar revisão e feedback
7. Fazer ajustes conforme necessário
8. Merge após aprovação

### Checklist de PR

Antes de submeter, garantir:
- [ ] Código segue os padrões do projeto
- [ ] Auto-revisão completada
- [ ] Comentários adicionados a código complexo
- [ ] Documentação atualizada
- [ ] Sem novos warnings
- [ ] Testes adicionados e passando
- [ ] Mudanças dependentes mergeadas

## 5. Qualidade de Código

### Ferramentas de Linting

O projeto utiliza várias ferramentas para garantir qualidade:

- **Black** - Formatação automática de código
- **isort** - Ordenação automática de imports
- **Flake8** - Verificação de estilo PEP 8
- **mypy** - Verificação de tipos
- **pylint** - Análise estática de código
- **pytest** - Framework de testes com cobertura

### Pre-commit Hooks

Hooks automáticos executados antes de cada commit:
- Remoção de espaços em branco
- Correção de fim de arquivo
- Verificação de YAML
- Detecção de arquivos grandes
- Detecção de conflitos de merge
- Detecção de chaves privadas
- Formatação com Black e isort
- Verificação com Flake8 e mypy

### Padrões de Código

- **Indentação:** 4 espaços (sem tabs)
- **Comprimento de linha:** Máximo 100 caracteres
- **Nomes:** Significativos e descritivos
- **Docstrings:** Obrigatórias para funções e classes
- **Type hints:** Recomendados onde apropriado

## 6. Documentação

### Estrutura de Documentação

- **README.md** - Documentação principal em Inglês
- **README.pt-BR.md** - Documentação em Português (Brasil)
- **README.de-DE.md** - Documentação em Alemão
- **README.es-ES.md** - Documentação em Espanhol
- **README.fr-FR.md** - Documentação em Francês
- **README.fi.md** - Documentação em Finlandês

### Documentação Multilíngue

O projeto suporta 30+ idiomas através do MkDocs com plugin i18n:
- Documentação automática em múltiplos idiomas
- Seletor de idioma no site
- Contribuições de tradução bem-vindas

### Documentação Técnica

- **CONTRIBUTING.md** - Guia de contribuição
- **CODE_OF_CONDUCT.md** - Código de conduta
- **SECURITY.md** - Política de segurança
- **PACKAGING.md** - Guia de empacotamento
- **CHANGELOG.md** - Histórico de versões

## 7. Segurança

### Política de Segurança

- Vulnerabilidades devem ser reportadas por email (não em issues públicas)
- Resposta em até 48 horas
- Processo de avaliação e correção estruturado
- Divulgação pública após correção

### Proteção de Código

- Detecção de chaves privadas em pre-commit
- `.env.example` para variáveis de ambiente
- Arquivo `.gitignore` bem configurado

## 8. Testes

### Estrutura de Testes

- **Localização:** `tests/` directory
- **Framework:** pytest
- **Cobertura:** Monitorada com pytest-cov
- **Relatório:** HTML e terminal

### Execução de Testes

```bash
# Executar todos os testes
pytest

# Com cobertura
pytest --cov=albion_insight

# Gerar relatório HTML
pytest --cov=albion_insight --cov-report=html
```

## 9. CI/CD

### GitHub Actions

O projeto utiliza GitHub Actions para:
- Execução automática de testes
- Verificação de qualidade de código
- Validação de PRs
- Deploy automático de documentação

## 10. Comunidade

### Code of Conduct

- Ambiente acolhedor e inclusivo
- Respeito pela diversidade
- Tolerância zero para assédio ou discriminação
- Processo de denúncia claro

### Contribuição

- Contribuições de todos os níveis são bem-vindas
- Documentação clara para novos contribuidores
- Mentorado por maintainers experientes
- Reconhecimento de contribuidores

## 11. Versionamento

### Semantic Versioning

O projeto segue Semantic Versioning (MAJOR.MINOR.PATCH):
- **MAJOR:** Mudanças incompatíveis
- **MINOR:** Novas funcionalidades compatíveis
- **PATCH:** Correções de bugs

### Releases

- Tags Git para cada release
- Notas de release detalhadas
- Histórico em CHANGELOG.md

## 12. Checklist de Manutenção

Para manter o projeto saudável:

- [ ] Revisar issues regularmente
- [ ] Responder a PRs em tempo hábil
- [ ] Atualizar dependências
- [ ] Monitorar segurança
- [ ] Manter documentação atualizada
- [ ] Reconhecer contribuidores
- [ ] Planejar releases regularmente

---

**Última atualização:** 01/12/2025

Para mais informações, consulte o [CONTRIBUTING.md](CONTRIBUTING.md) ou abra uma issue com a label "question".
