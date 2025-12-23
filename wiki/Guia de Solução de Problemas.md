# Guia de Solução de Problemas (FAQ)

Este guia visa responder às perguntas mais frequentes e fornecer soluções para problemas comuns encontrados ao usar o Albion Insight.

## 1. Erros de Instalação e Dependências

### 1.1. `ImportError: attempted relative import with no known parent package` (Issue #2)

**Problema:** Este erro geralmente ocorre quando você tenta executar o arquivo `main.py` diretamente (ex: `python main.py`) em vez de executá-lo como um módulo Python.

**Solução:** O Albion Insight deve ser executado como um módulo para que as importações relativas funcionem corretamente.

**No Linux/macOS:**
```bash
# Certifique-se de estar no diretório raiz do projeto
# Se estiver usando ambiente virtual:
sudo venv/bin/python3 -m albion_insight

# Se estiver usando instalação global:
sudo python3 -m albion_insight
```

**No Windows (Executar como Administrador):**
```powershell
python -m albion_insight
```

### 1.2. Falha ao instalar `scapy` ou `libpcap-dev`

**Problema:** A instalação falha no Linux com erros relacionados a `libpcap-dev` ou no Windows com erros de compilação.

**Solução (Linux):** Certifique-se de que as dependências do sistema estão instaladas. O script `install.sh` tenta fazer isso automaticamente, mas você pode tentar manualmente:
```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```
*(Para outras distribuições, substitua `apt install` pelo seu gerenciador de pacotes, como `dnf install` ou `pacman -S`.)*

**Solução (Windows):** Certifique-se de que você tem o **WinPcap** ou **Npcap** instalado, que são necessários para a captura de pacotes no Windows.

## 2. Problemas de Execução e Interface

### 2.1. Tela Branca ou Interface Não Carrega no Linux (Issue #1)

**Problema:** Após a execução, a janela do aplicativo aparece, mas a interface fica em branco ou não responde. Isso é comum em algumas distribuições Linux LTS (Long-Term Support) devido a problemas de compatibilidade com o framework Flet/Flutter.

**Solução:**

1.  **Verifique a execução como módulo:** Certifique-se de que está executando o aplicativo como um módulo (veja 1.1).
2.  **Verifique as permissões:** A captura de pacotes requer permissões elevadas. Se você não usou o `setcap` (via `install.sh`), tente executar com `sudo`.
3.  **Atualize o Flet:** Tente atualizar o Flet para a versão mais recente dentro do seu ambiente virtual:
    ```bash
    source venv/bin/activate
    pip install --upgrade flet
    ```
4.  **Problema de GPU/Driver:** Em casos raros, pode ser um problema de driver de GPU. Tente executar com a flag `--web` para usar a interface no navegador (se suportado pelo Flet na versão atual) ou procure por logs de erro no terminal.

### 2.2. O aplicativo não está capturando dados (Silver, Fame, etc.)

**Problema:** O aplicativo inicia, mas os valores de estatísticas permanecem em zero ou não se atualizam.

**Solução:**

1.  **Execute como Root/Administrador:** A captura de pacotes de rede **sempre** requer privilégios elevados. Certifique-se de que o aplicativo está sendo executado com `sudo` (Linux/macOS) ou como Administrador (Windows).
2.  **Verifique as Portas:** O Albion Insight monitora as portas 5055, 5056 e 5058 (UDP). Certifique-se de que seu firewall não está bloqueando o tráfego nessas portas.
3.  **Verifique a Interface de Rede:** Em ambientes com múltiplas interfaces de rede (VPNs, máquinas virtuais), o Scapy pode estar monitorando a interface errada. Verifique se há uma opção de configuração para especificar a interface de rede no arquivo de configuração do Albion Insight (se existir).

## 3. Contribuição e Desenvolvimento

### 3.1. Como posso contribuir com traduções?

**Resposta:** Fico feliz com seu interesse! Você pode contribuir com traduções seguindo estes passos:

1.  **Fork** o repositório.
2.  Crie um novo arquivo `README.xx-YY.md` (onde `xx-YY` é o código do seu idioma, ex: `pt-PT` para Português Europeu) baseado no `README.md` principal.
3.  Traduza o conteúdo.
4.  Abra um **Pull Request** com suas alterações.

Consulte o [Guia de Contribuição Geral](Guia de Contribuição Geral.md) para mais detalhes.

[[Home]]
