# Segurança e Privacidade no Albion Insight

A segurança e a privacidade dos usuários são prioridades máximas no desenvolvimento do Albion Insight. Como uma ferramenta que lida com a captura de tráfego de rede, é crucial que os usuários compreendam como o projeto aborda estas questões.

## 1. Segurança da Execução (Linux)

O principal risco de segurança em ferramentas de captura de pacotes é a necessidade de privilégios elevados (`root` ou `sudo`).

### 1.1. Uso de `setcap` para Execução Segura

O Albion Insight implementa uma solução de segurança robusta no Linux:

*   **O Problema:** Executar o aplicativo inteiro como `sudo` é perigoso, pois um bug poderia comprometer todo o sistema.
*   **A Solução:** Utilizamos o utilitário `setcap` para conceder ao binário do Python apenas as capacidades de rede necessárias (`cap_net_raw` e `cap_net_admin`).
*   **O Resultado:** O aplicativo pode capturar pacotes sem a necessidade de ser executado como `root`, mitigando significativamente o risco de segurança.

**Recomendação:** Sempre utilize o script `./install.sh` e `./run.sh` no Linux, pois eles garantem que a configuração de segurança `setcap` seja aplicada corretamente.

## 2. Privacidade e Dados Capturados

O Albion Insight é um *sniffer* **local** e **não envia dados para servidores externos**.

### 2.1. O que é Capturado?

O aplicativo captura pacotes de rede UDP nas portas 5055, 5056 e 5058, que são as portas de comunicação do Albion Online. Os dados decodificados incluem:

*   Estatísticas do Jogo: Prata, Fama, Eventos de Combate (Dano, Cura, Kills, Deaths).
*   Identificadores de Entidades: IDs de jogadores, mobs e itens.

### 2.2. O que NÃO é Capturado/Enviado?

*   **Nenhuma Informação Pessoal:** O aplicativo não captura senhas, informações de login, endereços IP externos ou qualquer outro dado pessoal identificável.
*   **Nenhuma Transmissão Externa:** Os dados capturados e processados **permanecem exclusivamente no seu computador**. Não há código no Albion Insight que envie suas estatísticas ou pacotes de rede para qualquer servidor de terceiros.

## 3. Conformidade com as Regras do Jogo

O Albion Insight é considerado uma ferramenta **segura e permitida** pela Sandbox Interactive (desenvolvedora do Albion Online).

*   **Apenas Leitura:** O aplicativo **apenas lê** o tráfego de rede. Ele não injeta código, não modifica o cliente do jogo e não automatiza nenhuma ação.
*   **Ferramenta de Análise:** É uma ferramenta de análise de dados, similar a um medidor de dano que lê logs de combate, mas de forma mais direta através da rede.

**Nota:** O projeto original em C# e este *port* em Python são amplamente utilizados na comunidade e nunca foram associados a banimentos.

## 4. Relatório de Vulnerabilidades

Se você encontrar qualquer vulnerabilidade de segurança ou suspeitar de um comportamento inadequado no código:

*   **Consulte o [SECURITY.md](SECURITY.md):** Siga o processo de divulgação responsável detalhado no arquivo `SECURITY.md` do repositório.
*   **Divulgação Responsável:** Por favor, não divulgue vulnerabilidades publicamente (em Issues ou Pull Requests) antes de dar aos mantenedores tempo para corrigir o problema.
