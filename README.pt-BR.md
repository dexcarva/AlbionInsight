> Este é um documento traduzido pela comunidade. Pode não estar 100% atualizado com o [documento original em inglês](README.md).

# Albion Insight

[![Licença: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Versão do Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Plataforma](https://img.shields.io/badge/plataforma-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![Issues do GitHub](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contribuições são bem-vindas](https://img.shields.io/badge/contribui%C3%A7%C3%B5es-bem--vindas-brightgreen.svg)](CONTRIBUTING.pt-BR.md)

**[Leia isto em outros idiomas](README.md#translations)**

**Albion Insight** é uma ferramenta de análise de estatísticas multiplataforma (Linux, Windows, macOS) para o jogo Albion Online, reimplementada em **Python** com o framework **Flet**. Ele foi projetado para rastrear estatísticas do jogo em tempo real, como prata, fama e dados de combate (Medidor de Dano), por meio da análise do tráfego de rede.

Este projeto é uma alternativa moderna e de código aberto à ferramenta original `AlbionOnline-StatisticsAnalysis`, baseada em C#/WPF, com foco em compatibilidade multiplataforma e facilidade de uso.

## Funcionalidades

*   **Compatibilidade Multiplataforma:** Funciona nativamente no Linux, Windows e macOS.
*   **Rastreamento em Tempo Real:** Utiliza a biblioteca `Scapy` para capturar pacotes UDP nas portas do Albion Online (5055, 5056, 5058).
*   **Medidor de Dano:** Inclui as estruturas de dados e a interface do usuário para exibir estatísticas de combate ao vivo (Dano Causado, Cura Realizada, DPS).
*   **Interface de Usuário Moderna:** Construído com Flet, oferecendo um aplicativo de desktop rápido e com aparência nativa.
*   **Gerenciamento de Sessão:** Permite iniciar, parar, redefinir e salvar as estatísticas da sessão.

## Pré-requisitos

*   Python 3.8+
*   Bibliotecas **Flet** e **Scapy**.
*   **Privilégios de Root/Administrador:** Necessário para a captura de pacotes de rede.

## Instalação e Configuração

### Opção 1: Instalação Rápida (Linux - Recomendado)

Para usuários de Linux, fornecemos scripts de instalação automatizados:

```bash
# 1. Clone o repositório
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Execute o script de instalação
./install.sh

# 3. Execute o aplicativo
./run.sh
```

O script `install.sh` irá:
- Instalar as dependências do sistema (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Criar um ambiente virtual Python
- Instalar todos os pacotes Python necessários (Flet, Scapy)

O script `run.sh` solicitará automaticamente privilégios de root e executará o aplicativo.

### Opção 2: Instalação Manual

#### 1. Instale as Dependências do Sistema

**No Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**No Windows:**

Instale o Python 3.8+ em [python.org](https://www.python.org/downloads/)

#### 2. Instale as Dependências do Python

**No Linux (usando ambiente virtual - recomendado):**

```bash
# Crie um ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
source venv/bin/activate

# Instale as dependências
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

Como a captura de rede requer privilégios elevados, você deve executar o aplicativo como root ou administrador.

**No Linux (com ambiente virtual):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**No Linux (instalação em todo o sistema):**

```bash
sudo python3 -m albion_insight
```

**No Windows (Execute o Prompt de Comando/PowerShell como Administrador):**

```bash
python -m albion_insight
```

O aplicativo será aberto em uma janela de desktop nativa.

## Como Construir um Executável

O aplicativo pode ser empacotado em um executável autônomo usando o **PyInstaller**. Isso permite que os usuários executem o aplicativo sem instalar o Python ou suas dependências.

Para instruções detalhadas sobre como construir executáveis para Linux, Windows e macOS, consulte o guia **[PACKAGING.md](PACKAGING.md)**.

### Construção Rápida (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed -m albion_insight
```

O executável estará localizado na pasta `dist/`.

## Estrutura do Projeto

| Arquivo | Descrição |
| :--- | :--- |
| `albion_insight/` | O pacote principal do aplicativo. |
| `README.md` | Este arquivo de documentação. |
| `CONTRIBUTING.md` | Diretrizes para contribuir com o projeto. |
| `CODE_OF_CONDUCT.md` | O Código de Conduta do projeto. |
| `SECURITY.md` | Política para relatar vulnerabilidades de segurança. |

## Status Atual (Dados em Tempo Real)

O aplicativo agora inclui a lógica de **Decodificação do Protocolo Photon**, traduzida do projeto original em C#. Isso permite que o aplicativo processe eventos em tempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` diretamente do tráfego de rede.

**Nota:** A tradução completa de cada evento de combate (como `CastHit`, `Attack`) é um esforço contínuo. A implementação atual foca nas estatísticas principais e na estrutura do Medidor de Dano. O cálculo de DPS do Medidor de Dano é baseado nos eventos decodificados.

## Contribuindo

Recebemos bem as contribuições da comunidade! Seja você um desenvolvedor, designer ou apenas um entusiasta do Albion Online, há muitas maneiras de ajudar a melhorar o Albion Insight.

Por favor, leia nossas [Diretrizes de Contribuição](CONTRIBUTING.pt-BR.md) para informações detalhadas sobre como contribuir para este projeto.

### Início Rápido para Contribuidores:

1.  Faça um fork do repositório: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone seu fork: `git clone https://github.com/SEU_USUARIO/AlbionInsight.git`
3.  Crie um novo branch: `git checkout -b feature/sua-funcionalidade`
4.  Faça suas alterações e commit: `git commit -m "Adiciona sua funcionalidade"`
5.  Envie para o seu fork: `git push origin feature/sua-funcionalidade`
6.  Abra um Pull Request no repositório principal.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Agradecimentos

- Projeto original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) por Triky313
- Construído com o framework [Flet](https://flet.dev/)
- Análise de rede com a tecnologia [Scapy](https://scapy.net/)

---
*Uma solução multiplataforma para a comunidade do Albion Online.*
