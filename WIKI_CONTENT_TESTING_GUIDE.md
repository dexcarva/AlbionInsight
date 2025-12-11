# Guia de Testes e Qualidade de Código

A qualidade e a estabilidade do Albion Insight são garantidas por uma suíte robusta de testes automatizados e ferramentas de análise estática. Este guia detalha como executar os testes e como garantir que seu código atenda aos padrões de qualidade do projeto.

## 1. Ferramentas de Qualidade de Código

O projeto utiliza as seguintes ferramentas, que são executadas automaticamente via `pre-commit` e nos pipelines de Integração Contínua (CI):

| Ferramenta | Tipo | Propósito |
| :--- | :--- | :--- |
| **Black** | Formatador | Garante um estilo de código Python consistente (PEP 8). |
| **isort** | Formatador | Organiza automaticamente as importações. |
| **Flake8** | Linter | Verifica erros de sintaxe, complexidade e estilo. |
| **mypy** | Type Checker | Garante a correção de tipos estáticos, prevenindo bugs. |
| **pre-commit** | Hook Manager | Executa todas as ferramentas acima antes de cada commit. |

**Recomendação:** Sempre execute `pre-commit run --all-files` antes de abrir um Pull Request para garantir que seu código esteja limpo.

## 2. Testes Automatizados com `pytest`

Utilizamos o `pytest` como nosso framework de testes. Os testes estão localizados no diretório `tests/`.

### 2.1. Executando a Suíte de Testes

Para rodar todos os testes, certifique-se de que as dependências de desenvolvimento estejam instaladas (`pip install -e .[dev]`) e execute:

```bash
pytest
```

### 2.2. Verificando a Cobertura de Código

É crucial que novas funcionalidades e correções de bugs sejam acompanhadas por testes que garantam sua funcionalidade. Utilizamos o `pytest-cov` para medir a cobertura de código.

Para gerar um relatório de cobertura, execute:

```bash
pytest --cov=albion_insight --cov-report=term-missing
```

O objetivo é manter a cobertura de código em um nível alto, especialmente nas áreas críticas de decodificação de protocolo (`core/network_tracker.py`).

### 2.3. Tipos de Testes

| Tipo de Teste | Localização | Propósito |
| :--- | :--- | :--- |
| **Testes Unitários** | `tests/unit/` | Testam pequenas unidades de código (funções, classes) isoladamente. |
| **Testes de Integração** | `tests/integration/` | Testam a interação entre diferentes módulos (ex: `SnifferManager` e `NetworkTracker`). |
| **Testes de Decodificação** | `tests/decoding/` | Utilizam amostras de pacotes reais para garantir que a lógica de decodificação do Protocolo Photon esteja correta. |

## 3. Contribuições e Testes

Ao submeter um Pull Request:

1.  **Novas Funcionalidades:** Devem vir acompanhadas de testes unitários que demonstrem que a funcionalidade funciona conforme o esperado.
2.  **Correções de Bugs:** Devem incluir um teste que **falhe** antes da correção ser aplicada e **passe** após a correção, garantindo que o bug não retorne (regressão).

Agradecemos sua dedicação em manter o Albion Insight um projeto estável e de alta qualidade!
