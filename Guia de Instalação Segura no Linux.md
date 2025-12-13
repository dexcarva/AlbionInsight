# Guia de Instalação Segura no Linux

Este guia detalha o método de instalação recomendado para usuários Linux, focando na segurança ao evitar a execução do aplicativo com privilégios de `root` o tempo todo.

## 1. Pré-requisitos

Certifique-se de ter o Python 3.8+ e as ferramentas básicas de desenvolvimento instaladas.

\`\`\`bash
sudo apt update
sudo apt install -y libpcap-dev python3-pip python3-venv
\`\`\`

## 2. Clonagem e Configuração do Ambiente

1.  **Clone o repositório:**
    \`\`\`bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    \`\`\`

2.  **Crie e ative o ambiente virtual:**
    \`\`\`bash
    python3 -m venv venv
    source venv/bin/activate
    \`\`\`

3.  **Instale as dependências:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

## 3. Configuração de Segurança com `setcap` (Recomendado)

A captura de pacotes de rede requer privilégios especiais. Em vez de usar `sudo` para rodar o aplicativo inteiro, o comando `setcap` permite conceder a capacidade de `cap_net_raw` (captura de rede bruta) apenas ao executável Python dentro do seu ambiente virtual.

1.  **Localize o executável Python:**
    \`\`\`bash
    PYTHON_EXECUTABLE=$(realpath venv/bin/python)
    echo "Executável Python: $PYTHON_EXECUTABLE"
    \`\`\`

2.  **Aplique a capacidade `cap_net_raw`:**
    \`\`\`bash
    sudo setcap cap_net_raw+eip $PYTHON_EXECUTABLE
    \`\`\`
    *Isso permite que o executável Python leia pacotes de rede sem precisar de `sudo`.*

## 4. Execução do Aplicativo

Com a configuração `setcap`, você pode executar o Albion Insight como um usuário normal, dentro do ambiente virtual, mantendo a segurança do sistema.

\`\`\`bash
source venv/bin/activate
python -m albion_insight
\`\`\`

## 5. Revertendo a Configuração

Se precisar remover a capacidade `cap_net_raw` do executável Python:

\`\`\`bash
sudo setcap -r $PYTHON_EXECUTABLE
\`\`\`
