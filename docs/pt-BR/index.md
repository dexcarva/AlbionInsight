# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Read this in other languages</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Português (Brasil - pt-BR)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)** | **[Czech](README.cs-CZ.md)** | **[Persian (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)** | **[Português (Portugal)](README.pt-PT.md)** | **[Hebrew](README.he-IL.md)** | **[Norwegian](README.no-NO.md)** | **[Finnish](README.fi-FI.md)**

</details>

**Albion Insight** é uma ferramenta de análise de estatísticas multiplataforma (Linux, Windows, macOS) para o jogo Albion Online, reimplementada em **Python** usando o framework **Flet**. Ele foi projetado para rastrear estatísticas em tempo real no jogo, incluindo prata, fama e dados de combate (Medidor de Dano), analisando o tráfego de rede.

Este projeto é uma alternativa moderna e de código aberto à ferramenta original `AlbionOnline-StatisticsAnalysis` baseada em C#/WPF, focada em compatibilidade multiplataforma e facilidade de uso.

## Funcionalidades

*   **Compatibilidade Multiplataforma:** Funciona nativamente em Linux, Windows e macOS.
*   **Rastreamento em Tempo Real:** Usa a biblioteca `Scapy` para farejar pacotes UDP nas portas do Albion Online (5055, 5056, 5058).
*   **Estrutura do Medidor de Dano:** Inclui as estruturas de dados e a interface de usuário necessárias para exibir estatísticas de combate ao vivo (Dano Causado, Cura Realizada, DPS).
*   **Interface de Usuário Moderna:** Construído com Flet, fornecendo um aplicativo de desktop rápido e com aparência nativa.
*   **Gerenciamento de Sessão:** Permite iniciar, parar, redefinir e salvar estatísticas de sessão.

## Pré-requisitos

*   Python 3.8+
*   Bibliotecas **Flet** e **Scapy**.
*   **Privilégios de Root/Administrador:** Necessários para a captura de pacotes de rede.

## Instalação e Configuração

### Opção 1: Instalação Rápida (Linux - Recomendado)

Para usuários Linux, fornecemos scripts de instalação automatizados:

```bash
# 1. Clonar o repositório
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Executar o script de instalação
./install.sh

# 3. Executar o aplicativo
./run.sh
```

O script `install.sh` irá:
- Instalar dependências do sistema (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Criar um ambiente virtual Python
- Instalar todos os pacotes Python necessários (Flet, Scapy)

O script `run.sh` solicitará automaticamente privilégios de root e executará o aplicativo.

### Opção 2: Instalação Manual

#### 1. Instalar Dependências do Sistema

**No Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**No Windows:**

Instale o Python 3.8+ em [python.org](https://www.python.org/downloads/)

#### 2. Instalar Dependências Python

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

#### 3. Executando o Aplicativo

Como o farejamento de rede requer privilégios elevados, você deve executar o aplicativo como root ou administrador.

**No Linux (com ambiente virtual):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**No Linux (instalação em todo o sistema):**

```bash
sudo python3 -m albion_insight
```

**No Windows (Executar Prompt de Comando/PowerShell como Administrador):**

```bash
python -m albion_insight
```

O aplicativo será aberto em uma janela de desktop nativa.

## Como Criar um Executável

O aplicativo pode ser empacotado em um executável autônomo usando **PyInstaller**. Isso permite que os usuários executem o aplicativo sem instalar o Python ou suas dependências.

Para instruções detalhadas sobre a criação de executáveis para Linux, Windows e macOS, consulte o guia **[PACKAGING.md](PACKAGING.md)**.

### Compilação Rápida (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

O executável estará localizado na pasta `dist/`.

## Estrutura do Projeto

The application is structured into modular components for better maintainability and scalability:

| Arquivo | Descrição |
| :--- | :--- |
| `albion_insight/core/` | Lógica central, rastreamento de rede, modelos de dados e decodificação de protocolo. |
| `albion_insight/ui/` | Componentes da interface de usuário construídos com Flet. |
| `albion_insight/utils/` | Funções utilitárias, configuração e registro (logging). |
| `albion_insight/__main__.py` | Ponto de entrada para o aplicativo. |
|| `README.md` | Este arquivo de documentação principal. |
| `README.pt-BR.md` | Este arquivo de documentação em Português do Brasil. |
| `README.fil-PH.md` | Este arquivo de documentação em Filipino (Tagalog). |
| `README.pt-PT.md` | Este arquivo de documentação em Português de Portugal. |
| `CONTRIBUTING.md` | Diretrizes para contribuição ao projeto. |
| `CODE_OF_CONDUCT.md` | Código de Conduta do projeto. |
| `SECURITY.md` | Política para reportar vulnerabilidades de segurança. |

## Status Atual (Dados em Tempo Real)

O aplicativo agora inclui a lógica de **Decodificação do Protocolo Photon**, traduzida do projeto original em C#. Isso permite que o aplicativo processe eventos em tempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` diretamente do tráfego de rede.

**Nota:** A tradução completa de todos os eventos de combate (como `CastHit`, `Attack`) é um esforço contínuo. A implementação atual foca nas estatísticas centrais e na estrutura para o Medidor de Dano. O cálculo de DPS do Medidor de Dano é baseado nos eventos decodificados.

## Contribuindo

Aceitamos contribuições da comunidade! Seja você um desenvolvedor, designer ou apenas um entusiasta de Albion Online, há muitas maneiras de ajudar a melhorar o Albion Insight.

Por favor, leia nossas [Diretrizes de Contribuição](CONTRIBUTING.md) para informações detalhadas sobre como contribuir para este projeto.

### Início Rápido para Contribuidores:

1.  Faça um Fork do repositório: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone seu fork: `git clone https://github.com/SEU_NOME_DE_USUARIO/AlbionInsight.git`
3.  Crie uma nova branch: `git checkout -b feature/seu-nome-da-funcionalidade`
4.  Faça suas alterações e commit: `git commit -m "Adicionar sua funcionalidade"`
5.  Envie para o seu fork: `git push origin feature/seu-nome-da-funcionalidade`
6.  Abra um Pull Request no repositório principal

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

- Projeto original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) por Triky313
- Construído com o framework [Flet](https://flet.dev/)
- Análise de rede otimizada por [Scapy](https://scapy.net/)

---
*Uma solução multiplataforma para a comunidade de Albion Online.*
