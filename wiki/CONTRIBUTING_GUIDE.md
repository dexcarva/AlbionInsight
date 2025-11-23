# Guia de Contribuição para o Albion Insight

Este guia detalha como você pode contribuir para o projeto Albion Insight, seja reportando bugs, sugerindo novas funcionalidades, ou enviando código.

## Como Reportar um Bug

Se você encontrar um erro, por favor, siga estes passos:

1. **Verifique Issues Existentes:** Antes de abrir uma nova Issue, procure na lista de Issues abertas para ver se o problema já foi reportado.
2. **Use o Template de Bug:** Use o template de "Relatório de Bug" disponível no GitHub. Isso garante que você forneça todas as informações necessárias.
3. **Inclua Detalhes Essenciais:**
    - **Passos para Reproduzir:** Descreva exatamente como o erro pode ser replicado.
    - **Comportamento Esperado:** O que você esperava que acontecesse.
    - **Ambiente:** Seu Sistema Operacional, versão do Python e versão do Albion Insight.
    - **Logs e Capturas de Tela:** Se possível, anexe logs de erro e capturas de tela.

## Como Sugerir uma Funcionalidade

Novas ideias são sempre bem-vindas!

1. **Verifique Issues Existentes:** Verifique se a funcionalidade já foi sugerida.
2. **Use o Template de Feature:** Use o template de "Sugestão de Funcionalidade" para estruturar sua ideia.
3. **Descreva o Problema e a Solução:** Explique o problema que a nova funcionalidade resolveria e como você imagina a solução.

## Contribuindo com Código (Pull Requests)

Se você deseja contribuir com código, siga o fluxo de trabalho abaixo:

1. **Fork o Repositório:** Crie um fork do repositório .
2. **Crie um Branch:** Crie um branch com um nome descritivo (ex:  ou ).
3. **Instale as Dependências:** Certifique-se de ter todas as dependências instaladas ().
4. **Desenvolva e Teste:** Implemente suas mudanças e certifique-se de que todos os testes existentes passem. Adicione novos testes se for o caso.
5. **Execute o Linting e Type Checking:**
    ```bash
    flake8 albion_insight
    mypy albion_insight
    ```
6. **Use o Template de PR:** Ao abrir o Pull Request, preencha o template de PR para que a revisão seja mais rápida.
7. **Mantenha o Histórico Limpo:** Faça um "squash" dos seus commits em um único commit significativo antes de abrir o PR, se necessário.

## Diretrizes de Código

- **Estilo:** Siga o estilo de código Python (PEP 8).
- **Tipagem:** Use anotações de tipo sempre que possível (mypy).
- **Documentação:** Comente seu código e atualize a documentação relevante (READMEs, Wiki).

Agradecemos sua contribuição!
