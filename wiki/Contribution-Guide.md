# Guia de Contribuição para o Albion Insight

Agradecemos o seu interesse em contribuir para o Albion Insight! Sua ajuda é essencial para tornar esta ferramenta a melhor possível para a comunidade de Albion Online.

## Como Você Pode Ajudar

Existem várias maneiras de contribuir, mesmo que você não seja um programador experiente:

### 1. Relatar Bugs e Sugerir Funcionalidades

*   **Bugs:** Se encontrar um erro, por favor, abra uma [Issue no GitHub](https://github.com/dexcarva/AlbionInsight/issues). Inclua o máximo de detalhes possível: passos para reproduzir, sua versão do Python/OS e logs de erro.
*   **Funcionalidades:** Tem uma ideia para melhorar o Albion Insight? Abra uma [Issue de Sugestão de Funcionalidade](https://github.com/dexcarva/AlbionInsight/issues) e descreva o que você gostaria de ver e por que seria útil.

### 2. Contribuições de Código

Se você é um desenvolvedor, siga o nosso processo de Pull Request:

1.  **Fork** o repositório principal.
2.  **Clone** o seu fork localmente.
3.  Crie um novo branch para a sua funcionalidade ou correção (`git checkout -b feature/minha-nova-funcionalidade`).
4.  **Configure o ambiente de desenvolvimento** (veja o [Guia de Instalação](Installation-Guide)).
5.  Faça suas alterações, seguindo os padrões de código (PEP 8).
6.  **Teste** suas alterações.
7.  **Commit** suas mudanças com uma mensagem clara e descritiva (veja o `CONTRIBUTING.md` para o formato de commit).
8.  **Push** para o seu fork.
9.  Abra um **Pull Request** no repositório principal.

### 3. Documentação e Tradução

*   **Traduções:** O projeto valoriza a documentação em vários idiomas. Se você fala um idioma que ainda não está documentado (como o Alemão que acabamos de adicionar!), considere traduzir o `README.md` e o `CONTRIBUTING.md`.
*   **Wiki:** Ajude a manter a Wiki atualizada e clara. Se você notar que alguma informação está faltando ou confusa, sinta-se à vontade para sugerir edições.

### 4. Decodificação do Protocolo Photon

O maior desafio do projeto é a decodificação completa do protocolo Photon do Albion Online. Se você tem experiência em análise de pacotes ou engenharia reversa, sua ajuda é inestimável!

*   Consulte a página **[Detalhes Técnicos: Protocolo Photon](Technical-Details-Photon-Protocol)** para entender como funciona a decodificação.
*   Use ferramentas como o Wireshark para capturar pacotes e identificar novos códigos de eventos.
*   Compartilhe suas descobertas em uma Issue ou Pull Request.

## Padrões de Código

*   **Python:** Siga o **PEP 8** (4 espaços para indentação).
*   **Mensagens de Commit:** Use o formato **Conventional Commits** (ex: `feat: Adiciona funcionalidade X`, `fix: Corrige bug Y`).

**Obrigado por fazer parte da comunidade Albion Insight!**
