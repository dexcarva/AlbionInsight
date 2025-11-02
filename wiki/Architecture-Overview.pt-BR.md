# Visão Geral da Arquitetura

**[Read in English](Architecture-Overview.md)**
**[Leer en Español](Architecture-Overview.es-ES.md)**

Este documento fornece uma visão geral de alto nível da arquitetura do Albion Insight, explicando como os diferentes componentes trabalham juntos para rastrear e exibir as estatísticas do Albion Online.

## Arquitetura do Sistema

O Albion Insight segue uma arquitetura modular com três camadas principais:

### 1. Camada de Captura de Rede

A camada de captura de rede é responsável por interceptar e filtrar pacotes de rede do cliente do jogo Albion Online. Esta camada usa a biblioteca **Scapy** para realizar a captura de pacotes de baixo nível.

**Componentes Chave:**
- **Sniffer de Pacotes**: Captura pacotes UDP nas portas do Albion Online (5055, 5056, 5058)
- **Filtro de Pacotes**: Filtra o tráfego que não é do Albion para reduzir a sobrecarga de processamento
- **Gerenciador de Buffer**: Gerencia as filas de pacotes de entrada para evitar perda de dados

**Tecnologias:**
- Biblioteca Scapy do Python
- Acesso a socket raw (requer privilégios de root/administrador)
- Manipulação de protocolo UDP

### 2. Camada de Decodificação de Protocolo

Uma vez que os pacotes são capturados, eles precisam ser decodificados do formato do Protocolo Photon para eventos de jogo significativos. Esta camada traduz a lógica de decodificação C# original para Python.

**Componentes Chave:**
- **Decodificador Photon**: Analisa pacotes do Protocolo Photon
- **Despachante de Eventos**: Roteia eventos decodificados para manipuladores apropriados
- **Manipuladores de Eventos**: Processam tipos de eventos específicos (UpdateMoney, UpdateFame, CastHit, etc.)
- **Gerenciador de Estado**: Mantém o estado do jogo e as informações do jogador

**Estrutura do Protocolo Photon:**
```
Pacote Photon
├── Cabeçalho
│   ├── Tipo de Protocolo
│   ├── Tipo de Comando
│   └── Número de Sequência
└── Payload
    ├── Código do Evento
    ├── Contagem de Parâmetros
    └── Parâmetros
        ├── Tipo
        ├── Chave
        └── Valor
```

**Tipos de Eventos Atualmente Implementados:**
- Atualizações de dinheiro (prata ganha/gasta)
- Atualizações de fama (fama obtida)
- Abates e mortes de jogadores
- Eventos de combate (implementação parcial)

### 3. Camada de Interface do Usuário

A camada de UI apresenta as estatísticas rastreadas ao usuário em uma interface limpa e com aparência nativa. Construída com **Flet**, ela fornece uma experiência de aplicação desktop multiplataforma.

**Componentes Chave:**
- **Janela Principal**: Contêiner da aplicação e navegação
- **Visualização do Medidor de Dano**: Exibição de estatísticas de combate em tempo real
- **Gerenciador de Sessão**: Controles para iniciar, parar e salvar sessões
- **Painel de Estatísticas**: Visão geral dos dados da sessão
- **Módulo de Exportação**: Funcionalidade para salvar dados da sessão

**Framework de UI:**
- Flet (Flutter para Python)
- Vinculação de dados reativa
- Componentes Material Design

## Fluxo de Dados

O diagrama a seguir ilustra como os dados fluem através do sistema:

```
Cliente Albion Online
    ↓ (pacotes UDP)
Interface de Rede
    ↓
Captura de Pacotes Scapy
    ↓
Filtro de Pacotes
    ↓
Decodificador de Protocolo Photon
    ↓
Despachante de Eventos
    ↓ ↓ ↓
Manipuladores de Eventos
    ↓
Gerenciador de Estado
    ↓
Vinculação de Dados da UI
    ↓
Componentes Flet UI
    ↓
Exibição para o Usuário
```

