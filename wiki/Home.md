# Albion Insight - Visão Geral do Projeto

<details>
<summary>Read this in other languages</summary>

**[Português (Brasil)](Home.pt-BR.md)** | **[English](Home.md)** | **[Ukrainian](Home.uk-UA.md)** | **[Korean](Home.ko-KR.md)**

</details>

O **Albion Insight** é uma ferramenta de análise de estatísticas de código aberto e multiplataforma, desenvolvida em **Python** com o framework **Flet**, dedicada à comunidade do jogo **Albion Online**. Seu propósito é rastrear e exibir estatísticas em tempo real, como dados de combate (Damage Meter), ganhos de prata e fama, através da análise do tráfego de rede do jogo.

Este projeto representa um esforço de modernização e portabilidade do projeto original em C# (`AlbionOnline-StatisticsAnalysis`), superando as limitações de plataforma e promovendo a colaboração da comunidade.

## 🎯 Objetivos Principais

1.  **Portabilidade:** Garantir o funcionamento nativo em Linux, Windows e macOS.
2.  **Transparência:** Ser uma alternativa de código aberto e auditável.
3.  **Funcionalidade:** Fornecer um Damage Meter preciso e um rastreador de estatísticas de sessão confiável.
4.  **Modularidade:** Manter uma estrutura de código limpa e modular para facilitar a manutenção e a contribuição.

## 🗺️ Mapa da Wiki

A Wiki do projeto é o seu guia completo para entender, usar e contribuir com o Albion Insight.

| Seção | Descrição | Status |
| :--- | :--- | :--- |
| **[Guia de Uso](Usage-Guide.md)** | Instruções passo a passo sobre como instalar, configurar e usar o aplicativo. | ✅ Completo |
| **[Guia de Instalação](Installation-Guide.md)** | Detalhes sobre os pré-requisitos e métodos de instalação para diferentes sistemas operacionais. | ✅ Completo |
| **[Visão Geral da Arquitetura](Architecture-Overview.md)** | Visão geral da estrutura de código, módulos e fluxo de dados. | ✅ Completo |
| **[Decodificação do Protocolo Photon](Photon-Protocol-Decoding.md)** | Explicação técnica sobre como o tráfego do Albion Online é decodificado. | ✅ Completo |
| **[Perguntas Frequentes (FAQ)](FAQ.md)** | Respostas para as dúvidas mais comuns da comunidade. | ✅ Completo |
| **[Guia de Contribuição](Contribution-Guide.md)** | Como configurar o ambiente de desenvolvimento, padrões de código e processo de Pull Request. | ✅ Completo |
| **[Solução de Problemas](Troubleshooting.pt-BR.md)** | Soluções para erros e problemas de configuração comuns. | ✅ Completo |
| **[Korean (한국어) Home](Home.ko-KR.md)** | Visão geral do projeto em Coreano. | ✅ Completo |
| **[Roadmap](Roadmap.md)** | Funcionalidades planejadas e o futuro do projeto. | ✅ Completo |

## 💖 Filosofia Open Source e Comunidade

O **Albion Insight** nasceu da crença de que as melhores ferramentas são aquelas construídas pela própria comunidade que as utiliza. Acreditamos no poder da colaboração para criar soluções transparentes, seguras e que atendam às necessidades reais dos jogadores de Albion Online.

Nossa filosofia se baseia em três pilares:

1.  **Transparência Total:** Todo o código-fonte é aberto e auditável. Queremos que você saiba exatamente como seus dados são processados, sem caixas-pretas ou surpresas.
2.  **Segurança em Primeiro Lugar:** Ao contrário de ferramentas de código fechado, a natureza aberta do Albion Insight permite que a comunidade revise e valide a segurança do código, garantindo que ele não realize ações maliciosas ou viole os termos de serviço do jogo.
3.  **Construído para a Comunidade, pela Comunidade:** O projeto evolui com base no feedback e nas contribuições dos usuários. Cada sugestão, relatório de bug ou pull request é valorizado e contribui para o futuro da ferramenta.

Ao usar e contribuir com o Albion Insight, você não está apenas obtendo uma ferramenta, mas fazendo parte de um movimento por um ecossistema de ferramentas mais aberto e seguro para a comunidade de Albion Online.

## 🤝 Como Contribuir

O Albion Insight prospera com a colaboração da comunidade. Sendo um projeto de código aberto, ele garante **transparência** no processamento de dados e permite que qualquer pessoa audite o código, garantindo a segurança e a integridade da ferramenta. Encorajamos ativamente a contribuição, seja através de relatórios de bugs, sugestões de funcionalidades ou código. Seu envolvimento é fundamental para o sucesso e a longevidade do projeto.

## 🌟 Melhores Práticas de Contribuição

Para garantir a qualidade e a consistência do projeto, pedimos que os contribuidores sigam estas diretrizes:

*   **Comunique-se:** Use as [Issues](https://github.com/dexcarva/AlbionInsight/issues) para discutir grandes mudanças antes de começar a codificar.
*   **Padrões de Código:** Siga o estilo de código Python definido por `black` e `isort`.
*   **Testes:** Inclua testes unitários para novas funcionalidades ou correções de bugs.
*   **Commits:** Use mensagens de commit claras e sem quebras de linha desnecessárias, seguindo o padrão **Conventional Commits** (ex: `feat: Adiciona nova funcionalidade` ou `fix: Corrige erro de importação`).

## 🛠️ Detalhes Técnicos

O Albion Insight é construído sobre as seguintes tecnologias:

*   **Linguagem:** Python 3.8+
*   **Interface Gráfica:** [Flet](https://flet.dev/) (para uma UI nativa e multiplataforma)
*   **Análise de Rede:** [Scapy](https://scapy.net/) (para captura e manipulação de pacotes)
*   **Protocolo:** Implementação de decodificação do protocolo **Photon** do Albion Online.

---
*Última atualização: 28 de Novembro de 2025*
