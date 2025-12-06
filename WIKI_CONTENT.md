# Conteúdo Proposto para a Wiki do Albion Insight

Este documento contém a estrutura e o conteúdo sugerido para a Wiki do projeto Albion Insight. O objetivo é fornecer uma documentação clara e abrangente para usuários e colaboradores.

## 1. Home (Página Principal)

**Título:** Albion Insight: Estatísticas Multiplataforma para Albion Online

**Conteúdo:**

O **Albion Insight** é uma ferramenta de análise de estatísticas em tempo real para o jogo Albion Online. Desenvolvido em **Python** e utilizando o framework **Flet**, ele oferece uma solução multiplataforma (Linux, Windows, macOS) para rastrear dados cruciais do jogo, como:

*   **Medidor de Dano (Damage Meter):** Acompanhe o dano e a cura em tempo real.
*   **Rastreamento de Sessão:** Monitore ganhos de Prata e Fama por sessão.
*   **Análise de Tráfego de Rede:** Utiliza a biblioteca Scapy para decodificar pacotes do protocolo Photon.

**Por que o Albion Insight?**

Este projeto nasceu como um *port* do projeto original em C# (`AlbionOnline-StatisticsAnalysis`) para superar as limitações de plataforma (o original funcionava apenas no Windows). Nosso foco é a **compatibilidade**, a **facilidade de uso** e a **transparência** de ser um projeto de código aberto.

**Links Rápidos:**
*   [Guia de Instalação](#2-guia-de-instalação)
*   [Guia de Uso](#3-guia-de-uso)
*   [Solução de Problemas (FAQ)](#4-solução-de-problemas-faq)
*   [Como Contribuir](#5-como-contribuir)

---

## 2. Guia de Instalação

**Título:** Instalação e Configuração

**Conteúdo:**

A instalação do Albion Insight requer o Python 3.8+ e privilégios de administrador/root para a captura de pacotes de rede.

### 2.1. Linux (Recomendado)

Recomendamos o uso dos scripts de instalação para uma configuração mais rápida:

1.  **Clone o Repositório:**
    \`\`\`bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    \`\`\`
2.  **Execute a Instalação:**
    \`\`\`bash
    ./install.sh
    \`\`\`
    *Este script instalará as dependências do sistema (`libpcap-dev`) e criará um ambiente virtual.*
3.  **Execute o Aplicativo:**
    \`\`\`bash
    ./run.sh
    \`\`\`
    *O script `run.sh` solicitará automaticamente a senha de root/sudo para iniciar a captura de pacotes.*

### 2.2. Windows

1.  **Instale o Python:** Baixe e instale o Python 3.8+ em [python.org](https://www.python.org/downloads/).
2.  **Instale as Dependências:**
    \`\`\`powershell
    pip install flet scapy
    \`\`\`
3.  **Execute como Administrador:** Abra o Prompt de Comando ou PowerShell **como Administrador** e execute:
    \`\`\`powershell
    python -m albion_insight
    \`\`\`

### 2.3. macOS

*Instruções de instalação para macOS serão adicionadas em breve. Atualmente, a instalação manual via `pip` e a execução com `sudo` são necessárias.*

---

## 3. Guia de Uso

**Título:** Primeiros Passos com o Albion Insight

**Conteúdo:**

### 3.1. Captura de Pacotes

O Albion Insight começa a rastrear o tráfego de rede assim que é iniciado com privilégios elevados.

*   **Verificação:** Se a captura estiver funcionando, você verá o status de conexão como **"Conectado"** ou **"Rastreando"** na interface.
*   **Portas:** O rastreamento é focado nas portas 5055, 5056 e 5058, usadas pelo Albion Online.

### 3.2. Medidor de Dano (Damage Meter)

A aba "Damage Meter" exibe estatísticas de combate em tempo real.

| Métrica | Descrição |
| :--- | :--- |
| **Dano Total** | O dano total causado por você e seu grupo. |
| **Cura Total** | A cura total realizada por você e seu grupo. |
| **DPS (Dano por Segundo)** | A taxa de dano causada no período de tempo da sessão. |
| **Eventos** | Lista de eventos de combate decodificados (em desenvolvimento). |

**Controles de Sessão:**
*   **Iniciar/Parar:** Pausa ou retoma o rastreamento.
*   **Resetar:** Limpa todos os dados da sessão atual.
*   **Salvar:** Exporta os dados da sessão para um arquivo (formato em desenvolvimento).

---

## 4. Solução de Problemas (FAQ)

**Título:** Perguntas Frequentes e Solução de Problemas

**Conteúdo:**

| Pergunta | Resposta |
| :--- | :--- |
| **Por que preciso de privilégios de root/administrador?** | A biblioteca `Scapy` precisa de acesso de baixo nível à interface de rede para "farejar" (sniff) os pacotes de dados do jogo. Isso é uma exigência de segurança do sistema operacional. |
| **O Albion Insight é seguro? Posso ser banido?** | O Albion Insight **apenas monitora** o tráfego de rede. Ele não injeta código, não modifica o cliente do jogo e não automatiza ações. O projeto original (C#) e este *port* são considerados seguros e permitidos pela Sandbox Interactive (desenvolvedora do Albion Online). |
| **Estou no Linux e vejo uma tela branca.** | Este é um problema conhecido em algumas distribuições LTS. Certifique-se de estar usando a versão mais recente do Albion Insight, pois uma correção foi aplicada recentemente. Se o problema persistir, abra uma [Issue no GitHub](https://github.com/dexcarva/AlbionInsight/issues). |
| **Posso usar com VPN ou ExitLag?** | Sim, mas a configuração pode ser mais complexa. Você precisará garantir que o `Scapy` esteja rastreando a interface de rede correta que está sendo usada pela VPN. |

---

## 5. Como Contribuir

**Título:** Guia para Desenvolvedores

**Conteúdo:**

Agradecemos todas as contribuições! O Albion Insight é um projeto em constante evolução.

### 5.1. Configuração do Ambiente de Desenvolvimento

1.  **Clone o Repositório:**
    \`\`\`bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    \`\`\`
2.  **Crie e Ative o Ambiente Virtual:**
    \`\`\`bash
    python3 -m venv venv
    source venv/bin/activate
    \`\`\`
3.  **Instale as Dependências:**
    \`\`\`bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt # Para ferramentas de qualidade de código
    \`\`\`
4.  **Execute os Testes:**
    \`\`\`bash
    pytest
    \`\`\`

### 5.2. Fluxo de Contribuição

1.  Crie um *fork* do repositório.
2.  Crie um *branch* para sua funcionalidade (`git checkout -b feature/minha-nova-feature`).
3.  Faça suas alterações e **certifique-se de que todos os testes passem**.
4.  Abra um **Pull Request** e preencha o template de PR.

*Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.*
