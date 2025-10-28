# Albion Insight

**[Read this in English (Leia em Inglês)](README.md)**

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

### 1. Instalar Dependências do Python

Certifique-se de ter o Python instalado. Em seguida, instale as bibliotecas necessárias:

```bash
pip3 install flet scapy pyinstaller
```

### 2. Dependências de Captura de Rede (Linux)

No Linux, você pode precisar instalar o `libpcap` ou `tcpdump` para que o Scapy funcione corretamente.

```bash
# Exemplo para Debian/Ubuntu
sudo apt update
sudo apt install libpcap-dev
```

### 3. Executando a Aplicação

Como a captura de rede requer privilégios elevados, você deve executar a aplicação como root ou administrador.

**No Linux:**

```bash
sudo python3 albion_insight.py
```

**No Windows (Execute o Prompt de Comando/PowerShell como Administrador):**

```bash
python albion_insight.py
```

A aplicação será aberta em uma janela desktop nativa.

## Como Criar um Executável

A aplicação pode ser empacotada em um executável standalone usando o **PyInstaller**. Isso permite que os usuários executem a aplicação sem instalar o Python ou suas dependências.

### 1. Comando de Build

Execute o seguinte comando no diretório raiz do projeto:

```bash
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight.py
```

*   `--name "AlbionInsight"`: Define o nome do arquivo executável.
*   `--onefile`: Cria um único arquivo executável (facilita a distribuição).
*   `--windowed`: Oculta a janela do console (para aplicações desktop no Windows/macOS).

### 2. Distribuição

O executável estará localizado na pasta `dist`. Você pode distribuir este arquivo para usuários do respectivo sistema operacional.

## Estrutura do Projeto

A aplicação inteira está contida em um único arquivo para simplicidade:

| Arquivo | Descrição |
| :--- | :--- |
| `albion_insight.py` | O arquivo principal da aplicação contendo toda a lógica (Modelos, Rastreador de Rede, Interface Flet). |
| `README.md` | Este arquivo de documentação (em inglês). |
| `README.pt-BR.md` | Este arquivo de documentação (em português). |

## Status Atual (Dados em Tempo Real)

A aplicação agora inclui a lógica de **Decodificação do Protocolo Photon**, traduzida do projeto C# original. Isso permite que a aplicação processe eventos em tempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` diretamente do tráfego de rede.

**Nota:** A tradução completa de todos os eventos de combate (como `CastHit`, `Attack`) é um esforço contínuo. A implementação atual foca nas estatísticas principais e na estrutura do Medidor de Dano. O cálculo de DPS do Medidor de Dano é baseado nos eventos decodificados.

## Contribuindo

Aceitamos contribuições da comunidade! Seja você um desenvolvedor, designer ou apenas um entusiasta do Albion Online, existem muitas maneiras de ajudar a melhorar o Albion Insight.

### Como Você Pode Contribuir:

*   **Reportar Bugs:** Encontrou um bug? Abra uma issue na nossa página de [GitHub Issues](https://github.com/dexcarva/AlbionInsight/issues) com passos detalhados para reproduzi-lo.
*   **Sugerir Funcionalidades:** Tem uma ideia para uma nova funcionalidade? Compartilhe na seção de Issues com a label "enhancement".
*   **Melhorar a Documentação:** Ajude-nos a melhorar o README, adicionar tutoriais ou traduzir a documentação para outros idiomas.
*   **Contribuições de Código:** Faça um fork do repositório, faça suas alterações e envie um Pull Request. Certifique-se de seguir o estilo de código e incluir testes, se aplicável.
*   **Testar em Diferentes Plataformas:** Ajude-nos a testar a aplicação em várias distribuições Linux, versões do Windows e macOS para garantir compatibilidade.
*   **Decodificar Mais Eventos:** O Protocolo Photon tem centenas de tipos de eventos. Ajude-nos a traduzir mais handlers de eventos do código C# original para Python.

### Começando:

1.  Faça um fork do repositório: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone seu fork: `git clone https://github.com/SEU_USUARIO/AlbionInsight.git`
3.  Crie uma nova branch: `git checkout -b feature/nome-da-sua-funcionalidade`
4.  Faça suas alterações e commit: `git commit -m "Adiciona sua funcionalidade"`
5.  Envie para seu fork: `git push origin feature/nome-da-sua-funcionalidade`
6.  Abra um Pull Request no repositório principal

---
*Uma solução multiplataforma para a comunidade do Albion Online.*

