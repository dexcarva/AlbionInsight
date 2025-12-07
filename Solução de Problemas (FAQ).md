# Perguntas Frequentes e Solução de Problemas

| Pergunta | Resposta |
| :--- | :--- |
| **Por que preciso de privilégios de root/administrador?** | A biblioteca `Scapy` precisa de acesso de baixo nível à interface de rede para "farejar" (sniff) os pacotes de dados do jogo. Isso é uma exigência de segurança do sistema operacional. |
| **O Albion Insight é seguro? Posso ser banido?** | O Albion Insight **apenas monitora** o tráfego de rede. Ele não injeta código, não modifica o cliente do jogo e não automatiza ações. O projeto original (C#) e este *port* são considerados seguros e permitidos pela Sandbox Interactive (desenvolvedora do Albion Online). |
| **Estou no Linux e vejo uma tela branca.** | Este é um problema conhecido em algumas distribuições LTS. Certifique-se de estar usando a versão mais recente do Albion Insight, pois uma correção foi aplicada recentemente. Se o problema persistir, abra uma [Issue no GitHub](https://github.com/dexcarva/AlbionInsight/issues). |
| **Posso usar com VPN ou ExitLag?** | Sim, mas a configuração pode ser mais complexa. Você precisará garantir que o `Scapy` esteja rastreando a interface de rede correta que está sendo usada pela VPN. |

[[Home]]
