# Guia de Instalação do Albion Insight

Este guia fornece instruções passo a passo para instalar e executar o Albion Insight em diferentes sistemas operacionais.

## Pré-requisitos

*   **Python 3.8+**
*   **Git** (para clonar o repositório)
*   **Root/Administrator Privileges** (para a captura de pacotes de rede com `scapy`).

## Opção 1: Instalação Rápida (Linux - Recomendado)

Para usuários Linux, fornecemos scripts automatizados que simplificam o processo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```

2.  **Execute o script de instalação:**
    ```bash
    ./install.sh
    ```
    Este script irá:
    *   Instalar dependências de sistema (como `libpcap-dev`).
    *   Criar e ativar um ambiente virtual Python (`venv`).
    *   Instalar as dependências Python (`flet`, `scapy`).

3.  **Execute a aplicação:**
    ```bash
    ./run.sh
    ```
    O script `run.sh` solicitará automaticamente privilégios de root para iniciar a captura de pacotes.

## Opção 2: Instalação Manual

### 1. Instalar Dependências de Sistema

**No Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**No Windows:**
*   Instale o Python 3.8+ a partir de [python.org](https://www.python.org/downloads/).
*   Certifique-se de que o **Wireshark** ou **Npcap** esteja instalado para que o `scapy` funcione corretamente.

### 2. Instalar Dependências Python

Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Criar ambiente virtual
    python3 -m venv venv

    # Ativar (Linux/macOS)
    source venv/bin/activate

    # Ativar (Windows)
    venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Executar a Aplicação

A captura de pacotes requer privilégios elevados.

**No Linux (com ambiente virtual ativado):**
```bash
sudo python3 albion_insight.py
```

**No Windows (Execute o Prompt de Comando/PowerShell como Administrador):**
```bash
python albion_insight.py
```

A aplicação será aberta em uma janela de desktop nativa.

## Solução de Problemas

*   **"Permission denied" ao iniciar:** Certifique-se de que está executando a aplicação com `sudo` (Linux/macOS) ou como **Administrador** (Windows).
*   **"No network interfaces found"**: Verifique se o `scapy` está instalado corretamente e se as dependências de sistema (como `libpcap-dev`) estão presentes.
*   **Erro de ícone (`AttributeError: module 'flet' has no attribute 'icons'`):** Certifique-se de que sua versão do `flet` está atualizada (verifique o `requirements.txt`).
