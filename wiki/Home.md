# Albion Insight - Visão Geral do Projeto

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
| **[Roadmap](Roadmap.md)** | Funcionalidades planejadas e o futuro do projeto. | ✅ Completo |

## 🤝 Comunidade e Código Aberto

O Albion Insight prospera com a colaboração da comunidade. Sendo um projeto de código aberto, ele garante **transparência** no processamento de dados e permite que qualquer pessoa audite o código, garantindo a segurança e a integridade da ferramenta. Encorajamos ativamente a contribuição, seja através de relatórios de bugs, sugestões de funcionalidades ou código. Seu envolvimento é fundamental para o sucesso e a longevidade do projeto.

## 🛠️ Detalhes Técnicos

O Albion Insight é construído sobre as seguintes tecnologias:

*   **Linguagem:** Python 3.8+
*   **Interface Gráfica:** [Flet](https://flet.dev/) (para uma UI nativa e multiplataforma)
*   **Análise de Rede:** [Scapy](https://scapy.net/) (para captura e manipulação de pacotes)
*   **Protocolo:** Implementação de decodificação do protocolo **Photon** do Albion Online.

---
*Última atualização: 21 de Novembro de 2025*
