# 🗺️ Roteiro do Projeto Albion Insight (Roadmap)

**[Read in English](Roadmap.md)**

Este roteiro descreve os recursos e melhorias planejadas para o Albion Insight. O cronograma é aproximado e pode mudar com base nas contribuições da comunidade e nas prioridades.

## Versão Atual: 0.1.0 (Lançamento Inicial)

### Funcionalidades Implementadas
- ✅ Suporte multiplataforma (Linux, Windows, macOS)
- ✅ Captura de pacotes de rede em tempo real
- ✅ Decodificação básica do Protocolo Photon
- ✅ Estrutura e interface de usuário do medidor de dano (Damage Meter)
- ✅ Gerenciamento de sessão (iniciar, parar, redefinir, salvar)
- ✅ Rastreamento de prata e fama
- ✅ Rastreamento básico de eventos de combate

## Versão 0.2.0 (1º Trimestre de 2026) - Rastreamento de Combate Aprimorado

### Metas
- Implementação completa dos eventos de combate centrais
- Melhoria da precisão do medidor de dano
- Interface de usuário aprimorada para estatísticas de combate

### Funcionalidades Planejadas
- [ ] Implementação completa do evento `CastHit`
- [ ] Implementação completa do evento `Attack`
- [ ] Melhorias no rastreamento de cura
- [ ] Rastreamento de *buffs* e *debuffs*
- [ ] Rastreamento de tempo de recarga de habilidades (*cooldown*)
- [ ] Visualizador de registro de combate (*Combat Log*)
- [ ] Gráfico de DPS em tempo real
- [ ] Colunas configuráveis no medidor de dano

### Melhorias Técnicas
- [ ] Testes de unidade para manipuladores de eventos
- [ ] Otimização de desempenho para processamento de pacotes
- [ ] Otimização do uso de memória
- [ ] Melhorias no tratamento de erros

## Versão 0.3.0 (2º Trimestre de 2026) - Persistência e Análise de Dados

### Metas
- Adicionar armazenamento persistente para histórico de sessões
- Fornecer ferramentas de análise de dados históricos
- Aprimoramentos na funcionalidade de exportação

### Funcionalidades Planejadas
- [ ] Banco de dados SQLite para armazenamento de sessões
- [ ] Navegador de histórico de sessões
- [ ] Análise estatística de sessões passadas
- [ ] Comparação entre sessões
- [ ] Exportação para formato CSV
- [ ] Exportação para formato JSON
- [ ] Exportação para formato Excel
- [ ] Backup automático de sessões

### Melhorias Técnicas
- [ ] Design de esquema de banco de dados
- [ ] Sistema de migração para atualizações de banco de dados
- [ ] Integração de biblioteca de visualização de dados
- [ ] Camada de cache para desempenho

## Versão 0.4.0 (3º Trimestre de 2026) - Funcionalidades Avançadas

### Metas
- Implementar recursos de rastreamento avançados da ferramenta original
- Adicionar rastreamento específico de masmorras
- Aprimorar a exibição de informações do jogador

### Funcionalidades Planejadas
- [ ] Rastreador de masmorras (*Dungeon tracker*)
- [ ] Temporizador de entrada em masmorras
- [ ] Rastreamento de histórico de mapas
- [ ] Painel de informações do jogador
- [ ] Rastreamento de atividade de guilda
- [ ] Registrador de *loot* (*Loot logger*)
- [ ] Notificações de itens raros
- [ ] Calculadora de Fama por hora

### Melhorias Técnicas
- [ ] Sistema de cache de eventos
- [ ] Gerenciamento de estado aprimorado
- [ ] Fundação para arquitetura de *plugins*
- [ ] Documentação da API

## Versão 0.5.0 (4º Trimestre de 2026) - Criação e Economia

### Metas
- Adicionar calculadora de criação (*crafting*)
- Implementar rastreamento de dados da Casa de Leilões (*Auction House*)
- Fornecer ferramentas de análise econômica

