# Guia de Refatoração Modular

## Nova Estrutura do Projeto
O projeto Albion Insight foi refatorado para uma estrutura modular mais limpa e sustentável. O código principal foi movido do diretório raiz para o subdiretório .

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

## Arquivos Removidos
Os seguintes arquivos foram removidos do diretório raiz, pois seu conteúdo foi movido para a nova estrutura modular:

* `albion_insight.py`
* `models.py`
* `network_tracker.py`

## Como Contribuir
Novas contribuições de código devem seguir a nova estrutura modular, garantindo que a lógica de negócio permaneça em `core/` e os componentes de UI em `ui/`.

