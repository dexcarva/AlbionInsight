# Guia de Contribuição Geral

Este guia visa fornecer um ponto de partida claro para qualquer pessoa interessada em contribuir para o projeto **Albion Insight**. Agradecemos seu interesse em ajudar a melhorar esta ferramenta para a comunidade de Albion Online!

## 1. Como Posso Contribuir?

Existem muitas maneiras de contribuir, mesmo que você não seja um desenvolvedor Python:

| Área de Contribuição | Descrição | Habilidades Chave |
| :--- | :--- | :--- |
| **Relatório de Bugs** | Identificar e relatar problemas de forma clara e reproduzível. | Observação, Comunicação |
| **Documentação** | Melhorar os arquivos README, a Wiki e a documentação do código. | Escrita Técnica, Fluência em Idiomas |
| **Tradução** | Traduzir a documentação e o site para novos idiomas. | Fluência em Idiomas |
| **Desenvolvimento de Código** | Implementar novos recursos, corrigir bugs e refatorar o código. | Python, Flet, Scapy |
| **Decodificação de Protocolo** | Ajudar a mapear novos eventos do jogo no Protocolo Photon. | Análise de Rede, Engenharia Reversa |

## 2. Antes de Começar

1.  **Leia o Código de Conduta:** Certifique-se de que suas interações estejam alinhadas com nosso [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
2.  **Verifique as Issues:** Antes de relatar um bug ou sugerir um recurso, verifique se já existe uma [Issue aberta](https://github.com/dexcarva/AlbionInsight/issues) sobre o assunto.
3.  **Use o Fluxo de Trabalho do Git:** Siga o fluxo de trabalho padrão de *fork*, *clone*, criação de *branch* e *Pull Request*.

## 3. Fluxo de Trabalho para Contribuições de Código

Para garantir a qualidade e a integração suave do código, siga estes passos:

1.  **Fork e Clone:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
    cd AlbionInsight
    ```
2.  **Crie uma Branch:**
    ```bash
    git checkout -b feature/nome-da-sua-feature
    # ou
    git checkout -b fix/correcao-do-bug
    ```
3.  **Instale as Dependências de Desenvolvimento:**
    ```bash
    # Instale as dependências listadas em [project.optional-dependencies] no pyproject.toml
    pip install -e .[dev]
    ```
4.  **Faça Suas Alterações:**
    *   Mantenha suas alterações focadas em um único problema ou recurso.
    *   Siga as convenções de estilo de código (o projeto usa **Black** e **isort**).
5.  **Execute os Testes e Linters:**
    ```bash
    # Execute os testes unitários
    pytest
    # Execute o linter e o formatador (se não estiver usando pre-commit)
    black .
    isort .
    flake8 albion_insight
    ```
6.  **Commit:** Use mensagens de commit claras e descritivas.
    *   **Exemplo:** `feat: Adiciona suporte para novo evento de combate X`
    *   **Exemplo:** `fix: Corrige erro de tela branca no Linux`
7.  **Push e Pull Request (PR):**
    ```bash
    git push origin feature/nome-da-sua-feature
    ```
    Abra um Pull Request no repositório principal.

## 4. Documentação Específica

Para contribuições em áreas mais técnicas, consulte os guias específicos na Wiki:

*   **[Decodificação do Protocolo Photon](WIKI_CONTENT_PROTOCOL_DECODING.md):** Para quem deseja mapear novos eventos do jogo.
*   **[Arquitetura Modular](WIKI_CONTENT_ARCHITECTURE.md):** Para entender a estrutura do código.
*   **[Guia de Instalação Segura](WIKI_CONTENT_INSTALLATION_GUIDE.md):** Para informações sobre a instalação e segurança no Linux.

Seu Pull Request será revisado o mais rápido possível. Obrigado por contribuir!
