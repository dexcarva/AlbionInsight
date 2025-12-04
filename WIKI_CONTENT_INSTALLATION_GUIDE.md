# Guia de Instalação Segura no Linux

Este guia detalha o processo de instalação do Albion Insight no Linux, com foco nas melhores práticas de segurança para a captura de pacotes de rede.

## 1. O Desafio da Captura de Pacotes

O Albion Insight utiliza a biblioteca `Scapy` para "farejar" (sniff) o tráfego de rede do jogo Albion Online. A captura de pacotes brutos (raw packets) é uma operação de baixo nível que, por padrão, exige **privilégios de root** (superusuário) no Linux.

A prática de executar um aplicativo inteiro como `root` é considerada uma **má prática de segurança**, pois um erro ou vulnerabilidade no código poderia comprometer todo o sistema operacional.

## 2. A Solução: Capacidades de Rede (`setcap`)

Para resolver este problema, o Albion Insight utiliza o utilitário `setcap` (set capabilities) durante a instalação. O `setcap` permite conceder permissões específicas a um arquivo executável sem conceder-lhe todos os privilégios de `root`.

Ao invés de executar o Python como `sudo`, nós concedemos ao executável do Python dentro do ambiente virtual apenas as capacidades necessárias para a captura de rede:

*   `cap_net_raw`: Permite o uso de sockets de pacotes brutos (raw sockets).
*   `cap_net_admin`: Permite operações de administração de rede.

### 2.1. O que o `install.sh` faz

O script de instalação automatizado (`install.sh`) agora inclui os seguintes passos de segurança:

1.  Instala o pacote `libcap2-bin` (que contém o `setcap`).
2.  Após instalar as dependências do Python no ambiente virtual (`venv`), ele executa o comando:
    \`\`\`bash
    sudo setcap 'cap_net_raw,cap_net_admin=eip' venv/bin/python3
    \`\`\`
    Este comando aplica as capacidades de rede diretamente ao binário do Python dentro do seu ambiente virtual.

## 3. Como Executar de Forma Segura

Graças ao `setcap`, você **não precisa mais** usar `sudo` para executar o Albion Insight.

1.  **Certifique-se de ter executado o `./install.sh` pelo menos uma vez.**
2.  Use o script de execução:
    \`\`\`bash
    ./run.sh
    \`\`\`

O script `run.sh` simplesmente executa:

\`\`\`bash
./venv/bin/python3 -m albion_insight
\`\`\`

Como o binário `venv/bin/python3` já possui as capacidades de rede necessárias, o aplicativo pode capturar pacotes com segurança, rodando com o seu usuário normal.

---
*Esta é uma melhoria de segurança crucial para o projeto, garantindo que você possa usar o Albion Insight sem comprometer a segurança do seu sistema.*
