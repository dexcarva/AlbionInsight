# Albion Insight Wiki - Página Principal

Bem-vindo à Wiki do **Albion Insight**, uma ferramenta de análise estatística multiplataforma para o jogo Albion Online. Este projeto é uma reimplementação moderna em **Python** e **Flet** do projeto original em C#, focando em compatibilidade e facilidade de uso.

## 🚀 Visão Geral do Projeto

O Albion Insight foi desenvolvido para fornecer aos jogadores de Albion Online uma visão em tempo real de suas estatísticas de jogo, como ganhos de silver, fame e, crucialmente, um **Damage Meter** (Medidor de Dano) para acompanhar o desempenho em combate.

A ferramenta opera analisando o tráfego de rede do jogo, decodificando o protocolo Photon para extrair dados relevantes de forma não intrusiva.

## ✨ Principais Recursos

| Recurso | Descrição |
| :--- | :--- |
| **Multiplataforma** | Suporte nativo para **Linux**, **Windows** e **macOS**. |
| **Rastreamento em Tempo Real** | Utiliza a biblioteca `Scapy` para capturar e processar pacotes UDP nas portas do Albion Online (5055, 5056, 5058). |
| **Damage Meter** | Estrutura pronta para exibir estatísticas de combate ao vivo (Dano Causado, Cura Realizada, DPS). |
| **Interface Moderna** | Construído com o framework Flet, oferecendo uma experiência de desktop rápida e com aparência nativa. |
| **Gerenciamento de Sessão** | Funcionalidades para iniciar, parar, redefinir e salvar estatísticas de sessões de jogo. |

## 🛠️ Instalação e Uso

A instalação requer **Python 3.8+** e as bibliotecas **Flet** e **Scapy**. Devido à natureza da captura de pacotes de rede, a aplicação **deve ser executada com privilégios de administrador/root**.

### 1. Pré-requisitos

*   Python 3.8+
*   Flet e Scapy (instalados via `pip`)
*   No Windows, pode ser necessário instalar o **Npcap** para o Scapy funcionar.

### 2. Instalação Rápida (Linux)

O repositório inclui scripts de automação para facilitar a instalação:

```bash
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight
./install.sh  # Instala dependências e cria ambiente virtual
./run.sh      # Executa a aplicação com privilégios de root
```

### 3. Execução Manual

Para executar a aplicação manualmente, use o seguinte comando (após instalar as dependências e dentro do ambiente virtual, se aplicável):

```bash
# No Linux (com privilégios de root)
sudo python3 -m albion_insight

# No Windows (em Prompt de Comando/PowerShell como Administrador)
python -m albion_insight
```

## 🏗️ Estrutura do Projeto (Para Contribuidores)

O projeto segue uma estrutura modular para facilitar a manutenção e o desenvolvimento:

| Diretório/Módulo | Responsabilidade |
| :--- | :--- |
| `albion_insight/core/` | Contém a lógica de negócio principal, como o rastreamento de rede (`network_tracker.py`), a decodificação do protocolo Photon (`photon_decoder.py`) e os modelos de dados (`models.py`). |
| `albion_insight/ui/` | Responsável pela interface do usuário e seus componentes, utilizando o framework Flet. |
| `albion_insight/utils/` | Funções auxiliares, como configuração de logging (`logger.py`) e variáveis de ambiente. |
| `tests/` | Contém os testes unitários e de integração para garantir a qualidade do código. |

## 🤝 Contribuições

Contribuições são muito bem-vindas! Se você deseja ajudar a melhorar o Albion Insight, por favor, leia o nosso [Guia de Contribuição](CONTRIBUTING.md).

As áreas de contribuição incluem:
*   **Desenvolvimento:** Implementação de mais eventos do protocolo Photon e refatoração de módulos.
*   **Testes:** Adição de testes unitários e de integração.
*   **Documentação:** Tradução e melhoria da documentação existente.
*   **Relatório de Bugs:** Abrir Issues para problemas encontrados.

## 📦 Construindo um Executável

Para criar uma versão standalone do aplicativo que não requer a instalação do Python, você pode usar o **PyInstaller**. Consulte o arquivo [PACKAGING.md](PACKAGING.md) para instruções detalhadas sobre como construir executáveis para diferentes sistemas operacionais.

---
*Esta página foi atualizada como parte de um esforço de manutenção e aplicação de melhores práticas de código aberto, incluindo a adição de detalhes sobre a estrutura do projeto para novos contribuidores.*
