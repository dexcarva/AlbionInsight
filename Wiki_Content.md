# Wiki do Projeto Albion Insight

## 1. Como Contribuir

Agradecemos o seu interesse em contribuir para o Albion Insight! Sua ajuda é fundamental para o sucesso e a evolução deste projeto.

### 1.1. Reportando Bugs

Se você encontrar um bug, por favor, siga estas etapas:
1.  Verifique se o bug já foi reportado nas [Issues](https://github.com/dexcarva/AlbionInsight/issues).
2.  Se não foi, abra uma nova Issue.
3.  Use o template de bug e preencha todos os campos, incluindo:
    *   **Passos para Reproduzir:** Descreva exatamente como o bug acontece.
    *   **Comportamento Esperado:** O que deveria ter acontecido.
    *   **Comportamento Atual:** O que realmente aconteceu.
    *   **Seu Ambiente:** Sistema Operacional, Versão do Python, etc.

### 1.2. Sugerindo Novas Funcionalidades

1.  Abra uma nova Issue.
2.  Use o template de sugestão de funcionalidade.
3.  Descreva a funcionalidade em detalhes e explique por que ela seria útil para a comunidade.

### 1.3. Contribuições de Código

1.  Faça um *fork* do repositório.
2.  Crie um novo *branch* para sua funcionalidade ou correção (`git checkout -b feature/minha-nova-feature` ou `git checkout -b fix/correcao-do-bug`).
3.  Instale as dependências e o `black` para formatação de código.
4.  Certifique-se de que seu código segue o estilo do projeto (use `black albion_insight`).
5.  Crie um Pull Request (PR) claro e conciso, referenciando a Issue que ele resolve (ex: `fix: Corrige o bug #123`).

## 2. Perguntas Frequentes (FAQ)

### P: O Albion Insight é seguro? Posso ser banido por usá-lo?

**R:** Sim, o Albion Insight é seguro. Ele funciona apenas lendo o tráfego de rede do jogo, o que é permitido pela política de terceiros da Sandbox Interactive (desenvolvedora do Albion Online). Ele não injeta código, não modifica arquivos do jogo e não automatiza ações. **Use por sua conta e risco**, mas a comunidade o considera seguro.

### P: Por que preciso de privilégios de Root/Administrador?

**R:** A ferramenta utiliza a biblioteca `Scapy` para "farejar" (sniffing) pacotes de rede. A captura de pacotes brutos é uma operação de baixo nível que, por padrão, requer permissões elevadas (Root no Linux/macOS, Administrador no Windows) para proteger o sistema contra uso malicioso.

### P: O Damage Meter está 100% preciso?

**R:** O Damage Meter está em desenvolvimento contínuo. Ele decodifica eventos do protocolo Photon traduzidos do projeto original em C#. Eventos como `UpdateMoney` e `UpdateFame` são precisos. No entanto, a decodificação completa de **todos** os eventos de combate (como `CastHit`, `Attack`) é um esforço contínuo. A precisão melhora a cada atualização.

### P: Como posso construir um executável para não precisar do Python?

**R:** Você pode usar o `PyInstaller`. As instruções detalhadas estão no arquivo **[PACKAGING.md](PACKAGING.md)**. Para Linux, o comando rápido é:
\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`
O executável estará na pasta `dist/`.
