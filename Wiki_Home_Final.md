# Página Principal da Wiki - Albion Insight

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

Para outras plataformas ou instalação manual, consulte o **Guia de Instalação** e a seção [Instalação e Configuração](https://github.com/dexcarva/AlbionInsight#installation-and-setup) no \`README.md\` principal.

## 3. Documentação Multilíngue

A documentação principal está disponível em diversas línguas. Por favor, selecione a sua:

| Idioma | Arquivo README |
| :--- | :--- |
| Português (Brasil) | [README.pt-BR.md](README.pt-BR.md) |
| Inglês | [README.md](README.md) |
| Malaio | [README.ms-MY.md](README.ms-MY.md) |
| *e muitos outros...* | *Verifique a lista completa no repositório.* |

## 4. Solução de Problemas Comuns (FAQ)

| Problema | Solução Proposta | Status |
| :--- | :--- | :--- |
| **Tela branca no Linux LTS** | Atualizar a versão do Flet e dependências. | **Aguardando Confirmação** (Issue #1) |
| *Adicionar mais FAQs aqui...* | | |

## 5. Contribuição

Seu apoio é fundamental! Consulte o [Guia de Contribuição Geral](CONTRIBUTING.md) para saber como você pode ajudar.

*   **Reportar Bugs:** Use a seção [Issues](https://github.com/dexcarva/AlbionInsight/issues).
*   **Sugerir Recursos:** Use a seção [Issues](https://github.com/dexcarva/AlbionInsight/issues).
*   **Desenvolvimento:** Consulte o [Guia para Desenvolvedores](Guia%20para%20Desenvolvedores.md).

---
*Esta página é um rascunho para o conteúdo final da Wiki. O conteúdo será transferido para a Wiki do GitHub após o commit.*
