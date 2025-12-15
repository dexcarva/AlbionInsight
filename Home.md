# Albion Insight: Estatísticas Multiplataforma para Albion Online

O **Albion Insight** é uma ferramenta de análise de estatísticas em tempo real para o jogo Albion Online. Desenvolvido em **Python** e utilizando o framework **Flet**, ele oferece uma solução multiplataforma (Linux, Windows, macOS) para rastrear dados cruciais do jogo, como:

*   **Medidor de Dano (Damage Meter):** Acompanhe o dano e a cura em tempo real.
*   **Rastreamento de Sessão:** Monitore ganhos de Prata e Fama por sessão.
*   **Análise de Tráfego de Rede:** Utiliza a biblioteca Scapy para decodificar pacotes do protocolo Photon.

## Por que o Albion Insight?

Este projeto nasceu como um *port* do projeto original em C# (`AlbionOnline-StatisticsAnalysis`) para superar as limitações de plataforma (o original funcionava apenas no Windows). Nosso foco é a **compatibilidade**, a **facilidade de uso** e a **transparência** de ser um projeto de código aberto.

## Melhores Práticas de Contribuição e Qualidade

O projeto adota rigorosas **Melhores Práticas de Projetos GitHub** para garantir a qualidade e a sustentabilidade do código.

*   **Padrão de Commits:** Utilizamos o **Conventional Commits** para mensagens claras e automação de releases.
*   **Qualidade de Código:** Ferramentas como **Black**, **Flake8** e **mypy** são aplicadas via `pre-commit hooks` para manter um código limpo e tipado.
*   **Gestão de Issues:** Priorizamos a **resposta humanizada** e o **fechamento seguro** de issues, sempre buscando a confirmação do usuário para a solução.
*   **Integração Contínua (CI/CD):** Um pipeline de GitHub Actions garante que todos os Pull Requests passem por testes e verificações de linting antes do merge.

## Links Rápidos da Wiki

| Guia | Descrição |
| :--- | :--- |
| [[Guia de Instalação Segura no Linux]] | Instruções detalhadas para instalação, incluindo a configuração de segurança `setcap` no Linux. |
| [[Guia de Uso]] | Como utilizar o Damage Meter, rastrear estatísticas e gerenciar sessões. |
| [[Arquitetura Modular do Albion Insight]] | Arquitetura do projeto, fluxo de dados e detalhes sobre a decodificação do protocolo Photon. |
| [[Solução de Problemas (FAQ)]] | Respostas para perguntas frequentes e soluções para problemas comuns de permissão e rastreamento. |
| [[Guia de Contribuição Geral]] | Como contribuir com o projeto, incluindo o padrão de Conventional Commits. |
| [[Melhores Práticas de Projetos GitHub no Albion Insight]] | Documentação sobre o fluxo de trabalho de Issues e Pull Requests. |
| [[README.zu-ZA]] | Imibhalo ngolimi lwesiZulu (Zulu documentation). |

Para mais detalhes, consulte o arquivo [[Melhores Práticas de Projetos GitHub no Albion Insight]].

---
*O Albion Insight é um projeto de código aberto, feito pela comunidade para a comunidade.*
