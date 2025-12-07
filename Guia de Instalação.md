# Instalação e Configuração

A instalação do Albion Insight requer o Python 3.8+ e privilégios de administrador/root para a captura de pacotes de rede.

## 1. Linux (Recomendado)

Recomendamos o uso dos scripts de instalação para uma configuração mais rápida:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```
2.  **Execute a Instalação:**
    ```bash
    ./install.sh
    ```
    *Este script instalará as dependências do sistema (`libpcap-dev`) e criará um ambiente virtual.*
3.  **Execute o Aplicativo:**
    ```bash
    ./run.sh
    ```
    *O script `run.sh` solicitará automaticamente a senha de root/sudo para iniciar a captura de pacotes.*

## 2. Windows

1.  **Instale o Python:** Baixe e instale o Python 3.8+ em [python.org](https://www.python.org/downloads/).
2.  **Instale as Dependências:**
    ```powershell
    pip install flet scapy
    ```
3.  **Execute como Administrador:** Abra o Prompt de Comando ou PowerShell **como Administrador** e execute:
    ```powershell
    python -m albion_insight
    ```

## 3. macOS

*Instruções de instalação para macOS serão adicionadas em breve. Atualmente, a instalação manual via `pip` e a execução com `sudo` são necessárias.*

[[Home]]
