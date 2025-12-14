# Início - Albion Insight Wiki

Bem-vindo à Wiki do **Albion Insight**, a ferramenta de análise de estatísticas multiplataforma para o MMORPG **Albion Online**.

O Albion Insight é um projeto de código aberto, reescrito em Python a partir do projeto original em C# (`AlbionOnline-StatisticsAnalysis`), com o objetivo de fornecer à comunidade uma ferramenta leve, moderna e compatível com Linux, Windows e macOS.

## 1. O que é Albion Insight?

É um sniffer de pacotes de rede que monitora o tráfego de dados entre o cliente do Albion Online e os servidores do jogo. Ele decodifica esses pacotes para extrair informações valiosas em tempo real, como:

*   **Estatísticas Financeiras:** Atualizações de Prata e Fama.
*   **Eventos de Combate:** Registro de Kills e Deaths.
*   **Medidor de Dano (Damage Meter):** Cálculo de DPS (Dano por Segundo) e HPS (Cura por Segundo) em tempo real.

## 2. Primeiros Passos

### Requisitos Mínimos

*   **Python 3.8+**
*   **Privilégios de Administrador/Root** (necessário para a captura de pacotes de rede).

### Instalação Rápida (Linux)

Para usuários de Linux, o método mais rápido é usar os scripts de instalação fornecidos:

1.  Clone o repositório:
    \`\`\`bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    \`\`\`
2.  Execute o script de instalação (ele cuidará das dependências do sistema e do Python):
    \`\`\`bash
    ./install.sh
    \`\`\`
3.  Execute a aplicação (será solicitada a senha de root/administrador):
    \`\`\`bash
    ./run.sh
    \`\`\`

Para outras plataformas ou instalação manual, consulte o [[Guia de Instalação Segura no Linux]] e a seção [Instalação e Configuração](https://github.com/dexcarva/AlbionInsight#installation-and-setup) no \`README.md\` principal.

## 3. Solução de Problemas Comuns (FAQ)

| Problema | Solução Proposta | Status |
| :--- | :--- | :--- |
| **Tela Branca no Linux (LTS)** | Este problema foi reportado na Issue #1 e a correção foi aplicada. Caso persista, verifique se a versão do Flet está atualizada. | **Resolvido** (Fechado por Inatividade) |
| **"Permission Denied" ao executar** | A captura de pacotes de rede requer privilégios elevados. **Recomendamos o uso do `setcap`** para permitir que o Python capture pacotes sem rodar como root. Consulte o [[Guia de Instalação Segura no Linux]]. | **Resolvido** (Requisito/Documentado) |
| **Não captura pacotes** | Verifique se o Albion Online está rodando e se o seu firewall não está bloqueando o tráfego nas portas 5055, 5056 e 5058. | Requer Diagnóstico |

## 4. Guias Técnicos e de Governança

Para uma compreensão mais aprofundada da estrutura do projeto e das políticas de gestão, consulte os seguintes guias:

*   **Arquitetura Modular:** Entenda a separação de responsabilidades entre os módulos Core, UI e Utils. Consulte o [[Arquitetura Modular do Albion Insight]].
*   **Decodificação do Protocolo Photon:** Detalhes técnicos sobre a captura de pacotes, OpCodes e extração de estatísticas. Consulte o [[Decodificação do Protocolo Photon no Albion Insight]].
*   **Qualidade de Código e Testes:** Entenda como garantimos a estabilidade e a qualidade do código, e como você pode contribuir com testes. Consulte o [[Guia de Testes e Qualidade de Código]].
*   **Segurança e Privacidade:** Entenda como o Albion Insight lida com a segurança da execução e a privacidade dos seus dados. Consulte o [[Guia de Segurança e Privacidade]].
*   **Governança e Melhores Práticas:** Detalhes sobre padrões de código, gestão de Issues e fluxo de Pull Requests. Consulte o [[Governança e Melhores Práticas do Projeto Albion Insight]].

## 5. Contribuição

O Albion Insight é um projeto comunitário. Sua ajuda é sempre bem-vinda!

*   **Reportar Bugs/Sugestões:** Use a seção [Issues](https://github.com/dexcarva/AlbionInsight/issues).
*   **Contribuir com Código:** Leia nosso [[Guia de Contribuição Geral]] para começar.

---
*Esta Wiki é mantida pela comunidade. Sinta-se à vontade para expandir e melhorar esta documentação!*
