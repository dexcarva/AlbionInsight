# 贡献指南 (Contributing Guidelines)

我们非常欢迎社区对 **Albion Insight** 项目的贡献！您的帮助对于使这个工具对所有 Albion Online 玩家更有用至关重要。

请花一些时间阅读以下指南，以确保您的贡献能够顺利地被整合到项目中。

## 行为准则 (Code of Conduct)

请注意，本项目及其参与者受 [行为准则](CODE_OF_CONDUCT.md) 约束。通过参与，您同意遵守其条款。

## 如何贡献 (How to Contribute)

有几种方式可以为 Albion Insight 做出贡献：

### 1. 报告 Bug (Reporting Bugs)

如果您发现了一个 Bug，请首先检查 [Issues](https://github.com/dexcarva/AlbionInsight/issues) 列表，看是否已经有人报告了。如果没有，请创建一个新的 Issue，并提供以下信息：

*   **清晰且描述性的标题。**
*   **重现 Bug 的步骤。**
*   **您正在使用的 Albion Insight 版本。**
*   **您的操作系统和 Python 版本。**
*   **任何相关的错误消息或截图。**

### 2. 建议新功能 (Suggesting Enhancements)

我们欢迎任何改进项目的新功能或建议。请在 [Issues](https://github.com/dexcarva/AlbionInsight/issues) 中提出您的建议，并描述：

*   **您希望添加的功能。**
*   **为什么这个功能对项目有价值。**
*   **如果可能，提供一个实现该功能的潜在方法。**

### 3. 代码贡献 (Code Contributions)

如果您想直接贡献代码，请遵循以下步骤：

1.  **Fork** 仓库：[github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  **克隆** 您的 Fork：`git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  **创建新分支**：`git checkout -b feature/your-feature-name` 或 `fix/your-bug-fix`
4.  **设置开发环境**：
    *   确保您已安装 [先决条件](#先决条件-prerequisites)。
    *   安装依赖项：`pip install -r requirements.txt`
5.  **进行更改**：
    *   请确保您的代码遵循 **PEP 8** 风格指南。
    *   对于新功能，请考虑添加或更新相关的文档。
6.  **测试**：在提交之前，请确保您的更改没有引入新的 Bug，并且应用程序可以正常运行。
7.  **提交更改**：使用清晰且描述性的提交信息。我们推荐使用 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) 规范（例如：`feat: 添加新功能`，`fix: 修复一个 Bug`）。
8.  **推送到您的 Fork**：`git push origin your-branch-name`
9.  **打开 Pull Request (PR)**：
    *   确保您的 PR 目标是 `main` 分支。
    *   在 PR 描述中，清晰地解释您的更改内容和原因。
    *   如果您的 PR 解决了某个 Issue，请在描述中提及它（例如：`Closes #123`）。

### 4. 文档和翻译 (Documentation and Translation)

文档对于项目的成功至关重要。如果您发现文档有任何错误、遗漏或可以改进的地方，请随时提交 PR。

我们特别欢迎对 **README** 和 **CONTRIBUTING** 文件进行新的语言翻译。如果您想添加一种新的语言：

1.  复制 `README.md` 或 `CONTRIBUTING.md`。
2.  将其命名为 `README.xx-YY.md` 或 `CONTRIBUTING.xx-YY.md`，其中 `xx-YY` 是语言代码（例如：`zh-CN` 代表简体中文）。
3.  将内容翻译成目标语言。
4.  在主 `README.md` 中添加指向您的新翻译文件的链接。

## 感谢您的贡献！ (Thank You for Contributing!)
