# Solução de Problemas (FAQ)

Este guia de Perguntas Frequentes (FAQ) e Solução de Problemas visa responder às dúvidas mais comuns e ajudar a resolver problemas de instalação ou execução do Albion Insight.

| Pergunta | Resposta Detalhada |
| :--- | :--- |
| **Por que preciso de privilégios de root/administrador?** | A biblioteca **Scapy**, utilizada pelo Albion Insight para analisar o tráfego de rede, requer acesso de baixo nível à interface de rede para "farejar" (sniff) os pacotes de dados do jogo. Esta é uma exigência de segurança do sistema operacional (Linux, macOS e Windows) para qualquer aplicação que precise capturar dados diretamente da rede. Sem esses privilégios, o programa não consegue ver os pacotes de dados do Albion Online. |
| **O Albion Insight é seguro? Posso ser banido?** | O Albion Insight **apenas monitora** o tráfego de rede. Ele não injeta código, não modifica o cliente do jogo e não automatiza ações. O projeto original (C#) e este *port* em Python são ferramentas passivas de análise. A Sandbox Interactive (desenvolvedora do Albion Online) geralmente permite o uso de ferramentas passivas que não oferecem vantagem competitiva. No entanto, o uso é por sua conta e risco. |
| **Estou no Linux e vejo uma tela branca.** | Este é um problema conhecido em algumas distribuições Linux LTS (Long-Term Support) devido a incompatibilidades com o framework Flet. **Solução:** Certifique-se de estar usando a versão mais recente do Albion Insight. Se o problema persistir, tente executar o aplicativo com a flag `--web` para usar a interface no navegador (embora não seja a experiência nativa ideal). Se o problema persistir, por favor, abra uma [Issue no GitHub](https://github.com/dexcarva/AlbionInsight/issues) com detalhes do seu sistema operacional e versão. |
| **Posso usar com VPN ou ExitLag?** | Sim, é possível, mas a configuração pode ser mais complexa. Você precisará garantir que o **Scapy** esteja rastreando a **interface de rede correta** que está sendo usada pela VPN ou serviço de otimização de rota. O Albion Insight tenta detectar a interface automaticamente, mas em ambientes com VPN, pode ser necessário especificar a interface manualmente nas configurações (recurso em desenvolvimento). |

[[Home]]
