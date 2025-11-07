# Contribuindo para o Albion Insight

**[Read in English](CONTRIBUTING.md)**

Primeiramente, obrigado por considerar contribuir para o Albion Insight! São pessoas como você que tornam o Albion Insight uma ferramenta tão valiosa para a comunidade de Albion Online.

## Sumário

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
  - [Relatar Bugs](#relatar-bugs)
  - [Sugerir Funcionalidades](#sugerir-funcionalidades)
  - [Contribuições de Código](#contribuições-de-código)
  - [Documentação](#documentação)
- [Configuração para Desenvolvimento](#configuração-para-desenvolvimento)
- [Padrões de Codificação](#padrões-de-codificação)
- [Mensagens de Commit](#mensagens-de-commit)
- [Processo de Pull Request](#processo-de-pull-request)

## Código de Conduta

Este projeto e todos que participam dele são regidos pelo nosso Código de Conduta. Ao participar, espera-se que você siga este código. Por favor, reporte comportamentos inaceitáveis aos mantenedores do projeto.

## Como Posso Contribuir?

### Relatar Bugs

Antes de criar relatórios de bugs, por favor, verifique as *issues* existentes para evitar duplicatas. Ao criar um relatório de bug, inclua o máximo de detalhes possível usando o modelo de relatório de bug.

**Bons relatórios de bug incluem:**
- Um título claro e descritivo
- Passos exatos para reproduzir o problema
- Comportamento esperado versus real
- Capturas de tela, se aplicável
- Detalhes do seu ambiente (Sistema Operacional, versão do Python, etc.)
- Logs ou mensagens de erro relevantes

### Sugerir Funcionalidades

Sugestões de funcionalidades são bem-vindas! Por favor, use o modelo de solicitação de funcionalidade e forneça:
- Uma descrição clara da funcionalidade
- O problema que ela resolve
- Possíveis abordagens de implementação
- Quaisquer alternativas que você considerou

### Contribuições de Código

Adoramos contribuições de código! Veja como começar:

1. **Faça um Fork** do repositório e crie seu *branch* a partir de `master`.
2. **Configure seu ambiente de desenvolvimento** (veja Configuração para Desenvolvimento abaixo).
3. **Faça suas alterações** seguindo nossos padrões de codificação.
4. **Teste suas alterações** completamente.
5. **Atualize a documentação**, se necessário.
6. **Envie um *pull request*** usando nosso modelo de PR.

### Documentação

Melhorias na documentação são sempre apreciadas! Isso inclui:
- Arquivos README
- Páginas Wiki
- Comentários no código
- Tutoriais e guias
- Traduções para outros idiomas

## Configuração para Desenvolvimento

### Pré-requisitos

- Python 3.8 ou superior
- Git
- Privilégios de Root/Administrador (para captura de pacotes)

### Configurando Seu Ambiente

```bash
# Clone seu fork
git clone https://github.com/SEU_USUARIO/AlbionInsight.git
cd AlbionInsight

# Crie um ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
# No Linux/macOS:
source venv/bin/activate
# No Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Instale as dependências de desenvolvimento
pip install pylint flake8 black pytest
```

### Executando a Aplicação

```bash
# No Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# No Windows (como Administrador):
python albion_insight.py
```

## Padrões de Codificação

Seguimos as diretrizes de estilo PEP 8 para código Python. Por favor, garanta que seu código adere a estes padrões:

- Use 4 espaços para indentação (sem tabulações)
- Comprimento máximo da linha de 100 caracteres
- Use nomes de variáveis e funções significativos
- Adicione *docstrings* a todas as funções e classes
- Inclua dicas de tipo (*type hints*) onde apropriado
- Mantenha as funções focadas e concisas

**Ferramentas para ajudar:**
```bash
# Formate seu código com black
black albion_insight.py

# Verifique problemas de estilo
flake8 albion_insight.py

# Execute o linter
pylint albion_insight.py
```

## Mensagens de Commit

Escreva mensagens de *commit* claras e significativas:

- Use o tempo presente ("Adiciona funcionalidade" e não "Adicionada funcionalidade")
- Use o modo imperativo ("Move o cursor para..." e não "Moveu o cursor para...")
- Limite a primeira linha a 72 caracteres
- Referencie *issues* e *pull requests* quando relevante

**Exemplos:**
```
Adiciona funcionalidade de exportação do medidor de dano

Corrige a análise de pacotes de rede para conexões IPv6

Atualiza o README com instruções de instalação para macOS

Fecha #123
```

## Processo de Pull Request

1. **Atualize a documentação** para quaisquer alterações na funcionalidade.
2. **Adicione testes** para novas funcionalidades ou correções de bugs.
3. **Garanta que todos os testes passem** antes de enviar.
4. **Atualize o README.md**, se necessário.
5. **Preencha o modelo de PR** completamente.
6. **Ligue *issues* relacionadas** na descrição do seu PR.
7. **Solicite revisão** dos mantenedores.
8. **Responda ao *feedback*** prontamente e profissionalmente.

### Lista de Verificação do PR

Antes de enviar seu PR, garanta:
- [ ] O código segue as diretrizes de estilo do projeto
- [ ] Auto-revisão concluída
- [ ] Comentários adicionados a seções de código complexas
- [ ] Documentação atualizada
- [ ] Nenhuma nova advertência gerada
- [ ] Testes adicionados e aprovados
- [ ] Alterações dependentes mescladas

## Perguntas?

Não hesite em fazer perguntas! Você pode:
- Abrir uma *issue* com o rótulo "question"
- Juntar-se às nossas discussões da comunidade
- Entrar em contato com os mantenedores

Obrigado por contribuir para o Albion Insight! Seus esforços ajudam a tornar esta ferramenta melhor para toda a comunidade de Albion Online.
