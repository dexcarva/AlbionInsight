# Guia de Contribuição

Agradecemos todas as contribuições! Para garantir um processo de desenvolvimento suave, siga estas diretrizes.

### 1. Configuração do Ambiente

1.  **Fork** o repositório: `https://github.com/dexcarva/AlbionInsight`
2.  **Clone** seu fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Crie um **Virtual Environment** (Recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Desenvolvimento

*   **Separação de Preocupações:** Mantenha a lógica de dados em `core/models.py`, a lógica de rede em `core/network_tracker.py` e a UI em `main.py`.
*   **Testes:** Embora não haja testes automatizados no momento, teste suas alterações executando o aplicativo com privilégios de administrador/root.
*   **Decodificação Photon:** Se estiver trabalhando na decodificação de novos eventos, consulte a documentação do protocolo Photon e adicione a lógica de *parsing* em `core/network_tracker.py`.

### 3. Submissão de Código

1.  Crie uma nova *branch* para sua funcionalidade ou correção:
    ```bash
    git checkout -b feature/minha-nova-funcionalidade
    ```
2.  Faça *commit* de suas alterações com mensagens claras e descritivas.
3.  Envie para o seu fork:
    ```bash
    git push origin feature/minha-nova-funcionalidade
    ```
4.  Abra um **Pull Request** para a *branch* `main` do repositório principal.
