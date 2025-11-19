# Albion Insight - 項目概覽 (Project Overview)

**Albion Insight** 是一個開源且跨平台的統計分析工具，使用 **Python** 和 **Flet** 框架開發，專門為 **Albion Online** 遊戲社區服務。其目的是通過分析遊戲的網絡流量，實時追蹤和顯示統計數據，例如戰鬥數據（傷害計量器）、銀幣和聲望收益。

該項目代表了對原始 C# 項目 (`AlbionOnline-StatisticsAnalysis`) 的現代化和移植工作，旨在克服平台限制並促進社區協作。

## 🎯 主要目標 (Main Objectives)

1.  **可移植性 (Portability):** 確保在 Linux、Windows 和 macOS 上原生運行。
2.  **透明度 (Transparency):** 成為一個開源且可審計的替代方案。
3.  **功能性 (Functionality):** 提供精確的傷害計量器和可靠的會話統計追蹤器。
4.  **模塊化 (Modularity):** 保持代碼結構清晰和模塊化，以便於維護和貢獻。

## 🗺️ Wiki 地圖 (Wiki Map)

項目 Wiki 是您理解、使用和貢獻 Albion Insight 的完整指南。

| 區塊 (Section) | 描述 (Description) | 狀態 (Status) |
| :--- | :--- | :--- |
| **[使用指南](Usage-Guide.md)** | 關於如何安裝、配置和使用應用程序的逐步說明。 | ✅ 完成 |
| **[安裝指南](Installation-Guide.md)** | 不同操作系統的先決條件和安裝方法的詳細信息。 | ✅ 完成 |
| **[項目架構概覽](Architecture-Overview.md)** | 代碼結構、模塊和數據流的概覽。 | ✅ 完成 |
| **[Photon 協議解碼](Photon-Protocol-Decoding.md)** | 關於 Albion Online 網絡流量如何被解碼的技術解釋。 | ✅ 完成 |
| **[常見問題 (FAQ)](FAQ.md)** | 社區最常見問題的答案。 | ✅ 完成 |
| **[貢獻指南](Contribution-Guide.md)** | 如何設置開發環境、代碼標準和 Pull Request 流程。 | ✅ 完成 |
| **[故障排除](Troubleshooting.pt-BR.md)** | 常見錯誤和配置問題的解決方案。 | ✅ 完成 |
| **[路線圖](Roadmap.md)** | 計劃中的功能和項目的未來。 | ✅ 完成 |

## 🛠️ 技術細節 (Technical Details)

Albion Insight 基於以下技術構建：

*   **語言 (Language):** Python 3.8+
*   **圖形界面 (Graphical Interface):** [Flet](https://flet.dev/) (用於原生和跨平台的 UI)
*   **網絡分析 (Network Analysis):** [Scapy](https://scapy.net/) (用於數據包捕獲和操作)
*   **協議 (Protocol):** 實現了 Albion Online **Photon** 協議的解碼。

---
*最後更新: 2025年11月19日*
