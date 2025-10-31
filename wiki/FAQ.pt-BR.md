# Perguntas Frequentes (FAQ)

**[Read in English](FAQ.md)**

## Perguntas Gerais

### O que é o Albion Insight?

Albion Insight é uma ferramenta de análise de estatísticas multiplataforma para Albion Online. Ela rastreia estatísticas do jogo em tempo real, como prata ganha, fama obtida e dados de combate, analisando o tráfego de rede. A ferramenta é uma reimplementação moderna em Python da popular ferramenta AlbionOnline-StatisticsAnalysis, projetada para funcionar no Linux, Windows e macOS.

### O Albion Insight é permitido pelos desenvolvedores do jogo?

Sim, ferramentas que monitoram o tráfego de rede sem modificar o cliente do jogo ou fornecer vantagens injustas são geralmente permitidas. O Albion Insight segue os mesmos princípios da ferramenta original AlbionOnline-StatisticsAnalysis, que foi esclarecida como aceitável pelos gerentes da comunidade do Albion Online.

A ferramenta:
- Apenas monitora o tráfego de rede
- Não modifica o cliente do jogo
- Não rastreia jogadores fora do seu campo de visão
- Não fornece overlay no jogo

Para referência, veja a [discussão oficial no fórum](https://forum.albiononline.com/index.php/Thread/124819-Regarding-3rd-Party-Software-and-Network-Traffic-aka-do-not-cheat-Update-16-45-U/).

### O Albion Insight é gratuito?

Sim, o Albion Insight é completamente gratuito e de código aberto sob a Licença MIT. Você pode usar, modificar e distribuir livremente.

## Instalação e Configuração

### Quais sistemas operacionais são suportados?

O Albion Insight suporta:
- **Linux** (Debian, Ubuntu, Fedora, Arch e outras distribuições)
- **Windows** (Windows 10 e posteriores)
- **macOS** (macOS 10.15 e posteriores)

### Por que preciso de privilégios de root/administrador?

A captura de pacotes de rede requer privilégios elevados para acessar a interface de rede em baixo nível. Isso é um recurso de segurança dos sistemas operacionais modernos. A ferramenta usa a biblioteca Scapy, que precisa desses privilégios para capturar pacotes de rede.

### Posso usar o Albion Insight com VPN ou ExitLag?

Sim, o Albion Insight deve funcionar com conexões VPN e proxies de jogos como ExitLag. A ferramenta captura pacotes no nível da interface de rede, então ela pode ver o tráfego independentemente de estar roteado através de uma VPN.

### Posso usar o Albion Insight com GeForce NOW?

Infelizmente, não. Ao jogar através de serviços de jogos em nuvem como GeForce NOW, o jogo roda em servidores remotos, e a análise de tráfego de rede acontece nesses servidores, não na sua máquina local. O Albion Insight não pode capturar esse tráfego.

## Perguntas de Uso

### Como faço para começar a rastrear minha sessão?

Após iniciar o Albion Insight com privilégios de administrador/root, a ferramenta começará automaticamente a capturar o tráfego de rede quando você iniciar o Albion Online. Você pode usar os controles de gerenciamento de sessão para iniciar, parar, resetar ou salvar os dados da sua sessão.

### Quais estatísticas o Albion Insight rastreia?

Atualmente, o Albion Insight rastreia:
- **Prata**: Dinheiro ganho e gasto
- **Fama**: Fama obtida de várias atividades
- **Estatísticas de Combate**: Dano causado, cura realizada, DPS (Dano Por Segundo)
- **Eventos de Jogador**: Abates, mortes e outras interações de jogadores

Mais recursos estão sendo adicionados conforme a decodificação do Protocolo Photon é expandida.

### Por que o medidor de dano não está mostrando nenhum dado?

Existem várias razões possíveis:
1. **Privilégios**: Certifique-se de que está executando a ferramenta com privilégios de root/administrador
2. **Interface de Rede**: A ferramenta pode estar escutando na interface de rede errada
3. **Jogo Não Está Rodando**: Inicie o Albion Online após iniciar o Albion Insight
4. **Firewall**: Verifique se seu firewall está bloqueando a ferramenta

Veja o [Guia de Solução de Problemas](Troubleshooting.pt-BR.md) para soluções mais detalhadas.

### Posso exportar os dados da minha sessão?

Sim, os dados da sessão podem ser salvos para análise posterior. A funcionalidade de exportação está disponível através da interface de gerenciamento de sessão. Os dados exportados são salvos em um formato estruturado que pode ser aberto com aplicativos de planilha ou analisado programaticamente.

## Perguntas Técnicas

### O que é o Protocolo Photon?

Albion Online usa o motor de rede Photon para comunicação cliente-servidor. O Protocolo Photon é o formato de dados usado para codificar eventos do jogo e atualizações de estado. O Albion Insight decodifica esses pacotes para extrair estatísticas do jogo em tempo real.

### Quão preciso é o medidor de dano?

A precisão do medidor de dano depende da completude da decodificação de eventos do Protocolo Photon. Atualmente, os eventos principais de combate estão implementados, mas alguns casos específicos e habilidades particulares podem não ser totalmente rastreados. A comunidade está ativamente trabalhando para melhorar a cobertura de eventos.

### O Albion Insight afeta o desempenho do jogo?

Não, o Albion Insight roda como um processo separado e apenas monitora passivamente o tráfego de rede. Ele não injeta código no jogo ou modifica arquivos do jogo, então não deve afetar o desempenho do jogo.

### Posso contribuir para o projeto?

Absolutamente! Albion Insight é um projeto de código aberto, e contribuições são bem-vindas. Você pode:
- Reportar bugs e sugerir funcionalidades
- Melhorar a documentação
- Adicionar suporte para mais eventos do Protocolo Photon
- Testar a ferramenta em diferentes plataformas
- Enviar melhorias de código

Veja as [Diretrizes de Contribuição](../CONTRIBUTING.pt-BR.md) para mais informações.

## Solução de Problemas

### A aplicação não inicia

1. **Verifique a versão do Python**: Certifique-se de ter Python 3.8 ou posterior instalado
2. **Verifique as dependências**: Garanta que Flet e Scapy estão instalados corretamente
3. **Verifique privilégios**: Execute a aplicação com privilégios de root/administrador
4. **Verifique logs**: Procure por mensagens de erro na saída do terminal/console

### Estou recebendo erros de permissão

Isso geralmente significa que a aplicação não está sendo executada com privilégios suficientes. No Linux, use `sudo` para executar a aplicação. No Windows, execute o Prompt de Comando ou PowerShell como Administrador.

### A ferramenta não está capturando nenhum pacote

1. **Verifique se o jogo está rodando**: Inicie o Albion Online
2. **Verifique a interface de rede**: Certifique-se de que a ferramenta está escutando na interface correta
3. **Verifique configurações do firewall**: Garanta que seu firewall não está bloqueando a ferramenta
4. **Reinicie a ferramenta**: Tente fechar e reabrir o Albion Insight

Para passos de solução de problemas mais detalhados, veja o [Guia de Solução de Problemas](Troubleshooting.pt-BR.md).

## Ainda Tem Dúvidas?

Se sua pergunta não foi respondida aqui:
1. Confira a [Wiki](Home.pt-BR.md) para documentação mais detalhada
2. Pesquise nas [issues existentes](https://github.com/dexcarva/AlbionInsight/issues) no GitHub
3. Abra uma nova issue com a label "question"

---

*Última atualização: Outubro de 2025*
