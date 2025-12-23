# Guia para Desenvolvedores

Este guia é destinado a desenvolvedores que desejam contribuir com o **Albion Insight**. Ele detalha a arquitetura do projeto, o fluxo de trabalho de desenvolvimento e, crucialmente, a lógica de decodificação do protocolo.

## 1. Arquitetura Modular

O projeto é estruturado em módulos claros para separar as responsabilidades:

| Módulo | Responsabilidade Principal |
| :--- | :--- |
| `albion_insight/core/` | Contém a lógica de negócios: `network_tracker`, `protocol_decoder`, `models` e `sniffer_manager`. |
| `albion_insight/ui/` | Contém a interface do usuário construída com **Flet**. |
| `albion_insight/utils/` | Funções utilitárias, como `logger` e `config`. |
| `albion_insight/__main__.py` | Ponto de entrada principal da aplicação. |

### Fluxo de Dados Simplificado

1.  **`main_logic.py`** inicia o **`SnifferManager`** e a **UI**.
2.  A **UI** (Interface do Usuário) envia um comando para o **`SnifferManager`** iniciar a captura.
3.  O **`SnifferManager`** inicia o **`sniffer_process.py`** como um subprocesso com `sudo` (para permissões de rede).
4.  O **`sniffer_process.py`** executa o **`network_tracker.py`**.
5.  O **`network_tracker.py`** usa **Scapy** para capturar pacotes e os envia para o **`ProtocolDecoder`**.
6.  O **`ProtocolDecoder`** atualiza o objeto **`SessionStats`** e envia dados de volta para o **`SnifferManager`** via `stdout` do subprocesso.
7.  O **`SnifferManager`** lê o `stdout` e armazena os dados em uma fila para a **UI** consumir.

## 2. Decodificação do Protocolo Photon

O Albion Online utiliza o framework de rede **Photon**. A parte mais crítica do projeto é a tradução da lógica de decodificação do C# (do projeto original) para o Python.

*   **Localização:** A lógica de decodificação reside em `albion_insight/core/protocol_decoder.py`.
*   **OpCodes:** O decodificador mapeia os OpCodes (códigos de operação) do Photon para métodos de tratamento específicos (ex: `_handle_update_money`).
*   **Melhoria Contínua:** A decodificação completa de todos os eventos de combate (como `CastHit`, `Attack`) é um esforço contínuo. Contribuições nesta área são extremamente valiosas.

## 3. Padrões de Código e Qualidade

O projeto segue rigorosos padrões de qualidade para garantir a manutenibilidade:

*   **Formatação:** Usamos **Black** para formatação de código e **isort** para ordenação de imports.
*   **Linting:** **Flake8** e **Pylint** são usados para identificar erros e problemas de estilo.
*   **Tipagem:** **mypy** é usado para tipagem estática, garantindo a robustez do código.

**Fluxo de Contribuição:**

1.  Faça um *fork* do repositório.
2.  Crie um *branch* para sua *feature* ou *fix*.
3.  Instale as dependências de desenvolvimento (`pip install -r requirements-dev.txt`).
4.  Use `pre-commit install` para configurar os *hooks* de qualidade.
5.  Faça suas alterações e garanta que os testes passem.
6.  Crie um **Pull Request** com uma mensagem de commit seguindo o padrão **Conventional Commits** (ex: `feat: Adiciona suporte a novos pacotes de dano`).

[[Home]]
