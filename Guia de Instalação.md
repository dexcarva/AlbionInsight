# Guia de Instalação e Configuração

A instalação do Albion Insight requer o Python 3.8+ e privilégios de administrador/root para a captura de pacotes de rede.

## 1. Linux (Recomendado - Instalação Segura com `setcap`)

O Albion Insight utiliza a biblioteca `Scapy` para "farejar" (sniff) o tráfego de rede. Para evitar a má prática de executar o aplicativo inteiro como `root`, usamos o utilitário `setcap` para conceder ao binário do Python apenas as permissões de rede necessárias.

### 1.1. Instalação Rápida (Recomendado)

Recomendamos o uso dos scripts de instalação para uma configuração mais rápida e segura:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```
2.  **Execute a Instalação:**
    ```bash
    ./install.sh
    ```
    *Este script instalará as dependências do sistema (`libpcap-dev`, `libcap2-bin`), criará um ambiente virtual e aplicará o `setcap` de forma segura.*
3.  **Execute o Aplicativo (Sem `sudo`):**
    ```bash
    ./run.sh
    ```
    *O script `run.sh` executa o Python do ambiente virtual, que já possui as capacidades de rede necessárias, sem a necessidade de `sudo`.*

### B. Configuração de Segurança Avançada (Recomendado para Desenvolvedores)

Para evitar a execução de todo o Python como `root`, você pode usar o comando `setcap` para dar permissão de rede apenas ao executável do Python dentro do ambiente virtual.

1.  **Instale as dependências e crie o ambiente virtual** (conforme o passo 1.A).
2.  **Aplique as permissões de rede:**
    \`\`\`bash
    # Assumindo que você está no diretório raiz do projeto
    sudo setcap cap_net_raw,cap_net_admin=eip venv/bin/python
    \`\`\`
    **Atenção:** O uso de `setcap` é mais seguro, mas requer que você confie no código que está executando.

3.  **Execute a aplicação sem `sudo`:**
    \`\`\`bash
    venv/bin/python -m albion_insight
    \`\`\`

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

## 3. macOS (Instalação Manual)

A instalação no macOS é manual e requer a instalação de ferramentas de desenvolvimento e privilégios de administrador.

1.  **Instale o Python:** Instale o Python 3.8+ (via Homebrew ou do site oficial).
2.  **Instale o Xcode Command Line Tools:**
    ```bash
    xcode-select --install
    ```
3.  **Instale o libpcap (necessário para o Scapy):**
    ```bash
    brew install libpcap
    ```
    *Se você não tiver o Homebrew, instale-o primeiro.*
4.  **Instale as Dependências Python:**
    ```bash
    # Crie e ative um ambiente virtual (recomendado)
    python3 -m venv venv
    source venv/bin/activate
    
    # Instale as dependências
    pip install flet scapy
    ```
5.  **Execute como Root:** A captura de pacotes requer privilégios elevados.
    ```bash
    sudo venv/bin/python3 -m albion_insight
    ```

[[Home]]
