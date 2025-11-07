# Albion Insight

**Uma ferramenta de análise de estatísticas de rede *cross-platform* para Albion Online, baseada no projeto original de Triky313.**

O Albion Insight é um *port* em Python do popular **AlbionOnline-StatisticsAnalysis** de Triky313, que originalmente só funcionava no Windows. Nosso objetivo é fornecer uma solução *cross-platform* (Linux, Windows e macOS) para a comunidade de Albion Online, permitindo a análise de dados em tempo real através da captura de pacotes de rede.

## Funcionalidades Principais
*   **Compatibilidade *Cross-Platform***: Desenvolvido em Python com `Flet`, garantindo que funcione em Linux, Windows e macOS.
*   **Rastreamento em Tempo Real**: Utiliza a biblioteca `Scapy` para farejar pacotes UDP nas portas do Albion Online (5055, 5056, 5058).
*   **Estrutura de Medidor de Dano**: Inclui as estruturas de dados e a interface de usuário necessárias para exibir estatísticas de combate em tempo real (Dano Causado, Cura Realizada, DPS).
*   **Interface Moderna**: Construído com Flet, proporcionando uma aplicação de desktop rápida e com aparência nativa.
*   **Gerenciamento de Sessão**: Permite iniciar, parar, redefinir e salvar estatísticas de sessão.

## Pré-requisitos
*   Python 3.8+
*   Bibliotecas **Flet** e **Scapy**.
*   **Privilégios de Root/Administrador**: Necessários para a captura de pacotes de rede.

## Instalação e Configuração
### Opção 1: Instalação Rápida (Linux - Recomendado)
Para usuários Linux, fornecemos *scripts* de instalação automatizada:
```bash
# 1. Clone o repositório
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight
# 2. Execute o script de instalação
./install.sh
# 3. Execute a aplicação
./run.sh
```
O *script* `install.sh` irá:
- Instalar dependências do sistema (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Criar um ambiente virtual Python
- Instalar todos os pacotes Python necessários (Flet, Scapy)
O *script* `run.sh` solicitará automaticamente privilégios de *root* e executará a aplicação.

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
# Crie o ambiente virtual
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

#### 3. Executando a Aplicação
Como a captura de rede requer privilégios elevados, você deve executar a aplicação como *root* ou administrador.
**No Linux (com ambiente virtual):**
```bash
sudo venv/bin/python3 albion_insight.py
```
**No Linux (instalação em todo o sistema):**
```bash
sudo python3 albion_insight.py
```
**No Windows (Execute o Prompt de Comando/PowerShell como Administrador):**
```bash
python albion_insight.py
```
A aplicação será aberta em uma janela de desktop nativa.

## Como Construir um Executável
A aplicação pode ser empacotada em um executável *standalone* usando **PyInstaller**. Isso permite que os usuários executem a aplicação sem instalar o Python ou suas dependências.
Para instruções detalhadas sobre a construção de executáveis para Linux, Windows e macOS, consulte o guia **[PACKAGING.md](PACKAGING.md)**.

### Construção Rápida (Linux)
```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight.py
```
O executável estará localizado na pasta `dist/`.

## Estrutura do Projeto
Toda a aplicação está contida em um único arquivo para simplificar:
| Arquivo | Descrição |
| :--- | :--- |
| `albion_insight.py` | O arquivo principal da aplicação contendo toda a lógica (Modelos, Rastreador de Rede, Interface Flet). |
| `README.md` | Este arquivo de documentação (em Inglês). |
| `README.pt-br.md` | Este arquivo de documentação (em Português do Brasil). |

## Status Atual (Dados em Tempo Real)
A aplicação agora inclui a **Lógica de Decodificação do Protocolo Photon**, traduzida do projeto original em C#. Isso permite que a aplicação processe eventos em tempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` diretamente do tráfego de rede.
**Nota**: A tradução completa de cada evento de combate (como `CastHit`, `Attack`) é um esforço contínuo. A implementação atual foca nas estatísticas centrais e na estrutura para o Medidor de Dano. O cálculo de DPS do Medidor de Dano é baseado nos eventos decodificados.

## Contribuições
Aceitamos contribuições da comunidade! Seja você um desenvolvedor, designer ou apenas um entusiasta de Albion Online, há muitas maneiras de ajudar a melhorar o Albion Insight.
Por favor, leia nossas [Diretrizes de Contribuição](CONTRIBUTING.md) para informações detalhadas sobre como contribuir para este projeto.

### Início Rápido para Contribuidores:
1.  Faça um *fork* do repositório: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone seu *fork*: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Crie um novo *branch*: `git checkout -b feature/seu-nome-da-feature`
4.  Faça suas alterações e *commit*: `git commit -m "Adicione sua feature"`
5.  Envie para o seu *fork*: `git push origin feature/seu-nome-da-feature`
6.  Abra um *Pull Request* no repositório principal

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Agradecimentos
- Projeto Original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) por Triky313
- Construído com o *framework* [Flet](https://flet.dev/)
- Análise de rede alimentada por [Scapy](https://scapy.net/)

---
*Uma solução cross-platform para a comunidade de Albion Online.*
