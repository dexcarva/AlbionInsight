# Albion Insight

Leia isto noutras línguas

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Leia isto noutras línguas</summary>

**[Árabe](README.ar-SA.md)** | **[Alemão](README.de-DE.md)** | **[Grego](README.el-GR.md)** | **[Espanhol](README.es-ES.md)** | **[Francês](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Húngaro](README.hu-HU.md)** | **[Indonésio](README.id-ID.md)** | **[Italiano](README.it-IT.md)** | **[Japonês](README.ja-JP.md)** | **[Coreano](README.ko-KR.md)** | **[Holandês](README.nl-NL.md)** | **[Polaco](README.pl-PL.md)** | **[Português (Brasil)](README.pt-BR.md)** | **[Romeno](README.ro-RO.md)** | **[Russo](README.ru-RU.md)** | **[Sueco](README.sv-SE.md)** | **[Tailandês](README.th-TH.md)** | **[Turco](README.tr-TR.md)** | **[Vietnamita](README.vi-VN.md)** | **[Chinês (Simplificado)](README.zh-CN.md)** | **[Chinês (Tradicional)](README.zh-TW.md)** | **[Chinês (Tradicional - Hong Kong)](README.zh-HK.md)** | **[Checo](README.cs-CZ.md)** | **[Persa (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)** | **[Português (Portugal)](README.pt-PT.md)**

</details>

**Albion Insight** é uma ferramenta de análise estatística multi-plataforma (Linux, Windows, macOS) para o jogo Albion Online, re-implementada em **Python** usando o framework **Flet**. Foi concebida para rastrear estatísticas em tempo real no jogo, incluindo prata, fama e dados de combate (Medidor de Dano), analisando o tráfego de rede.

Este projeto é uma alternativa moderna e de código aberto à ferramenta original `AlbionOnline-StatisticsAnalysis` baseada em C#/WPF, focando na compatibilidade multi-plataforma e facilidade de uso.

## Funcionalidades

*   **Compatibilidade Multi-Plataforma:** Executa nativamente em Linux, Windows e macOS.
*   **Rastreamento em Tempo Real:** Usa a biblioteca `Scapy` para farejar pacotes UDP nas portas do Albion Online (5055, 5056, 5058).
*   **Estrutura do Medidor de Dano:** Inclui as estruturas de dados e UI necessárias para exibir estatísticas de combate em tempo real (Dano Causado, Cura Realizada, DPS).
*   **UI Moderna:** Construída com Flet, fornecendo uma aplicação de desktop rápida e com aparência nativa.
*   **Gestão de Sessões:** Permite iniciar, parar, reiniciar e guardar estatísticas de sessão.

## Pré-requisitos

*   Python 3.8+
*   Bibliotecas **Flet** e **Scapy**.
*   **Privilégios de Root/Administrador:** Necessários para a captura de pacotes de rede.

## Instalação e Configuração

### Opção 1: Instalação Rápida (Linux - Recomendado)

Para utilizadores Linux, fornecemos scripts de instalação automatizados:

```bash
# 1. Clonar o repositório
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Executar o script de instalação
./install.sh

# 3. Executar a aplicação
./run.sh
```

O script `install.sh` irá:

*   Instalar dependências do sistema (`libpcap-dev`, `python3-pip`, `python3-venv`)
*   Criar um ambiente virtual Python
*   Instalar todos os pacotes Python necessários (Flet, Scapy)

O script `run.sh` solicitará automaticamente privilégios de root e executará a aplicação.

### Opção 2: Instalação Manual

#### 1\. Instalar Dependências do Sistema

**No Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**No Windows:**

Instale o Python 3.8+ a partir de [python.org]()

#### 2\. Instalar Dependências Python

**No Linux (usando ambiente virtual - recomendado):**

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install flet scapy
```

**No Linux (instalação em todo o sistema):**

```bash
pip3 install flet scapy --break-system-packages
```

**No Windows:**

```bash
pip install flet scapy
```

#### 3\. Executar a Aplicação

Uma vez que a análise de rede requer privilégios elevados, deve executar a aplicação como root ou administrador.

**No Linux (com ambiente virtual):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**No Linux (instalação em todo o sistema):**

```bash
sudo python3 -m albion_insight
```

**No Windows (Executar Linha de Comandos/PowerShell como Administrador):**

```bash
python -m albion_insight
```

A aplicação abrirá numa janela de desktop nativa.

## Como Criar um Executável

A aplicação pode ser empacotada num executável autónomo usando o **PyInstaller**. Isto permite que os utilizadores executem a aplicação sem instalar o Python ou as suas dependências.

Para instruções detalhadas sobre como criar executáveis para Linux, Windows e macOS, consulte o guia **[PACKAGING.md]()**.

### Criação Rápida (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed -m albion_insight
```

O executável estará localizado na pasta `dist/`.

## Estrutura do Projeto

A aplicação está estruturada em componentes modulares para melhor manutenção e escalabilidade:

| Ficheiro | Descrição |
| :-- | :-- |
| `albion_insight/core/` | Lógica central, rastreamento de rede, modelos de dados e descodificação de protocolo. |
| `albion_insight/ui/` | Componentes da interface de utilizador construídos com Flet. |
| `albion_insight/utils/` | Funções de utilidade, configuração e registo (logging). |
| `albion_insight/__main__.py` | Ponto de entrada para a aplicação. |
| `README.md` | Documentação principal em Inglês. |
| `README.pt-BR.md` | Esta documentação em Português do Brasil. |
| `README.pt-PT.md` | Esta documentação em Português de Portugal. |
| `CONTRIBUTING.md` | Diretrizes para contribuir para o projeto. |
| `CODE_OF_CONDUCT.md` | O Código de Conduta do projeto. |
| `SECURITY.md` | Política para relatar vulnerabilidades de segurança. |

## Estado Atual (Dados em Tempo Real)

A aplicação inclui agora a lógica de **Descodificação do Protocolo Photon**, traduzida do projeto C# original. Isto permite que a aplicação processe eventos em tempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` diretamente do tráfego de rede.

**Nota:** A tradução completa de cada evento de combate (como `CastHit`, `Attack`) é um esforço contínuo. A implementação atual foca nas estatísticas centrais e na estrutura para o Medidor de Dano. O cálculo de DPS do Medidor de Dano é baseado nos eventos descodificados.
