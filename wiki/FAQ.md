# Frequently Asked Questions (FAQ)

**[Leia em Português](FAQ.pt-BR.md)**

## General Questions

### What is Albion Insight?

Albion Insight is a cross-platform statistics analysis tool for Albion Online. It tracks real-time in-game statistics such as silver earned, fame gained, and combat data by analyzing network traffic. The tool is a modern Python reimplementation of the popular AlbionOnline-StatisticsAnalysis tool, designed to work on Linux, Windows, and macOS.

### Is Albion Insight allowed by the game developers?

Yes, tools that monitor network traffic without modifying the game client or providing unfair advantages are generally allowed. Albion Insight follows the same principles as the original AlbionOnline-StatisticsAnalysis tool, which has been clarified as acceptable by the Albion Online community managers.

The tool:
- Only monitors network traffic
- Does not modify the game client
- Does not track players outside your view
- Does not provide an overlay to the game

For reference, see the [official forum discussion](https://forum.albiononline.com/index.php/Thread/124819-Regarding-3rd-Party-Software-and-Network-Traffic-aka-do-not-cheat-Update-16-45-U/).

### Is Albion Insight free?

Yes, Albion Insight is completely free and open source under the MIT License. You can use, modify, and distribute it freely.

## Installation and Setup

### Which operating systems are supported?

Albion Insight supports:
- **Linux** (Debian, Ubuntu, Fedora, Arch, and other distributions)
- **Windows** (Windows 10 and later)
- **macOS** (macOS 10.15 and later)

### Why do I need root/administrator privileges?

Network packet capture requires elevated privileges to access the network interface at a low level. This is a security feature of modern operating systems. The tool uses the Scapy library, which needs these privileges to sniff network packets.

### Can I use Albion Insight with a VPN or ExitLag?

Yes, Albion Insight should work with VPN connections and gaming proxies like ExitLag. The tool captures packets at the network interface level, so it can see traffic regardless of whether it's routed through a VPN.

### Can I use Albion Insight with GeForce NOW?

Unfortunately, no. When playing through cloud gaming services like GeForce NOW, the game runs on remote servers, and the network traffic analysis happens on those servers, not on your local machine. Albion Insight cannot capture this traffic.

## Usage Questions

### How do I start tracking my session?

After launching Albion Insight with administrator/root privileges, the tool will automatically begin capturing network traffic when you start playing Albion Online. You can use the session management controls to start, stop, reset, or save your session data.

### What statistics does Albion Insight track?

Currently, Albion Insight tracks:
- **Silver**: Money earned and spent
- **Fame**: Fame gained from various activities
- **Combat Statistics**: Damage dealt, healing done, DPS (Damage Per Second)
- **Player Events**: Kills, deaths, and other player interactions

More features are being added as the Photon Protocol decoding is expanded.

### Why isn't the damage meter showing any data?

There are several possible reasons:
1. **Privileges**: Make sure you're running the tool with root/administrator privileges
2. **Network Interface**: The tool might be listening on the wrong network interface
3. **Game Not Running**: Start Albion Online after launching Albion Insight
4. **Firewall**: Check if your firewall is blocking the tool

See the [Troubleshooting Guide](Troubleshooting.md) for more detailed solutions.

### Can I export my session data?

Yes, session data can be saved for later analysis. The export functionality is available through the session management interface. Exported data is saved in a structured format that can be opened with spreadsheet applications or analyzed programmatically.

## Technical Questions

### What is the Photon Protocol?

Albion Online uses the Photon networking engine for client-server communication. The Photon Protocol is the data format used to encode game events and state updates. Albion Insight decodes these packets to extract game statistics in real-time.

### How accurate is the damage meter?

The damage meter's accuracy depends on the completeness of the Photon Protocol event decoding. Currently, the core combat events are implemented, but some edge cases and specific abilities may not be fully tracked. The community is actively working on improving the event coverage.

### Does Albion Insight affect game performance?

No, Albion Insight runs as a separate process and only passively monitors network traffic. It does not inject code into the game or modify game files, so it should not affect game performance.

### Can I contribute to the project?

Absolutely! Albion Insight is an open-source project, and contributions are welcome. You can:
- Report bugs and suggest features
- Improve documentation
- Add support for more Photon Protocol events
- Test the tool on different platforms
- Submit code improvements

See the [Contributing Guidelines](../CONTRIBUTING.md) for more information.

## Troubleshooting

### The application won't start

1. **Check Python version**: Make sure you have Python 3.8 or later installed
2. **Check dependencies**: Ensure Flet and Scapy are installed correctly
3. **Check privileges**: Run the application with root/administrator privileges
4. **Check logs**: Look for error messages in the terminal/console output

### I'm getting permission errors

This usually means the application is not running with sufficient privileges. On Linux, use `sudo` to run the application. On Windows, run the Command Prompt or PowerShell as Administrator.

### The tool is not capturing any packets

1. **Verify game is running**: Start Albion Online
2. **Check network interface**: Make sure the tool is listening on the correct interface
3. **Check firewall settings**: Ensure your firewall isn't blocking the tool
4. **Restart the tool**: Try closing and reopening Albion Insight

For more detailed troubleshooting steps, see the [Troubleshooting Guide](Troubleshooting.md).

## Still Have Questions?

If your question isn't answered here:
1. Check the [Wiki](Home.md) for more detailed documentation
2. Search [existing issues](https://github.com/dexcarva/AlbionInsight/issues) on GitHub
3. Open a new issue with the "question" label

---

*Last updated: October 2025*
