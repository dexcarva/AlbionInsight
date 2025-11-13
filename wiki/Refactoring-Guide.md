# Guia de Refatoração Modular

## Nova Estrutura do Projeto
O projeto Albion Insight foi refatorado para uma estrutura modular mais limpa e sustentável. O código principal foi movido do diretório raiz para o subdiretório `albion_insight/`.

### Estrutura de Diretórios

```
AlbionInsight/
├── albion_insight/
│   ├── core/           # Lógica de negócio, modelos de dados, decodificação de pacotes
│   ├── ui/             # Componentes da interface do usuário (Flet)
│   └── main.py         # Ponto de entrada principal da aplicação
├── run.sh              # Script de execução atualizado para o novo ponto de entrada
└── ...
```

## Refatoração do Network Tracker (Novidade)

O componente de rastreamento de rede (`network_tracker.py`) foi refatorado de um conjunto de funções para uma **classe `NetworkTracker`**.

### Benefícios da Refatoração:
1.  **Gerenciamento de Estado:** O estado da sessão (estatísticas, status de execução) agora é encapsulado na instância da classe, facilitando o gerenciamento e a passagem de dados.
2.  **Controle de Thread:** A classe gerencia explicitamente a thread de captura de pacotes (`sniff_thread`), permitindo um controle mais limpo sobre o início e a parada da captura.
3.  **Preparação para o Futuro:** A estrutura de classe facilita a injeção de dependências e a implementação de testes unitários.

### Alterações Principais:
- O arquivo `albion_insight/core/network_tracker.py` agora contém a classe `NetworkTracker`.
- Uma instância global (`tracker_instance`) é criada no final do arquivo para manter a compatibilidade com a UI existente.
- A função `start_network_tracker()` agora chama `tracker_instance.start()`.
- A função `get_current_stats()` agora chama `tracker_instance.get_current_stats()`.

## Arquivos Removidos
Os seguintes arquivos foram removidos do diretório raiz, pois seu conteúdo foi movido para a nova estrutura modular:

* `albion_insight.py`
* `models.py`
* `network_tracker.py`

## Como Contribuir
Novas contribuições de código devem seguir a nova estrutura modular, garantindo que a lógica de negócio permaneça em `core/` e os componentes de UI em `ui/`.
