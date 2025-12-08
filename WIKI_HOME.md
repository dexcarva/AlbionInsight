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

Para outras plataformas ou instalação manual, consulte a seção [Instalação e Configuração](https://github.com/dexcarva/AlbionInsight#installation-and-setup) no \`README.md\` principal.

## 3. Solução de Problemas Comuns (FAQ)

| Problema | Solução Proposta | Status |
| :--- | :--- | :--- |
| **Tela Branca no Linux (LTS)** | Este problema geralmente está relacionado a incompatibilidades com a versão do Flet ou drivers gráficos. Tente atualizar o Flet para a versão mais recente ou execute a aplicação com a flag \`--web\` para usar a interface no navegador (se suportado). | Em Investigação/Aguardando Feedback |
| **"Permission Denied" ao executar** | A captura de pacotes de rede requer privilégios elevados. Certifique-se de estar executando o script com \`sudo\` (Linux/macOS) ou como Administrador (Windows). | Resolvido (Requisito) |
| **Não captura pacotes** | Verifique se o Albion Online está rodando e se o seu firewall não está bloqueando o tráfego nas portas 5055, 5056 e 5058. | Requer Diagnóstico |

## 4. Contribuição

O Albion Insight é um projeto comunitário. Sua ajuda é sempre bem-vinda!

*   **Reportar Bugs/Sugestões:** Use a seção [Issues](https://github.com/dexcarva/AlbionInsight/issues).
*   **Contribuir com Código:** Leia nosso [Guia de Contribuição](CONTRIBUTING.md) para começar.

---
*Esta Wiki é mantida pela comunidade. Sinta-se à vontade para expandir e melhorar esta documentação!*
