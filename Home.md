# Albion Insight Wiki - Página Principal

Bem-vindo à Wiki do **Albion Insight**, uma ferramenta de análise estatística multiplataforma para o jogo Albion Online. Este projeto é uma reimplementação moderna em **Python** e **Flet** do projeto original em C#, focando em compatibilidade e facilidade de uso.

## 1. Visão Geral do Projeto

O Albion Insight foi desenvolvido para fornecer aos jogadores de Albion Online uma visão em tempo real de suas estatísticas de jogo, como ganhos de silver, fame e, crucialmente, um **Damage Meter** (Medidor de Dano) para acompanhar o desempenho em combate.

A ferramenta opera analisando o tráfego de rede do jogo, decodificando o protocolo Photon para extrair dados relevantes de forma não intrusiva.

| Recurso | Descrição |
| :--- | :--- |
| **Multiplataforma** | Suporte nativo para **Linux**, **Windows** e **macOS**. |
| **Rastreamento em Tempo Real** | Utiliza a biblioteca `Scapy` para capturar e processar pacotes UDP nas portas do Albion Online (5055, 5056, 5058). |
| **Medidor de Dano** | Estrutura pronta para exibir estatísticas de combate ao vivo (Dano Causado, Cura Realizada, DPS). |
| **Interface Moderna** | Construído com o framework Flet, oferecendo uma experiência de desktop rápida e com aparência nativa. |
| **Gerenciamento de Sessão** | Funcionalidades para iniciar, parar, redefinir e salvar estatísticas de sessões de jogo. |

## 2. Instalação e Uso

A instalação requer **Python 3.8+** e as bibliotecas **Flet** e **Scapy**. A arquitetura do projeto foi refatorada para separar a captura de pacotes (que requer privilégios de administrador/root) da interface do usuário (UI), melhorando a segurança.

### 2.1. Pré-requisitos

*   Python 3.8+
*   Flet e Scapy (instalados via `pip`)
*   No Windows, pode ser necessário instalar o **Npcap** para o Scapy funcionar.

### 2.2. Instalação Rápida (Linux)

O repositório inclui scripts de automação para facilitar a instalação:

```bash
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight
./install.sh  # Instala dependências e cria ambiente virtual
./run.sh      # Executa a aplicação com privilégios de root
```

### 2.3. Execução Manual

Para executar a aplicação manualmente, use o seguinte comando (após instalar as dependências e dentro do ambiente virtual, se aplicável):

```bash
# No Linux (a UI não precisa de root, mas o sniffer será chamado com sudo)
python3 -m albion_insight

# No Windows (em Prompt de Comando/PowerShell como Administrador)
python -m albion_insight
```

A aplicação solicitará privilégios de administrador/root apenas para o processo de captura de pacotes, enquanto a interface do usuário será executada com privilégios normais.

## 3. Solução de Problemas Comuns (FAQ)

Para problemas comuns e suas soluções, consulte a página **[FAQ.md](FAQ.md)**.

| Problema Comum | Causa Potencial | Solução Sugerida |
| :--- | :--- | :--- |
| **"Permissão Negada"** ao executar | Falta de privilégios de root/administrador para o *sniffing* de pacotes. | A aplicação solicitará privilégios de administrador/root automaticamente. Se o problema persistir, verifique as configurações do `sudo`. |
| **O aplicativo não abre** (Erro de Importação) | Dependências ausentes ou versão incorreta do Python. | Verifique se o Python 3.8+ está instalado e se todas as dependências em `requirements.txt` foram instaladas corretamente. |
| **Não rastreia dados** | O jogo não está aberto ou o *sniffing* de pacotes está bloqueado pelo firewall. | Verifique se o Albion Online está rodando e se o firewall permite o tráfego nas portas 5055, 5056 e 5058. |

## 4. Tópicos Avançados e Contribuição

Para informações mais detalhadas sobre a arquitetura do projeto, decodificação do Protocolo Photon, roadmap de melhorias e diretrizes de contribuição de código, consulte as páginas:

*   **[Tópicos Avançados](WIKI_ADVANCED.md)**
*   **[Melhorias e Roadmap](IMPROVEMENTS.md)**
*   **[Guia de Contribuição](CONTRIBUTING.md)**

---
*Esta página foi consolidada e estruturada para servir como a página principal da Wiki do projeto Albion Insight.*
