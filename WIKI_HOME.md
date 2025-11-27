# Albion Insight Wiki - Página Principal

Bem-vindo à Wiki do **Albion Insight**, a sua ferramenta de análise de estatísticas multiplataforma para o jogo Albion Online. Este projeto é um *port* em Python do popular `AlbionOnline-StatisticsAnalysis`, focado em compatibilidade com Linux, Windows e macOS.

## 1. Sobre o Albion Insight

O Albion Insight é um aplicativo de desktop construído com **Python** e o *framework* **Flet**. Ele funciona analisando o tráfego de rede do jogo (sniffing de pacotes UDP) para extrair dados em tempo real, como:

*   **Estatísticas de Combate:** Medidor de Dano (Damage Meter), Dano Causado, Cura Realizada e DPS (Dano por Segundo).
*   **Estatísticas Financeiras:** Acompanhamento de Ganhos e Perdas de Prata (Silver).
*   **Estatísticas de Progresso:** Acompanhamento de Fama (Fame) e outros dados de progressão.

**Importante:** O uso desta ferramenta requer **privilégios de administrador/root** para a captura de pacotes de rede.

## 2. Instalação e Configuração

A instalação varia ligeiramente dependendo do seu sistema operacional.

### 2.1. Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado no seu sistema.

### 2.2. Instalação Rápida (Linux)

Para usuários de Linux, o repositório oferece *scripts* de instalação e execução simplificados:

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```
2.  **Execute a Instalação:**
    ```bash
    ./install.sh
    ```
3.  **Execute o Aplicativo:**
    ```bash
    ./run.sh
    ```

### 2.3. Instalação Manual (Windows, macOS e Linux)

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    ```
2.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute o Aplicativo:**
    ```bash
    python main.py
    ```

## 3. Solução de Problemas Comuns

| Problema Comum | Causa Potencial | Solução Sugerida |
| :--- | :--- | :--- |
| **"Permissão Negada"** ao executar | Falta de privilégios de root/administrador para o *sniffing* de pacotes. | Execute o aplicativo com `sudo` (Linux/macOS) ou como Administrador (Windows). |
| **O aplicativo não abre** (Erro de Importação) | Dependências ausentes ou versão incorreta do Python. | Verifique se o Python 3.8+ está instalado e se todas as dependências em `requirements.txt` foram instaladas corretamente. |
| **Não rastreia dados** | O jogo não está aberto ou o *sniffing* de pacotes está bloqueado pelo firewall. | Verifique se o Albion Online está rodando e se o firewall permite o tráfego nas portas 5055, 5056 e 5058. |

## 4. Tópicos Avançados

Para informações mais detalhadas sobre a arquitetura do projeto, decodificação do Protocolo Photon e diretrizes de contribuição de código, consulte a página **[Tópicos Avançados](WIKI_ADVANCED.md)**.

## 5. Próximos Passos

Para acompanhar o roadmap e as funcionalidades futuras, consulte a seção [Próximos Passos e Roadmap](WIKI_ADVANCED.md#4-próximos-passos-e-roadmap) na página de Tópicos Avançados.

## 6. Como Contribuir

O Albion Insight é um projeto de código aberto e agradecemos todas as contribuições.

*   **Reportar Bugs:** Use a seção [Issues](https://github.com/dexcarva/AlbionInsight/issues) para relatar problemas.
*   **Sugestões de Recursos:** Abra uma Issue para discutir novas funcionalidades.
*   **Contribuições de Código:** Faça um *fork* do repositório, crie uma *branch* e envie um [Pull Request](https://github.com/dexcarva/AlbionInsight/pulls) com suas alterações.
*   **Traduções:** Ajude a traduzir o `README.md` para outros idiomas.

Consulte o arquivo `CONTRIBUTING.md` no repositório para diretrizes detalhadas.
