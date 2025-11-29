# Troubleshooting Guide - Albion Insight

## Common Issues and Solutions

### 1. Permission Denied or "No interfaces found"

**Problem:** You see an error message like "Permission denied" or "No interfaces found" when trying to run the application.

**Cause:** Network packet sniffing requires elevated privileges (root/administrator access).

**Solution:**
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

### 2. Damage Meter Not Updating

**Problem:** The damage meter shows no data or doesn't update in real-time.

**Cause:** The BPF filter may be incorrect, or Albion Online is not running, or using different ports.

**Solution:**
1. Ensure Albion Online is running and you're in-game.
2. Check if the BPF filter in `albion_insight/core/network_tracker.py` (executado pelo sniffer) está correto:
   ```
   udp and (port 5055 or port 5056 or port 5058)
   ```
3. Verify your network interface is correct in the configuration.
4. Check the logs in `logs/app.log` for detailed error messages.

---

### 3. Module Import Error

**Problem:** You see an error like `ModuleNotFoundError: No module named 'flet'` or similar.

**Cause:** The virtual environment is not activated or dependencies are not installed.

**Solution:**
1. Activate the virtual environment:
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### 4. Application Doesn't Close Properly

**Problem:** The application hangs when you try to close it, ou o processo do sniffer não é encerrado.

**Cause:** O subprocesso do sniffer (que roda com privilégios elevados) não foi encerrado corretamente pelo `SnifferManager`.

**Solution:**
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

### 5. UI Issues on Linux

**Problem:** The application window is blank, doesn't render properly, or crashes on Linux.

**Cause:** Missing system dependencies for Flet/GTK.

**Solution:**
Install the required system libraries:

```bash
# For Debian/Ubuntu
sudo apt update
sudo apt install libgtk-3-dev libglib2.0-dev

# For Fedora/RHEL
sudo dnf install gtk3-devel glib2-devel

# For Arch
sudo pacman -S gtk3 glib2
```

Then reinstall Flet:
```bash
pip install --upgrade flet
```

---

### 6. Flet Version Compatibility Issues

**Problem:** You see errors like `AttributeError: module 'flet' has no attribute 'icons'`.

**Cause:** The installed Flet version has breaking changes or incompatibilities.

**Solution:**
1. Check your Flet version:
   ```bash
   pip show flet
   ```

2. Update to the latest compatible version:
   ```bash
   pip install --upgrade flet==0.28.3
   ```

3. If issues persist, try a different version:
   ```bash
   pip install flet==0.27.0
   ```

---

### 7. Network Interface Not Found

**Problem:** The application can't find your network interface.

**Cause:** The configured interface name is incorrect or doesn't exist.

**Solution:**
1. List available network interfaces:
   - **Linux/macOS:**
     ```bash
     ifconfig
     # or
     ip link show
     ```
   - **Windows:**
     ```bash
     ipconfig
     ```

2. Update the `NETWORK_INTERFACE` in `.env` or `albion_insight/utils/config.py` with the correct interface name.

---

### 8. High CPU Usage

**Problem:** The application uses excessive CPU resources.

**Cause:** The packet sniffing loop is running too frequently or processing packets inefficiently.

**Solution:**
1. Check the sniffing loop in `albion_insight/core/network_tracker.py`.
2. Add delays or optimize packet processing.
3. Consider using a more efficient packet capture method.

---

### 9. Data Not Saving

**Problem:** Session data is not being saved to disk.

**Cause:** The session directory doesn't exist or there are permission issues.

**Solution:**
1. Ensure the `sessions/` directory exists:
   ```bash
   mkdir -p sessions
   ```

2. Check directory permissions:
   ```bash
   chmod 755 sessions/
   ```

3. Verify the `SESSION_DIR` configuration in `.env` or `albion_insight/utils/config.py`.

---

### 10. Logging Issues

**Problem:** Log files are not being created or logs are not appearing.

**Cause:** The `logs/` directory doesn't exist or logger is not properly configured.

**Solution:**
1. Ensure the `logs/` directory exists:
   ```bash
   mkdir -p logs
   ```

2. Check the logger configuration in `albion_insight/utils/logger.py`.

3. Verify the `LOG_DIR` and `LOG_LEVEL` settings in `.env`.

---

## Getting Help

If you encounter an issue not listed here:

1. **Check the logs:** Look at `logs/app.log` for detailed error messages.
2. **Search existing issues:** Visit [GitHub Issues](https://github.com/dexcarva/AlbionInsight/issues).
3. **Create a new issue:** Provide:
   - Your operating system and version
   - Python version
   - Flet version
   - Steps to reproduce the issue
   - Error messages and logs
   - Screenshots if applicable

---

**Last Updated:** November 29, 2025
