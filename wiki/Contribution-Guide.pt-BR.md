# Guia de Contribuição para o Albion Insight

Agradecemos o seu interesse em contribuir para o projeto Albion Insight! Seu apoio é fundamental para o sucesso e a longevidade desta ferramenta.

## Como Contribuir

Existem muitas maneiras de contribuir, mesmo que você não seja um desenvolvedor:

1.  **Reportar Bugs**: Use a seção [Issues](https://github.com/dexcarva/AlbionInsight/issues) para relatar problemas.
2.  **Sugerir Funcionalidades**: Abra uma Issue para sugerir novas ideias.
3.  **Melhorar a Documentação**: Ajude a traduzir ou melhorar a clareza dos nossos guias.
4.  **Escrever Código**: Contribua com correções de bugs ou novas funcionalidades.

## Configuração do Ambiente de Desenvolvimento

Para começar a codificar, siga estes passos:

1.  **Fork e Clone**:
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```
2.  **Ambiente Virtual**: Crie e ative um ambiente virtual para isolar as dependências.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate   # Windows
    ```
3.  **Instalar Dependências**: Instale as dependências de produção e desenvolvimento.
    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```
4.  **Executar a Aplicação**:
    ```bash
    # Lembre-se que a captura de pacotes requer privilégios elevados!
    sudo python3 albion_insight/main.py
    ```

## Padrões de Código e Qualidade

Para garantir a consistência do código, usamos as seguintes ferramentas:

*   **Black**: Para formatação automática de código.
*   **Flake8**: Para linting (verificação de estilo e erros).
*   **Mypy**: Para verificação de tipos estática.

**Antes de fazer o commit**, execute:
```bash
black .
flake8 .
mypy .
```

## Processo de Pull Request (PR)

1.  **Crie uma Branch**:
    ```bash
    git checkout -b feature/minha-nova-funcionalidade
    ```
2.  **Faça suas Alterações**: Implemente sua funcionalidade ou correção.
3.  **Commit**: Use mensagens de commit claras e descritivas (preferencialmente seguindo o padrão [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)).
    *   Exemplo: `fix: Corrigir erro de permissão no Linux`
    *   Exemplo: `feat: Adicionar suporte para novo evento Photon`
4.  **Abra o PR**: Envie suas alterações para o seu fork e abra um Pull Request para a branch `main` do repositório principal.

**O que esperar após o PR:**
*   Seu código será revisado por um mantenedor.
*   Poderemos solicitar alterações ou esclarecimentos.
*   Assim que aprovado, seu código será mesclado.

## Decodificação do Protocolo Photon

A parte mais complexa do projeto é a decodificação do protocolo Photon. Se você estiver trabalhando nesta área:

*   Consulte a documentação existente em [Photon Protocol Decoding](Photon-Protocol-Decoding.md).
*   Use ferramentas de análise de rede (como Wireshark) para capturar e analisar novos pacotes.
*   Adicione novos manipuladores de eventos em `albion_insight/core/network_tracker.py` (ou um módulo dedicado) para processar os dados.

---

*Última atualização: Novembro de 2025*
