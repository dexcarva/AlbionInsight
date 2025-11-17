# Albion Insight

[![Licença: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Versão Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Plataforma](https://img.shields.io/badge/plataforma-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contribuições Bem-vindas](https://img.shields.io/badge/contribui%C3%A7%C3%B5es-bem--vindas-brightgreen.svg)](CONTRIBUTING.pt-BR.md)

**[Read this in English (Leia em Inglês)](README.md)**
**[Leia em Espanhol (Leer en Español)](README.es-ES.md)**
**[Leia em Francês (Lire en Français)](README.fr-FR.md)**
**[Leia em Italiano (Leggi in Italiano)](README.it-IT.md)**
**[Leia em Russo (Читать на русском)](README.ru-RU.md)**

**Albion Insight** é uma ferramenta de análise de estatísticas multiplataforma (Linux, Windows, macOS) para o jogo Albion Online, reimplementada em **Python** usando o framework **Flet**. Ela foi projetada para rastrear estatísticas do jogo em tempo real, incluindo prata, fama e dados de combate (Medidor de Dano), analisando o tráfego de rede.

Este projeto é uma alternativa moderna e de código aberto à ferramenta original `AlbionOnline-StatisticsAnalysis` baseada em C#/WPF, com foco em compatibilidade multiplataforma e facilidade de uso.

## Funcionalidades

*   **Compatibilidade Multiplataforma:** Roda nativamente no Linux, Windows e macOS.
*   **Rastreamento em Tempo Real:** Usa a biblioteca `Scapy` para capturar pacotes UDP nas portas do Albion Online (5055, 5056, 5058).
*   **Estrutura do Medidor de Dano:** Inclui as estruturas de dados e a interface necessárias para exibir estatísticas de combate ao vivo (Dano Causado, Cura Realizada, DPS).
*   **Interface Moderna:** Construída com Flet, proporcionando uma aplicação desktop rápida e com aparência nativa.
*   **Gerenciamento de Sessão:** Permite iniciar, parar, resetar e salvar estatísticas de sessão.

## Pré-requisitos

*   Python 3.8+
*   Bibliotecas **Flet** e **Scapy**.
*   **Privilégios de Root/Administrador:** Necessários para captura de pacotes de rede.

## Instalação e Configuração

### Opção 1: Instalação Rápida (Linux - Recomendado)

Para usuários Linux, fornecemos scripts de instalação automatizados:

```bash
# 1. Clone o repositório
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Execute o script de instalação
./install.sh

# 3. Execute a aplicação
./run.sh
```

O script `install.sh` irá:
- Instalar dependências do sistema (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Criar um ambiente virtual Python
- Instalar todos os pacotes Python necessários (Flet, Scapy)

O script `run.sh` irá automaticamente solicitar privilégios de root e executar a aplicação.

### Opção 2: Instalação Manual

#### 1. Instalar Dependências do Sistema

**No Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**No Windows:**

Instale o Python 3.8+ de [python.org](https://www.python.org/downloads/)

#### 2. Instalar Dependências do Python

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

#### 3. Executando a Aplicação

Como a captura de rede requer privilégios elevados, você deve executar a aplicação como root ou administrador.

**No Linux (com ambiente virtual):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**No Linux (instalação em todo o sistema):**

```bash
sudo python3 albion_insight/main.py
```

**No Windows (Execute o Prompt de Comando/PowerShell como Administrador):**

```bash
python albion_insight/main.py
```

A aplicação será aberta em uma janela desktop nativa.

## Como Criar um Executável

A aplicação pode ser empacotada em um executável standalone usando o **PyInstaller**. Isso permite que os usuários executem a aplicação sem instalar o Python ou suas dependências.

Para instruções detalhadas sobre como criar executáveis para Linux, Windows e macOS, consulte o guia **[PACKAGING.md](PACKAGING.md)** (em inglês).

### Build Rápido (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

O executável estará localizado na pasta `dist/`.

## Estrutura do Projeto

A aplicação inteira está contida em um único arquivo para simplicidade:

| Arquivo | Descrição |
| :--- | :--- |
| `albion_insight/main.py` | O arquivo principal da aplicação contendo toda a lógica (Modelos, Rastreador de Rede, Interface Flet). |
| `README.md` | Este arquivo de documentação (em inglês). |
| `README.pt-BR.md` | Este arquivo de documentação (em português). |
| `README.fr-FR.md` | Este arquivo de documentação (em francês). |
| `README.it-IT.md` | Este arquivo de documentação (em italiano). |

## Status Atual (Dados em Tempo Real)

A aplicação agora inclui a lógica de **Decodificação do Protocolo Photon**, traduzida do projeto C# original. Isso permite que a aplicação processe eventos em tempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` diretamente do tráfego de rede.

**Nota:** A tradução completa de todos os eventos de combate (como `CastHit`, `Attack`) é um esforço contínuo. A implementação atual foca nas estatísticas principais e na estrutura do Medidor de Dano. O cálculo de DPS do Medidor de Dano é baseado nos eventos decodificados.

## Contribuindo

Aceitamos contribuições da comunidade! Seja você um desenvolvedor, designer ou apenas um entusiasta do Albion Online, existem muitas maneiras de ajudar a melhorar o Albion Insight.

Por favor, leia nossas [Diretrizes de Contribuição](CONTRIBUTING.pt-BR.md) para informações detalhadas sobre como contribuir com este projeto.

### Início Rápido para Contribuidores:

1.  Faça um fork do repositório: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone seu fork: `git clone https://github.com/SEU_USUARIO/AlbionInsight.git`
3.  Crie uma nova branch: `git checkout -b feature/nome-da-sua-funcionalidade`
4.  Faça suas alterações e commit: `git commit -m "Adiciona sua funcionalidade"`
5.  Envie para seu fork: `git push origin feature/nome-da-sua-funcionalidade`
6.  Abra um Pull Request no repositório principal

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Agradecimentos

- Projeto original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) por Triky313
- Construído com o framework [Flet](https://flet.dev/)
- Análise de rede powered by [Scapy](https://scapy.net/)

---
*Uma solução multiplataforma para a comunidade do Albion Online.*

