# Guia de Instalação do Albion Insight

Este guia fornece instruções detalhadas sobre como instalar e executar o **Albion Insight** em diferentes sistemas operacionais.

## Pré-requisitos

O Albion Insight é construído em Python e requer as seguintes dependências:

1.  **Python 3.8+**: Certifique-se de ter uma versão compatível do Python instalada.
2.  **Bibliotecas Python**: `flet` e `scapy`.
3.  **Privilégios de Administrador/Root**: A captura de pacotes de rede (sniffing) requer permissões elevadas. O aplicativo **deve** ser executado como `root` (Linux/macOS) ou **Administrador** (Windows).

---

## Opção 1: Instalação Rápida (Linux - Recomendado)

Para usuários de Linux (Debian/Ubuntu), o repositório inclui scripts que automatizam a instalação de dependências do sistema, a criação de um ambiente virtual e a execução.

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```

2.  **Execute o Script de Instalação:**
    ```bash
    ./install.sh
    ```
    Este script irá instalar as dependências do sistema (`libpcap-dev`, `python3-pip`, `python3-venv`), criar um ambiente virtual (`venv`) e instalar as bibliotecas Python necessárias.

3.  **Execute o Aplicativo:**
    ```bash
    ./run.sh
    ```
    O script `run.sh` solicitará automaticamente a senha de `root` (via `sudo`) e iniciará o aplicativo.

---

## Opção 2: Instalação Manual (Windows, macOS e Outros Linux)

### Passo 1: Instalar Dependências do Sistema

| Sistema Operacional | Dependências Necessárias | Comando de Instalação |
| :--- | :--- | :--- |
| **Linux (Debian/Ubuntu)** | `libpcap-dev`, `python3-pip`, `python3-venv` | `sudo apt update && sudo apt install libpcap-dev python3-pip python3-venv` |
| **macOS** | `libpcap` (geralmente pré-instalado) | N/A |
| **Windows** | Python 3.8+ (Instalador oficial) | N/A |

### Passo 2: Instalar Bibliotecas Python

Recomendamos o uso de um **ambiente virtual** para isolar as dependências do projeto.

1.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    # Crie o ambiente virtual
    python3 -m venv venv
    
    # Ative (Linux/macOS)
    source venv/bin/activate
    
    # Ative (Windows - PowerShell)
    .\venv\Scripts\Activate.ps1
    
    # Ative (Windows - CMD)
    .\venv\Scripts\activate.bat
    ```

2.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    # ou
    pip install flet scapy
    ```

### Passo 3: Executar o Aplicativo

O Albion Insight deve ser executado com privilégios elevados para permitir a captura de pacotes de rede.

| Sistema Operacional | Comando de Execução (dentro do ambiente virtual) |
| :--- | :--- |
| **Linux/macOS** | `sudo venv/bin/python3 albion_insight.py` |
| **Windows** | **Execute o Prompt de Comando/PowerShell como Administrador** e depois: `python albion_insight.py` |

Após a execução, o aplicativo abrirá em uma janela de desktop nativa.

## Solução de Problemas Comuns

### "Permission denied" (Permissão Negada)
*   **Causa:** O aplicativo não está sendo executado com privilégios de administrador/root.
*   **Solução:** Certifique-se de usar `sudo` no Linux/macOS ou de executar o terminal como Administrador no Windows.

### "No network interfaces found" (Nenhuma interface de rede encontrada)
*   **Causa:** O Scapy não conseguiu listar as interfaces de rede.
*   **Solução:** Verifique se o `libpcap` (ou equivalente no seu sistema) está instalado corretamente. No Windows, certifique-se de que o **Npcap** (necessário para o Scapy) está instalado.

### Erros de Decodificação
*   **Causa:** O protocolo do Albion Online pode ter sido atualizado.
*   **Solução:** Verifique o repositório para atualizações ou abra uma [Issue](https://github.com/dexcarva/AlbionInsight/issues) para relatar o problema.
