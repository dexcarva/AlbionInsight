# Solução de Problemas Comuns (Troubleshooting)

Este guia visa ajudar a resolver os problemas mais comuns que você pode encontrar ao usar ou desenvolver o Albion Insight.

## 1. Problemas de Permissão (Sniffing)

**Problema:** O aplicativo falha ao iniciar a captura de pacotes com erros como `Permission denied` ou `No interfaces found`.

**Causa:** A biblioteca `scapy` (usada para rastreamento de rede) requer privilégios elevados para acessar a interface de rede.

**Solução:**
*   **Linux/macOS:** Execute o aplicativo com `sudo`.
    ```bash
    sudo python3 albion_insight/main.py
    ```
*   **Windows:** Execute o Prompt de Comando ou PowerShell como **Administrador**.

## 2. O Medidor de Dano Não Atualiza

**Problema:** O aplicativo inicia, mas as estatísticas (dano, prata, fama) permanecem em zero ou não mudam.

**Causas Possíveis:**
1.  **Interface de Rede Incorreta:** O aplicativo está monitorando a interface de rede errada.
2.  **Filtro BPF Desatualizado:** O Albion Online mudou as portas de comunicação.
3.  **Problema de Decodificação:** O protocolo Photon foi atualizado e o decodificador não consegue mais interpretar os pacotes.

**Soluções:**
1.  **Verifique a Interface:** Edite o arquivo `.env` (ou `.env.example`) e defina a variável `NETWORK_INTERFACE` para o nome correto da sua interface (ex: `eth0`, `Wi-Fi`).
2.  **Verifique as Portas:** Confirme se as portas UDP 5055, 5056 e 5058 ainda são as usadas pelo Albion Online.
3.  **Verifique o Log:** Defina `LOG_LEVEL=DEBUG` no seu `.env` e verifique o arquivo de log (`logs/app.log`) para ver se os pacotes estão sendo capturados e se há erros de decodificação.

## 3. Erro de Importação Relativa

*   **Erro de Importação Relativa (`ImportError: attempted relative import with no known parent package`)**
    *   **Causa:** Este erro ocorre quando se tenta executar o arquivo principal (`albion_insight/main.py`) diretamente, pois ele usa importações relativas que só funcionam quando o módulo é executado como parte de um pacote.
    *   **Solução:** Em vez de usar `sudo venv/bin/python3 albion_insight/main.py`, execute o módulo como um pacote a partir do diretório raiz do projeto (`AlbionInsight`) usando a flag `-m`:
        ```bash
        sudo venv/bin/python3 -m albion_insight
        ```
    *   **Observação:** O script de execução (`run.sh`) foi atualizado para usar o comando correto, mas esta informação é útil para quem executa manualmente.

## 4. Erros de Dependência

**Problema:** Erros como `ModuleNotFoundError` ou problemas de versão ao iniciar.

**Causa:** As dependências não foram instaladas corretamente ou o ambiente virtual não está ativo.

**Solução:**
1.  **Ative o Ambiente Virtual:**
    ```bash
    source venv/bin/activate  # Linux/macOS
    ```
2.  **Reinstale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## 5. Problemas de UI (Flet)

**Problema:** A interface do usuário não é exibida corretamente ou trava no Linux.

**Causa:** Dependências do sistema para o Flet (que usa Flutter) estão ausentes.

**Solução:**
*   **Instale as Dependências do Flutter:** Em distribuições baseadas em Debian/Ubuntu, você pode precisar de pacotes como `libgtk-3-dev` ou outros pacotes de desenvolvimento. Consulte a documentação oficial do Flet/Flutter para as dependências do seu sistema operacional.

## 6. O Aplicativo Não Fecha

**Problema:** Ao fechar a janela, o processo Python continua em execução.

**Causa:** O *thread* de captura de pacotes (`scapy`) não foi encerrado corretamente.

**Solução:**
*   **Verifique o Código:** Certifique-se de que a função de fechamento da UI (no `albion_insight/ui/app.py`) chame o método de parada do `NetworkTracker` para encerrar o *thread* de *sniffing* de forma limpa.
*   **Encerramento Manual:** Se o problema persistir, você pode precisar encerrar o processo manualmente (ex: `killall python3` ou usar o Gerenciador de Tarefas no Windows).

---

*Última atualização: Novembro de 2025*
