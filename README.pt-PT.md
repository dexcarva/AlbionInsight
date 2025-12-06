# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

O **Albion Insight** é uma ferramenta de análise estatística multi-plataforma (Linux, Windows, macOS) para o jogo Albion Online, re-implementada em **Python** utilizando o *framework* **Flet**. Foi concebida para monitorizar estatísticas em tempo real no jogo, incluindo prata, fama e dados de combate (Medidor de Dano), através da análise do tráfego de rede.

Este projeto é uma alternativa moderna e de código aberto à ferramenta original `AlbionOnline-StatisticsAnalysis`, baseada em C#/WPF, focando-se na compatibilidade multi-plataforma e facilidade de utilização.

## Funcionalidades

*   **Compatibilidade Multi-Plataforma:** Executa nativamente em Linux, Windows e macOS.
*   **Monitorização em Tempo Real:** Utiliza a biblioteca `Scapy` para farejar pacotes UDP nas portas do Albion Online (5055, 5056, 5058).
*   **Estrutura do Medidor de Dano:** Inclui as estruturas de dados e interface de utilizador necessárias para exibir estatísticas de combate em direto (Dano Causado, Cura Realizada, DPS).
*   **Interface de Utilizador Moderna:** Construída com Flet, fornecendo uma aplicação de desktop com aparência nativa e rápida.
*   **Gestão de Sessões:** Permite iniciar, parar, redefinir e guardar estatísticas de sessão.

## Pré-requisitos

*   Python 3.8+
*   Bibliotecas **Flet** e **Scapy**.
*   **Privilégios de Root/Administrador:** Necessários para a captura de pacotes de rede.

## Instalação e Configuração

### Opção 1: Instalação Rápida (Linux - Recomendado)

Para utilizadores Linux, fornecemos scripts de instalação automatizados:

\`\`\`bash
# 1. Clonar o repositório
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Executar o script de instalação
./install.sh

# 3. Executar a aplicação
./run.sh
\`\`\`

O script `install.sh` irá:
- Instalar dependências do sistema (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Criar um ambiente virtual Python
- Instalar todos os pacotes Python necessários (Flet, Scapy)

O script `run.sh` solicitará automaticamente privilégios de root e executará a aplicação.

### Opção 2: Instalação Manual

#### 1. Instalar Dependências do Sistema

**Em Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Em Windows:**

Instalar Python 3.8+ a partir de [python.org](https://www.python.org/downloads/)

#### 2. Instalar Dependências Python

**Em Linux (utilizando ambiente virtual - recomendado):**

\`\`\`bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install flet scapy
\`\`\`

**Em Linux (instalação a nível de sistema):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Em Windows (Executar Linha de Comandos/PowerShell como Administrador):**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Executar a Aplicação

Uma vez que o farejamento de rede requer privilégios elevados, deve executar a aplicação como root ou administrador.

**Em Linux (com ambiente virtual):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Em Linux (instalação a nível de sistema):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Em Windows (Executar Linha de Comandos/PowerShell como Administrador):**

\`\`\`bash
python -m albion_insight
\`\`\`

A aplicação abrirá numa janela de desktop nativa.

## Como Criar um Executável

A aplicação pode ser empacotada num executável autónomo utilizando o **PyInstaller**. Isto permite aos utilizadores executar a aplicação sem instalar o Python ou as suas dependências.

Para instruções detalhadas sobre a criação de executáveis para Linux, Windows e macOS, consulte o guia **[PACKAGING.md](PACKAGING.md)**.

### Compilação Rápida (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

O executável estará localizado na pasta `dist/`.

## Estrutura do Projeto

A aplicação está estruturada em componentes modulares para melhor manutenção e escalabilidade:

| Ficheiro | Descrição |
| :--- | :--- |
| `albion_insight/core/` | Lógica central, monitorização de rede, modelos de dados e descodificação de protocolo. |
| `albion_insight/ui/` | Componentes da interface de utilizador construídos com Flet. |
| `albion_insight/utils/` | Funções de utilidade, configuração e registo. |
| `albion_insight/__main__.py` | Ponto de entrada para a aplicação. |
| `README.md` | Este ficheiro de documentação. |
| `CONTRIBUTING.md` | Diretrizes para contribuir para o projeto. |
| `CODE_OF_CONDUCT.md` | O Código de Conduta do projeto. |
| `SECURITY.md` | Política para relatar vulnerabilidades de segurança. |
| `README.it-IT.md` | Documentazione in italiano. |
| `README.pt-BR.md` | Documentação em português do Brasil. |
| `README.ru-RU.md` | Документация на русском языке. |
| `README.fr-FR.md` | Documentation en français. |
| `README.zh-CN.md` | 简体中文文档 (Simplified Chinese documentation). |
| `README.ko-KR.md` | 한국어 문서 (Korean documentation). |
| `README.es-ES.md` | Documentación en español (Spanish documentation). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Polish documentation). |
| `README.sv-SE.md` | Dokumentation på svenska (Swedish documentation). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (Vietnamese documentation). |
| `README.pt-PT.md` | Documentação em português europeu. |

## Estado Atual (Dados em Tempo Real)

A aplicação inclui agora a lógica de **Descodificação do Protocolo Photon**, traduzida do projeto original em C#. Isto permite que a aplicação processe eventos em tempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` diretamente do tráfego de rede.

**Nota:** A tradução completa de cada evento de combate (como `CastHit`, `Attack`) é um esforço contínuo. A implementação atual foca-se nas estatísticas centrais e na estrutura para o Medidor de Dano. O cálculo de DPS do Medidor de Dano baseia-se nos eventos descodificados.

## Contribuições

Acolhemos contribuições da comunidade! Quer seja um programador, designer ou apenas um entusiasta do Albion Online, existem muitas formas de ajudar a melhorar o Albion Insight.

Por favor, leia as nossas [Diretrizes de Contribuição](CONTRIBUTING.md) para informações detalhadas sobre como contribuir para este projeto.

### Início Rápido para Contribuintes:

1.  *Fork* o repositório: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone o seu *fork*: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Crie um novo *branch*: `git checkout -b feature/o-seu-nome-da-funcionalidade`
4.  Faça as suas alterações e *commit*: `git commit -m "Adicionar a sua funcionalidade"`
5.  *Push* para o seu *fork*: `git push origin feature/o-seu-nome-da-funcionalidade`
6.  Abra um *Pull Request* no repositório principal

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o ficheiro [LICENSE](LICENSE) para detalhes.

## Agradecimentos

- Projeto original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) por Triky313
- Construído com o *framework* [Flet](https://flet.dev/)
- Análise de rede alimentada por [Scapy](https://scapy.net/)

---
*Uma solução multi-plataforma para a comunidade Albion Online.*