## Modelo de Threading

O Albion Insight usa uma arquitetura multi-threaded para garantir uma UI responsiva e um processamento eficiente de pacotes:

- **Thread Principal**: Executa o loop de eventos da UI do Flet
- **Thread de Captura**: Captura continuamente pacotes de rede
- **Thread de Processamento**: Decodifica e processa eventos Photon
- **Thread de Atualização da UI**: Atualiza periodicamente a UI com novas estatísticas

**Comunicação entre Threads:**
- Filas thread-safe para passagem de pacotes
- Locks para acesso a estado compartilhado
- Atualizações de UI orientadas a eventos

## Estrutura de Arquivos

A aplicação é projetada com simplicidade em mente, contida principalmente em um único arquivo:

```
AlbionInsight/
├── albion_insight.py       # Arquivo principal da aplicação
│   ├── Modelos de Dados
│   ├── Captura de Rede
│   ├── Decodificador Photon
│   ├── Manipuladores de Eventos
│   ├── Gerenciamento de Estado
│   └── Flet UI
├── install.sh              # Script de instalação para Linux
├── run.sh                  # Script de execução para Linux (com sudo)
├── requirements.txt        # Dependências Python
├── README.md               # Documentação
└── PACKAGING.md            # Instruções de compilação
```

## Princípios de Design

### 1. Compatibilidade Multiplataforma

Todos os componentes são projetados para funcionar no Linux, Windows e macOS sem código específico de plataforma, sempre que possível. As diferenças de plataforma são tratadas através de camadas de abstração.

### 2. Dependências Mínimas

O projeto intencionalmente mantém as dependências mínimas para simplificar a instalação e reduzir potenciais problemas de compatibilidade. As dependências principais são:
- Python 3.8+
- Flet (framework de UI)
- Scapy (captura de rede)

### 3. Extensibilidade

O sistema de manipulador de eventos é projetado para ser facilmente extensível. Adicionar suporte para novos eventos Photon requer:
1. Identificar o código do evento
2. Criar uma função manipuladora
3. Registrar o manipulador com o despachante

### 4. Desempenho

As otimizações de desempenho incluem:
- Filtragem eficiente de pacotes para reduzir a carga de processamento
- Processamento assíncrono de eventos
- Carregamento preguiçoso de componentes de UI
- Pegada de memória mínima

## Comparação com o Projeto Original

| Aspecto | AlbionOnline-StatisticsAnalysis | Albion Insight |
|--------|--------------------------------|----------------|
| Linguagem | C# | Python |
| Framework de UI | WPF | Flet (Flutter) |
| Plataforma | Apenas Windows | Multiplataforma |
| Biblioteca de Rede | Customizada/Npcap | Scapy |
| Arquitetura | Solução multi-projeto | Aplicação de arquivo único |
| Cobertura de Eventos | Abrangente | Crescente (orientada pela comunidade) |

## Futuras Melhorias na Arquitetura

Melhorias arquitetônicas planejadas incluem:

1. **Sistema de Plugins**: Permitir extensões desenvolvidas pela comunidade
2. **Sistema de Configuração**: Arquivos de configuração externos para personalização
3. **Integração com Banco de Dados**: Armazenamento persistente opcional para dados históricos
4. **Servidor API**: API REST para integrações externas
5. **Estrutura de Arquivos Modular**: Dividir em múltiplos módulos à medida que a complexidade cresce

## Contribuindo para a Arquitetura

Se você está interessado em contribuir para a arquitetura:

1. Revise as [Diretrizes de Contribuição](../CONTRIBUTING.pt-BR.md)
2. Discuta grandes mudanças arquitetônicas nas Issues do GitHub primeiro
3. Garanta a compatibilidade com versões anteriores sempre que possível
4. Documente as decisões arquitetônicas

---

*Última atualização: Outubro de 2025*
