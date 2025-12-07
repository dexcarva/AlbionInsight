# Guia para Desenvolvedores

Agradecemos todas as contribuições! O Albion Insight é um projeto em constante evolução.

## 1. Configuração do Ambiente de Desenvolvimento

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```
2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt # Para ferramentas de qualidade de código
    ```
4.  **Execute os Testes:**
    ```bash
    pytest
    ```

## 2. Fluxo de Contribuição

1.  Crie um *fork* do repositório.
2.  Crie um *branch* para sua funcionalidade (`git checkout -b feature/minha-nova-feature`).
3.  Faça suas alterações e **certifique-se de que todos os testes passem**.
4.  Abra um **Pull Request** e preencha o template de PR.

*Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.*

[[Home]]
