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
