# Contribuindo para o Albion Insight

**[Read in English](CONTRIBUTING.md)**
**[Leer en Español](CONTRIBUTING.es-ES.md)**
**[Lire en Français](CONTRIBUTING.fr-FR.md)**

Antes de mais nada, obrigado por considerar contribuir com o Albion Insight! São pessoas como você que tornam o Albion Insight uma ferramenta incrível para a comunidade de Albion Online.

## Índice

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
  - [Reportando Bugs](#reportando-bugs)
  - [Sugerindo Funcionalidades](#sugerindo-funcionalidades)
  - [Contribuições de Código](#contribuições-de-código)
  - [Documentação](#documentação)
- [Configuração do Ambiente de Desenvolvimento](#configuração-do-ambiente-de-desenvolvimento)
- [Padrões de Código](#padrões-de-código)
- [Mensagens de Commit](#mensagens-de-commit)
- [Processo de Pull Request](#processo-de-pull-request)

## Código de Conduta

Este projeto e todos que participam dele são regidos pelo nosso Código de Conduta. Ao participar, espera-se que você mantenha este código. Por favor, reporte comportamentos inaceitáveis aos mantenedores do projeto.

## Como Posso Contribuir?

### Reportando Bugs

Antes de criar relatórios de bugs, verifique as issues existentes para evitar duplicatas. Ao criar um relatório de bug, inclua o máximo de detalhes possível usando o template de bug report.

**Bons relatórios de bug incluem:**
- Um título claro e descritivo
- Passos exatos para reproduzir o problema
- Comportamento esperado vs comportamento real
- Screenshots se aplicável
- Detalhes do seu ambiente (SO, versão do Python, etc.)
- Logs ou mensagens de erro relevantes

### Sugerindo Funcionalidades

Sugestões de funcionalidades são bem-vindas! Use o template de feature request e forneça:
- Uma descrição clara da funcionalidade
- O problema que ela resolve
- Possíveis abordagens de implementação
- Alternativas que você considerou

### Contribuições de Código

Adoramos contribuições de código! Veja como começar:

1. **Faça um fork do repositório** e crie sua branch a partir da `master`
2. **Configure seu ambiente de desenvolvimento** (veja Configuração do Ambiente abaixo)
3. **Faça suas alterações** seguindo nossos padrões de código
4. **Teste suas alterações** completamente
5. **Atualize a documentação** se necessário
6. **Envie um pull request** usando nosso template de PR

### Documentação

Melhorias na documentação são sempre apreciadas! Isso inclui:
- Arquivos README
- Páginas da Wiki
- Comentários no código
- Tutoriais e guias
- Traduções para outros idiomas

## Configuração do Ambiente de Desenvolvimento

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

# Instale dependências de desenvolvimento
pip install pylint flake8 black pytest
```

### Executando a Aplicação

```bash
# No Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# No Windows (como Administrador):
python albion_insight.py
```

## Padrões de Código

Seguimos as diretrizes de estilo PEP 8 para código Python. Certifique-se de que seu código adere a esses padrões:

- Use 4 espaços para indentação (sem tabs)
- Comprimento máximo de linha de 100 caracteres
- Use nomes significativos para variáveis e funções
- Adicione docstrings a todas as funções e classes
- Inclua type hints quando apropriado
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

Escreva mensagens de commit claras e significativas:

- Use o tempo presente ("Adiciona funcionalidade" não "Adicionou funcionalidade")
- Use o modo imperativo ("Move cursor para..." não "Move cursor para...")
- Limite a primeira linha a 72 caracteres
- Referencie issues e pull requests quando relevante

**Exemplos:**
```
Adiciona funcionalidade de exportação do damage meter

Corrige parsing de pacotes de rede para conexões IPv6

Atualiza README com instruções de instalação para macOS

Closes #123
```

## Processo de Pull Request

1. **Atualize a documentação** para quaisquer mudanças na funcionalidade
2. **Adicione testes** para novas funcionalidades ou correções de bugs
3. **Garanta que todos os testes passem** antes de enviar
4. **Atualize o README.md** se necessário
5. **Preencha o template de PR** completamente
6. **Vincule issues relacionadas** na descrição do seu PR
7. **Solicite revisão** dos mantenedores
8. **Responda ao feedback** prontamente e profissionalmente

### Checklist de PR

Antes de enviar seu PR, garanta que:
- [ ] O código segue as diretrizes de estilo do projeto
- [ ] Auto-revisão completada
- [ ] Comentários adicionados a seções complexas do código
- [ ] Documentação atualizada
- [ ] Nenhum novo warning gerado
- [ ] Testes adicionados e passando
- [ ] Mudanças dependentes foram merged

## Dúvidas?

Não hesite em fazer perguntas! Você pode:
- Abrir uma issue com a label "question"
- Participar das discussões da comunidade
- Entrar em contato com os mantenedores

Obrigado por contribuir com o Albion Insight! Seus esforços ajudam a tornar esta ferramenta melhor para toda a comunidade de Albion Online.