### Funcionalidades Planejadas
- [ ] Calculadora de criação
- [ ] Análise de custo de material
- [ ] Calculadora de margem de lucro
- [ ] Rastreamento de preços da Casa de Leilões
- [ ] Análise de tendências de mercado
- [ ] Histórico de preços de itens
- [ ] Rastreamento de comércio
- [ ] Painel econômico (*Economic dashboard*)

### Melhorias Técnicas
- [ ] Integração de API externa
- [ ] Sincronização de dados
- [ ] Atualizações de dados em segundo plano
- [ ] Sistema de notificação

## Versão 1.0.0 (2027) - Lançamento Estável

### Metas
- Paridade de recursos com a ferramenta original
- Lançamento estável e pronto para produção
- Documentação abrangente

### Funcionalidades Planejadas
- [ ] Todos os principais recursos do `AlbionOnline-StatisticsAnalysis`
- [ ] Cobertura abrangente de eventos
- [ ] Suporte a múltiplos idiomas na UI
- [ ] Temas personalizáveis
- [ ] Opções de configuração avançadas
- [ ] Sincronização em nuvem (opcional)
- [ ] Aplicativo complementar móvel (opcional)

### Melhorias Técnicas
- [ ] Cobertura total de testes
- [ ] Integração/implantação contínua
- [ ] Processo de lançamento automatizado
- [ ] *Benchmarking* de desempenho
- [ ] Auditoria de segurança
- [ ] Documentação de código
- [ ] Garantias de estabilidade da API

## Visão de Longo Prazo (Pós 1.0)

### Recursos Comunitários
- Mercado de *plugins*
- Manipuladores de eventos contribuídos pela comunidade
- Análise de sessão compartilhada
- *Leaderboards* (opcional, respeitando a privacidade)

### Análise Avançada
- Aprendizado de máquina para análise de padrões de jogo
- Análise preditiva para tendências de mercado
- Recomendações automatizadas para melhoria

### Integração
- Integração com bot do Discord
- Painel web (*Web dashboard*)
- Suporte a *overlay* de *streaming*
- Integração com ferramentas de terceiros

## Como Contribuir para o Roteiro

Agradecemos a contribuição da comunidade para o roteiro! Veja como você pode ajudar:

1. **Vote em Recursos**: Comente nas solicitações de recursos existentes nas [Issues do GitHub](https://github.com/dexcarva/AlbionInsight/issues)
2. **Sugira Recursos**: Abra uma nova *issue* com o rótulo `enhancement` e descreva sua proposta.
3. **Implemente Recursos**: Escolha um item do roteiro e envie um *Pull Request*.
4. **Forneça Feedback**: Compartilhe suas ideias sobre a priorização.

## Princípios do Roteiro

Nosso roteiro segue os seguintes princípios:

1. **Impulsionado pela Comunidade**: Os recursos são priorizados com base nas necessidades da comunidade.
2. **Estabilidade em Primeiro Lugar**: Não sacrificaremos a estabilidade por novos recursos.
3. **Multiplataforma**: Todos os recursos devem funcionar em todas as plataformas suportadas.
4. **Código Aberto**: Todos os recursos permanecem gratuitos e de código aberto.
5. **Respeito à Privacidade**: Nenhuma coleta de dados sem o consentimento explícito do usuário.

## Acompanhamento do Progresso

Você pode acompanhar o progresso dos itens do roteiro através de:
- [Marcos do GitHub (Milestones)](https://github.com/dexcarva/AlbionInsight/milestones)
- [Projetos do GitHub (Projects)](https://github.com/dexcarva/AlbionInsight/projects)
- [Registro de Alterações (Changelog)](../CHANGELOG.md)

---

*Este roteiro está sujeito a alterações com base no feedback e nas contribuições da comunidade.*

*Última atualização: 24 de Novembro de 2025*
