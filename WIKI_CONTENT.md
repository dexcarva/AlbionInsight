# Wiki do Albion Insight

Bem-vindo à Wiki do projeto Albion Insight! Este é o seu guia para entender, instalar, usar e contribuir para o projeto.

## 1. O que é o Albion Insight?

O Albion Insight é uma ferramenta de análise de estatísticas multiplataforma (Linux, Windows, macOS) para o jogo Albion Online. Ele foi reimplementado em **Python** e utiliza o framework **Flet** para fornecer uma interface de usuário moderna e nativa.

**Funcionalidade Principal:**
*   Rastreamento em tempo real de estatísticas do jogo (prata, fama, combate).
*   Análise de tráfego de rede usando a biblioteca `Scapy`.
*   Medidor de Dano (Damage Meter) com cálculo de DPS.

## 2. Guia de Instalação

Para instruções detalhadas de instalação, consulte o [README.md](README.md) principal.

**Requisitos:**
*   Python 3.8+
*   Privilégios de `root` ou `Administrador` para a captura de pacotes de rede.

## 3. Arquitetura do Projeto

O projeto adota uma arquitetura modular para facilitar a manutenção e o desenvolvimento.

| Módulo | Responsabilidade Principal | Tecnologias Chave |
| :--- | :--- | :--- |
| `albion_insight/core/` | Lógica de negócio, análise de rede, modelos de dados. | Python, Scapy, Pydantic |
| `albion_insight/ui/` | Apresentação de dados, interação com o usuário. | Python, Flet |
| `albion_insight/utils/` | Funções de suporte, logging, configuração. | Python |

## 4. Contribuição

Sua contribuição é muito bem-vinda!

**Como Contribuir:**
1.  **Fork** o repositório.
2.  Crie um *branch* para sua funcionalidade ou correção.
3.  Faça suas alterações e **commit**.
4.  Abra um **Pull Request** e preencha o template de PR.

*Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.*

## 5. Perguntas Frequentes (FAQ)

*   **O Albion Insight é permitido no jogo?**
    Sim. Ele apenas monitora o tráfego de rede e não interage com o cliente do jogo. É uma ferramenta passiva de análise.
*   **Por que preciso de privilégios de root/administrador?**
    A captura de pacotes de rede (sniffing) é uma operação de baixo nível que requer permissões elevadas no sistema operacional para funcionar corretamente.
*   **Posso usá-lo no Mac/Linux?**
    Sim! O Albion Insight foi portado para Python e Flet justamente para ser multiplataforma, suportando Linux, Windows e macOS.
