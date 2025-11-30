# Contribuir para o Albion Insight

**[Leia em Português do Brasil](CONTRIBUTING.pt-br.md)**

**[Leia em Português](CONTRIBUTING.pt-BR.md)**
**[Leer en Español](CONTRIBUTING.es-ES.md)**
**[Lire en Français](CONTRIBUTING.fr-FR.md)**
**[Read in Arabic (اقرأ بالعربية)](CONTRIBUTING.ar-SA.md)**
**[Czytaj po Polsku](CONTRIBUTING.pl-PL.md)**
**[Read in Hindi (हिंदी में पढ़ें)](CONTRIBUTING.hi-IN.md)**
**[Read in Thai (อ่านเป็นภาษาไทย)](CONTRIBUTING.th-TH.md)**

Antes de mais, obrigado por considerares contribuir para o Albion Insight! São pessoas como tu que fazem do Albion Insight uma ferramenta tão boa para a comunidade do Albion Online.

## Tabela de Conteúdos

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
  - [Reportar Erros](#reportar-erros)
  - [Sugerir Funcionalidades](#sugerir-funcionalidades)
  - [Contribuições de Código](#contribuições-de-código)
  - [Documentação](#documentação)
- [Configuração do Ambiente de Desenvolvimento](#configuração-do-ambiente-de-desenvolvimento)
- [Padrões de Codificação](#padrões-de-codificação)
- [Mensagens de Commit](#mensagens-de-commit)
- [Processo de Pull Request](#processo-de-pull-request)

## Código de Conduta

Este projeto e todos os que nele participam são regidos pelo nosso Código de Conduta. Ao participares, espera-se que cumpras este código. Por favor, reporta comportamentos inaceitáveis aos mantenedores do projeto.

## Como Posso Contribuir?

### Reportar Erros

Antes de criares relatórios de erros, por favor, verifica os problemas existentes para evitar duplicados. Quando criares um relatório de erro, inclui o máximo de detalhes possível usando o modelo de relatório de erro.

**Bons relatórios de erros incluem:**
- Um título claro e descritivo
- Passos exatos para reproduzir o problema
- Comportamento esperado vs. comportamento real
- Capturas de ecrã, se aplicável
- Detalhes do teu ambiente (SO, versão do Python, etc.)
- Registos ou mensagens de erro relevantes

### Sugerir Funcionalidades

Sugestões de funcionalidades são bem-vindas! Por favor, usa o modelo de pedido de funcionalidade e fornece:
- Uma descrição clara da funcionalidade
- O problema que ela resolve
- Possíveis abordagens de implementação
- Quaisquer alternativas que tenhas considerado

### Contribuições de Código

Adoramos contribuições de código! Eis como começar:

1. **Faz um fork do repositório** e cria o teu ramo a partir do `master`
2. **Configura o teu ambiente de desenvolvimento** (vê a Configuração do Ambiente de Desenvolvimento abaixo)
3. **Faz as tuas alterações** seguindo os nossos padrões de codificação
4. **Testa as tuas alterações** exaustivamente
5. **Atualiza a documentação**, se necessário
6. **Submete um pull request** usando o nosso modelo de PR

### Documentação

Melhorias na documentação são sempre apreciadas! Isto inclui:
- Ficheiros README
- Páginas da Wiki
- Comentários no código
- Tutoriais e guias
- Traduções para outras línguas

## Configuração do Ambiente de Desenvolvimento

### Pré-requisitos

- Python 3.8 ou superior
- Git
- Privilégios de Root/Administrador (para captura de pacotes)

### Configurar o Teu Ambiente

```bash
# Clona o teu fork
git clone https://github.com/O_TEU_UTILIZADOR/AlbionInsight.git
cd AlbionInsight

# Cria um ambiente virtual
python3 -m venv venv

# Ativa o ambiente virtual
# No Linux/macOS:
source venv/bin/activate
# No Windows:
venv\Scripts\activate

# Instala as dependências
pip install -r requirements.txt

# Instala as dependências de desenvolvimento
pip install pylint flake8 black pytest
```

### Executar a Aplicação

```bash
# No Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# No Windows (como Administrador):
python albion_insight.py
```

## Padrões de Codificação

Seguimos as diretrizes de estilo PEP 8 para o código Python. Por favor, garante que o teu código adere a estes padrões:

- Usa 4 espaços para indentação (sem tabulações)
- Comprimento máximo de linha de 100 caracteres
- Usa nomes de variáveis e funções significativos
- Adiciona docstrings a todas as funções e classes
- Inclui dicas de tipo (type hints) quando apropriado
- Mantém as funções focadas e concisas

**Ferramentas para ajudar:**
```bash
# Formata o teu código com o black
black albion_insight.py

# Verifica problemas de estilo
flake8 albion_insight.py

# Executa o linter
pylint albion_insight.py
```

## Mensagens de Commit

Escreve mensagens de commit claras e significativas:

- Usa o tempo presente ("Adiciona funcionalidade" e não "Adicionada funcionalidade")
- Usa o modo imperativo ("Move o cursor para..." e não "Move o cursor para...")
- Limita a primeira linha a 72 caracteres
- Refere problemas e pull requests quando relevante

**Exemplos:**
```
Adiciona funcionalidade de exportação do medidor de dano

Corrige a análise de pacotes de rede para ligações IPv6

Atualiza o README com instruções de instalação para macOS

Fecha #123
```

## Processo de Pull Request

1. **Atualiza a documentação** para quaisquer alterações na funcionalidade
2. **Adiciona testes** para novas funcionalidades ou correções de erros
3. **Garante que todos os testes passam** antes de submeter
4. **Atualiza o README.md**, se necessário
5. **Preenche o modelo de PR** completamente
6. **Liga os problemas relacionados** na tua descrição do PR
7. **Solicita a revisão** dos mantenedores
8. **Responde ao feedback** de forma rápida e profissional

### Lista de Verificação do PR

Antes de submeteres o teu PR, garante que:
- [ ] O código segue as diretrizes de estilo do projeto
- [ ] A auto-revisão foi concluída
- [ ] Foram adicionados comentários a secções de código complexas
- [ ] A documentação foi atualizada
- [ ] Não foram gerados novos avisos
- [ ] Foram adicionados testes e estes passam
- [ ] As alterações dependentes foram fundidas

## Perguntas?

Não hesites em fazer perguntas! Podes:
- Abrir um problema com a etiqueta "question"
- Juntar-te às nossas discussões da comunidade
- Contactar os mantenedores

Obrigado por contribuíres para o Albion Insight! Os teus esforços ajudam a tornar esta ferramenta melhor para toda a comunidade do Albion Online.
