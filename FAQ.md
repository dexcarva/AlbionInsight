# Frequently Asked Questions (FAQ) - Albion Insight

## General Questions

### Q1: What is Albion Insight?

**A:** Albion Insight is a cross-platform (Linux, Windows, macOS) statistics analysis tool for the game Albion Online. It tracks real-time in-game statistics like silver, fame, and combat data (Damage Meter) by analyzing network traffic. It's a modern, open-source alternative to the original C#/WPF-based tool.

---

### Q2: Is Albion Insight safe to use? Will I get banned?

**A:** Yes, Albion Insight is safe to use. It only analyzes network traffic and does not modify game files or inject code into the game. It's similar to other legitimate tools used by the community. However, always check the official Albion Online terms of service for the latest policies.

---

### Q3: Do I need administrator/root privileges to run Albion Insight?

**A:** Yes, network packet sniffing requires elevated privileges. You'll need to run the application with `sudo` on Linux/macOS or as Administrator on Windows.

---

### Q4: What are the system requirements?

**A:** 
- **Python:** 3.8 or higher
- **OS:** Linux, Windows, or macOS
- **RAM:** Minimum 512 MB (1 GB recommended)
- **Network:** Active internet connection to Albion Online servers

---

## Installation and Setup

### Q5: How do I install Albion Insight?

**A:** Follow the installation guide in the [README.md](README.md). We provide both quick install scripts for Linux and manual installation steps for all platforms.

---

### Q6: Can I use Albion Insight on macOS?

**A:** Yes! Albion Insight is fully compatible with macOS. Follow the manual installation steps in the README, and run the application with `sudo`.

---

### Q7: What if I get a "Permission denied" error?

**A:** This error occurs because network sniffing requires elevated privileges. Run the application with `sudo` on Linux/macOS or as Administrator on Windows. See the [TROUBLESHOOTING.md](TROUBLESHOOTING.md) guide for more details.

---

### Q8: How do I update Albion Insight?

**A:** 
1. Navigate to your Albion Insight directory.
2. Pull the latest changes:
   ```bash
   git pull origin main
   ```
3. Update dependencies:
   ```bash
   pip install -r requirements.txt --upgrade
   ```
4. Run the application again.

---

## Features and Functionality

### Q9: What statistics does Albion Insight track?

**A:** Currently, Albion Insight tracks:
- **Silver:** In-game currency earned
- **Fame:** Experience points gained
- **Damage Meter:** Real-time combat statistics (damage done, healing done, DPS)
- **Player Stats:** Individual player performance metrics

---

### Q10: Can I export my session data?

**A:** This feature is currently in development. Session data is saved locally in the `sessions/` directory. Future versions will support exporting to CSV, JSON, or other formats.

---

### Q11: Does Albion Insight work with all Albion Online servers?

**A:** Albion Insight is designed to work with the official Albion Online servers. It may not work with private servers or modified versions of the game.

---

### Q12: Can I use Albion Insight while playing in fullscreen?

**A:** Yes, Albion Insight runs as a separate application and can be displayed alongside the game. On Linux, you can use Alt+Tab to switch between windows. On Windows and macOS, you can arrange windows side-by-side or use virtual desktops.

---

## Troubleshooting

### Q13: The damage meter is not updating. What should I do?

**A:** 
1. Ensure Albion Online is running and you're in-game.
2. Check that your network interface is correctly configured.
3. Verify that the BPF filter is correct in the configuration.
4. Check the logs in `logs/app.log` for error messages.

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for more details.

---

### Q14: I see an error about "flet" module. What should I do?

**A:** This means the Flet library is not installed or not properly activated. Activate your virtual environment and reinstall dependencies:
```bash
source venv/bin/activate  # On Linux/macOS
pip install -r requirements.txt
```

---

### Q15: The application crashes on startup. How do I debug this?

**A:** 
1. Check the logs in `logs/app.log`.
2. Run the application from the terminal to see error messages:
   ```bash
   python albion_insight/main.py
   ```
3. Report the error on [GitHub Issues](https://github.com/dexcarva/AlbionInsight/issues) with the full error message and logs.

---

## Development and Contributing

### Q16: Can I contribute to Albion Insight?

**A:** Absolutely! We welcome contributions from the community. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute code, documentation, translations, or bug reports.

---

### Q17: How do I set up a development environment?

**A:** 
1. Fork the repository.
2. Clone your fork.
3. Create a virtual environment.
4. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
5. Make your changes and test them.
6. Submit a pull request.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.

---

### Q18: What programming languages does Albion Insight use?

**A:** Albion Insight is written in **Python** using the **Flet** framework for the UI and **Scapy** for network packet analysis.

---

### Q19: Can I build an executable from Albion Insight?

**A:** Yes! See the [PACKAGING.md](PACKAGING.md) guide for instructions on building standalone executables using PyInstaller.

---

## Performance and Optimization

### Q20: Why is the application using a lot of CPU?

**A:** High CPU usage can be caused by:
1. Inefficient packet processing.
2. Too frequent UI updates.
3. Running multiple instances.

Check the logs and consider optimizing the packet sniffing loop. Report performance issues on GitHub.

---

### Q21: Can I run Albion Insight on a low-end computer?

**A:** Albion Insight has modest system requirements. However, on very low-end systems, you might experience performance issues. Try:
1. Closing unnecessary applications.
2. Reducing the UI update frequency.
3. Running the application from an SSD instead of HDD.

---

## Legal and Licensing

### Q22: What is the license for Albion Insight?

**A:** Albion Insight is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

### Q23: Can I use Albion Insight commercially?

**A:** The MIT License allows commercial use, modification, and distribution. However, you must include the original license and copyright notice.

---

### Q24: Who is responsible for Albion Insight?

**A:** Albion Insight is maintained by the community. The original project was created by dexcarva as a port of the original C#/WPF tool by Triky313.

---

## Getting Help

### Q25: Where can I get help if my question isn't answered here?

**A:** 
1. Check the [TROUBLESHOOTING.md](TROUBLESHOOTING.md) guide.
2. Search existing [GitHub Issues](https://github.com/dexcarva/AlbionInsight/issues).
3. Create a new issue with a detailed description of your problem.
4. Join community discussions on Discord or forums.

---

**Last Updated:** November 13, 2025
