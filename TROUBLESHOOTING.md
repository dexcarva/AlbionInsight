# Guia de Solução de Problemas - Albion Insight

## Problemas Comuns e Soluções

### 1. Permissão Negada ou "Nenhuma interface encontrada"

**Problema:** Você vê uma mensagem de erro como "Permission denied" ou "No interfaces found" ao tentar executar a aplicação.

**Causa:** A captura de pacotes de rede requer privilégios elevados (acesso de root/administrador).

**Solução:**
- **Linux/macOS:** A aplicação agora solicitará privilégios de root/administrador apenas para o processo de captura de pacotes. Execute a aplicação normalmente:
  ```bash
  venv/bin/python3 -m albion_insight
  ```
  Ou use o script:
  ```bash
  ./run.sh
  ```
  Se o problema persistir, verifique se o `sudo` está configurado corretamente.

- **Windows:** A aplicação solicitará privilégios de administrador. Se o problema persistir, certifique-se de que o Prompt de Comando ou PowerShell não está sendo executado como Administrador, pois a aplicação fará a solicitação internamente.

---

### 2. Medidor de Dano Não Atualiza

**Problema:** O medidor de dano não mostra dados ou não atualiza em tempo real.

**Causa:** O filtro BPF pode estar incorreto, o Albion Online não está em execução ou está usando portas diferentes.

**Solução:**
1. Certifique-se de que o Albion Online está em execução e você está no jogo.
2. Verifique se o filtro BPF em `albion_insight/core/network_tracker.py` (executado pelo sniffer) está correto:
   ```
   udp and (port 5055 or port 5056 or port 5058)
   ```
3. Verifique se sua interface de rede está correta na configuração.
4. Verifique os logs em `logs/app.log` para mensagens de erro detalhadas.

---

### 3. Erro de Importação de Módulo

**Problema:** Você vê um erro como `ModuleNotFoundError: No module named 'flet'` ou similar.

**Causa:** O ambiente virtual não está ativado ou as dependências não estão instaladas.

**Solução:**
1. Ative o ambiente virtual:
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

### 4. Aplicação Não Fecha Corretamente

**Problema:** A aplicação trava quando você tenta fechá-la, ou o processo do sniffer não é encerrado.

**Causa:** O subprocesso do sniffer (que roda com privilégios elevados) não foi encerrado corretamente pelo `SnifferManager`.

**Solução:**
1. O `SnifferManager` deve lidar com o encerramento do subprocesso. Verifique os logs para erros no encerramento.
2. Se o problema persistir, encerre manualmente os processos:
   - **Linux/macOS:**
     ```bash
     sudo pkill -f "python.*sniffer_process"
     pkill -f "python.*albion_insight"
     ```
   - **Windows:**
     ```bash
     taskkill /IM python.exe /F
     ```

---

### 5. Problemas de UI no Linux

**Problema:** A janela da aplicação está em branco, não renderiza corretamente ou trava no Linux.

**Causa:** Dependências de sistema ausentes para Flet/GTK.

**Solução:**
Instale as bibliotecas de sistema necessárias:

```bash
# Para Debian/Ubuntu
sudo apt update
sudo apt install libgtk-3-dev libglib2.0-dev

# Para Fedora/RHEL
sudo dnf install gtk3-devel glib2-devel

# Para Arch
sudo pacman -S gtk3 glib2
```

Em seguida, reinstale o Flet:
```bash
pip install --upgrade flet
```

---

### 6. Problemas de Compatibilidade de Versão do Flet

**Problema:** Você vê erros como `AttributeError: module 'flet' has no attribute 'icons'`.

**Causa:** A versão instalada do Flet possui alterações incompatíveis.

**Solução:**
1. Verifique sua versão do Flet:
   ```bash
   pip show flet
   ```

2. Atualize para a versão compatível mais recente:
   ```bash
   pip install --upgrade flet==0.28.3
   ```

3. Se os problemas persistirem, tente uma versão diferente:
   ```bash
   pip install flet==0.27.0
   ```

---

### 7. Interface de Rede Não Encontrada

**Problema:** A aplicação não consegue encontrar sua interface de rede.

**Causa:** O nome da interface configurada está incorreto ou não existe.

**Solução:**
1. Liste as interfaces de rede disponíveis:
   - **Linux/macOS:**
     ```bash
     ifconfig
     # ou
     ip link show
     ```
   - **Windows:**
     ```bash
     ipconfig
     ```

2. Atualize o `NETWORK_INTERFACE` em `.env` ou `albion_insight/utils/config.py` com o nome correto da interface.

---

### 8. Alto Uso de CPU

**Problema:** A aplicação usa recursos excessivos da CPU.

**Causa:** O loop de captura de pacotes está sendo executado com muita frequência ou processando pacotes de forma ineficiente.

**Solução:**
1. Verifique o loop de *sniffing* em `albion_insight/core/network_tracker.py`.
2. Adicione atrasos ou otimize o processamento de pacotes.
3. Considere usar um método de captura de pacotes mais eficiente.

---

### 9. Dados Não Estão Sendo Salvos

**Problema:** Os dados da sessão não estão sendo salvos no disco.

**Causa:** O diretório de sessões não existe ou há problemas de permissão.

**Solução:**
1. Garanta que o diretório `sessions/` exista:
   ```bash
   mkdir -p sessions
   ```

2. Verifique as permissões do diretório:
   ```bash
   chmod 755 sessions/
   ```

3. Verifique a configuração de `SESSION_DIR` em `.env` ou `albion_insight/utils/config.py`.

---

### 10. Problemas de Logging

**Problema:** Os arquivos de log não estão sendo criados ou os logs não estão aparecendo.

**Causa:** O diretório `logs/` não existe ou o logger não está configurado corretamente.

**Solução:**
1. Garanta que o diretório `logs/` exista:
   ```bash
   mkdir -p logs
   ```

2. Verifique a configuração do logger em `albion_insight/utils/logger.py`.

3. Verifique as configurações de `LOG_DIR` e `LOG_LEVEL` em `.env`.

---

## Obtendo Ajuda

Se você encontrar um problema não listado aqui:

1. **Verifique os logs:** Procure em `logs/app.log` por mensagens de erro detalhadas.
2. **Pesquise Issues existentes:** Visite [GitHub Issues](https://github.com/dexcarva/AlbionInsight/issues).
3. **Crie uma nova Issue:** Forneça:
   - Seu sistema operacional e versão
   - Versão do Python
   - Versão do Flet
   - Passos para reproduzir o problema
   - Mensagens de erro e logs
   - Capturas de tela, se aplicável

---

**Última Atualização:** 30 de Novembro de 2025
