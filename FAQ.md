# Perguntas Frequentes (FAQ) - Albion Insight

## Perguntas Gerais

### P1: O que é o Albion Insight?

**R:** Albion Insight é uma ferramenta de análise estatística multiplataforma (Linux, Windows, macOS) para o jogo Albion Online. Ele rastreia estatísticas em tempo real no jogo, como prata, fama e dados de combate (Medidor de Dano), analisando o tráfego de rede. É uma alternativa moderna e de código aberto à ferramenta original baseada em C#/WPF.

---

### P2: O Albion Insight é seguro de usar? Serei banido?

**R:** Sim, o Albion Insight é seguro de usar. Ele apenas analisa o tráfego de rede e não modifica arquivos do jogo nem injeta código no jogo. É semelhante a outras ferramentas legítimas usadas pela comunidade. No entanto, verifique sempre os termos de serviço oficiais do Albion Online para as políticas mais recentes.

---

### P3: Preciso de privilégios de administrador/root para executar o Albion Insight?

**R:** Sim, a captura de pacotes de rede requer privilégios elevados. Você precisará executar a aplicação com `sudo` no Linux/macOS ou como Administrador no Windows.

---

### P4: Quais são os requisitos de sistema?

**R:** 
- **Python:** 3.8 ou superior
- **SO:** Linux, Windows ou macOS
- **RAM:** Mínimo 512 MB (1 GB recomendado)
- **Rede:** Conexão ativa com a internet para os servidores do Albion Online

---

## Instalação e Configuração

### P5: Como instalo o Albion Insight?

**R:** Siga o guia de instalação no [README.md](README.md). Fornecemos scripts de instalação rápida para Linux e etapas de instalação manual para todas as plataformas.

---

### P6: Posso usar o Albion Insight no macOS?

**R:** Sim! O Albion Insight é totalmente compatível com macOS. Siga as etapas de instalação manual no README e execute a aplicação com `sudo`.

---

### P7: E se eu receber um erro de "Permissão negada"?

**R:** Este erro ocorre porque a captura de pacotes de rede requer privilégios elevados. Execute a aplicação com `sudo` no Linux/macOS ou como Administrador no Windows. Consulte o guia [TROUBLESHOOTING.md](TROUBLESHOOTING.md) para mais detalhes.

---

### P8: Como atualizo o Albion Insight?

**R:** 
1. Navegue até o seu diretório Albion Insight.
2. Puxe as últimas alterações:
   ```bash
   git pull origin main
   ```
3. Atualize as dependências:
   ```bash
   pip install -r requirements.txt --upgrade
   ```
4. Execute a aplicação novamente.

---

## Recursos e Funcionalidades

### P9: Quais estatísticas o Albion Insight rastreia?

**R:** Atualmente, o Albion Insight rastreia:
- **Prata:** Moeda do jogo ganha
- **Fama:** Pontos de experiência ganhos
- **Medidor de Dano:** Estatísticas de combate em tempo real (dano causado, cura realizada, DPS)
- **Estatísticas do Jogador:** Métricas de desempenho individual do jogador

---

### P10: Posso exportar meus dados de sessão?

**R:** Este recurso está atualmente em desenvolvimento. Os dados da sessão são salvos localmente no diretório `sessions/`. Versões futuras suportarão a exportação para CSV, JSON ou outros formatos.

---

### P11: O Albion Insight funciona com todos os servidores do Albion Online?

**R:** O Albion Insight foi projetado para funcionar com os servidores oficiais do Albion Online. Pode não funcionar com servidores privados ou versões modificadas do jogo.

---

### P12: Posso usar o Albion Insight enquanto jogo em tela cheia?

**R:** Sim, o Albion Insight é executado como um aplicativo separado e pode ser exibido ao lado do jogo. No Linux, você pode usar Alt+Tab para alternar entre as janelas. No Windows e macOS, você pode organizar as janelas lado a lado ou usar áreas de trabalho virtuais.

---

## Solução de Problemas

### P13: O medidor de dano não está atualizando. O que devo fazer?

