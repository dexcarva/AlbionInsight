# Solução de Problemas Comuns

| Problema | Causa Mais Comum | Solução |
| :--- | :--- | :--- |
| **"Permission denied" ou "No interfaces found"** | O rastreamento de rede (sniffing) requer privilégios elevados. | **Linux/macOS:** Execute o aplicativo com `sudo`. Ex: `sudo venv/bin/python3 albion_insight/main.py`. **Windows:** Execute o Prompt de Comando ou PowerShell como **Administrador**. |
| **O medidor de dano não atualiza** | O filtro BPF pode estar incorreto ou o Albion Online está usando portas diferentes. | Verifique se o filtro BPF em `core/network_tracker.py` (`udp and (port 5055 or port 5056 or port 5058)`) ainda é válido. Certifique-se de que o jogo está em execução. |
| **Erro de importação de módulo** | O ambiente virtual não está ativado ou as dependências não foram instaladas. | Ative o ambiente virtual (`source venv/bin/activate`) e execute `pip install -r requirements.txt`. |
| **O aplicativo não fecha corretamente** | O *thread* de *sniffing* não foi encerrado. | A função `on_close` em `albion_insight/main.py` agora garante que o `NetworkTracker` seja parado. Se o problema persistir, verifique se o processo `scapy` foi encerrado. |
| **Problemas de UI no Linux** | Dependências do Flet/GTK ausentes. | Certifique-se de que as dependências do sistema para Flet (como `libgtk-3-dev` ou equivalentes) estejam instaladas. |