**R:** 
1. Certifique-se de que o Albion Online está em execução e você está no jogo.
2. Verifique se sua interface de rede está configurada corretamente.
3. Verifique se o filtro BPF está correto na configuração.
4. Verifique os logs em `logs/app.log` para mensagens de erro.

Consulte [TROUBLESHOOTING.md](TROUBLESHOOTING.md) para mais detalhes.

---

### P14: Vejo um erro sobre o módulo "flet". O que devo fazer?

**R:** Isso significa que a biblioteca Flet não está instalada ou não está ativada corretamente. Ative seu ambiente virtual e reinstale as dependências:
```bash
source venv/bin/activate  # No Linux/macOS
pip install -r requirements.txt
```

---

### P15: A aplicação trava na inicialização. Como depurar isso?

**R:** 
1. Verifique os logs em `logs/app.log`.
2. Execute a aplicação a partir do terminal para ver as mensagens de erro:
   ```bash
   python albion_insight/main.py
   ```
3. Relate o erro em [GitHub Issues](https://github.com/dexcarva/AlbionInsight/issues) com a mensagem de erro completa e os logs.

---

## Desenvolvimento e Contribuição

### P16: Posso contribuir para o Albion Insight?

**R:** Com certeza! Aceitamos contribuições da comunidade. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para obter diretrizes sobre como contribuir com código, documentação, traduções ou relatórios de bugs.

---

### P17: Como configuro um ambiente de desenvolvimento?

**R:** 
1. Faça um fork do repositório.
2. Clone seu fork.
3. Crie um ambiente virtual.
4. Instale as dependências de desenvolvimento:
   ```bash
   pip install -r requirements-dev.txt
   ```
5. Faça suas alterações e teste-as.
6. Envie um pull request.

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para obter instruções detalhadas.

---

### P18: Quais linguagens de programação o Albion Insight usa?

**R:** O Albion Insight é escrito em **Python** usando o framework **Flet** para a UI e **Scapy** para análise de pacotes de rede.

---

### P19: Posso criar um executável a partir do Albion Insight?

**R:** Sim! Consulte o guia [PACKAGING.md](PACKAGING.md) para obter instruções sobre como criar executáveis autônomos usando PyInstaller.

---

## Desempenho e Otimização

### P20: Por que a aplicação está usando muita CPU?

**R:** O alto uso da CPU pode ser causado por:
1. Processamento ineficiente de pacotes.
2. Atualizações de UI muito frequentes.
3. Execução de múltiplas instâncias.

Verifique os logs e considere otimizar o loop de captura de pacotes. Relate problemas de desempenho no GitHub.

---

### P21: Posso executar o Albion Insight em um computador de baixo desempenho?

**R:** O Albion Insight tem requisitos de sistema modestos. No entanto, em sistemas muito fracos, você pode ter problemas de desempenho. Tente:
1. Fechar aplicativos desnecessários.
2. Reduzir a frequência de atualização da UI.
3. Executar a aplicação a partir de um SSD em vez de um HDD.

---

## Legal e Licenciamento

### P22: Qual é a licença do Albion Insight?

**R:** O Albion Insight é licenciado sob a **Licença MIT**. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---

### P23: Posso usar o Albion Insight comercialmente?

**R:** A Licença MIT permite o uso comercial, modificação e distribuição. No entanto, você deve incluir a licença original e o aviso de direitos autorais.

---

### P24: Quem é o responsável pelo Albion Insight?

**R:** O Albion Insight é mantido pela comunidade. O projeto original foi criado por dexcarva como um port do original em C#/WPF de Triky313.

---

## Obtendo Ajuda

### P25: Onde posso obter ajuda se minha pergunta não for respondida aqui?

**R:** 
1. Consulte o guia [TROUBLESHOOTING.md](TROUBLESHOOTING.md).
2. Pesquise [Issues](https://github.com/dexcarva/AlbionInsight/issues) existentes no GitHub.
3. Crie uma nova issue com uma descrição detalhada do seu problema.
4. Participe de discussões da comunidade no Discord ou fóruns.

---

**Última Atualização:** 30 de Novembro de 2025
