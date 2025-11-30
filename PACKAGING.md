# Empacotando o Albion Insight como um Executável Autônomo

Este guia explica como criar um executável autônomo para o **Albion Insight** usando **PyInstaller**. Isso permite que os usuários executem a aplicação sem instalar o Python ou suas dependências.

## Pré-requisitos

*   Python 3.8+ instalado
*   Ambiente virtual com todas as dependências instaladas (execute `./install.sh` primeiro)

## Instalação

Primeiro, instale o PyInstaller em seu ambiente virtual:

```bash
source venv/bin/activate
pip install pyinstaller
```

## Construindo o Executável

### Linux

```bash
source venv/bin/activate
pyinstaller --name "AlbionInsight" \
            --onefile \
            --windowed \
            --add-data "README.md:." \
            --add-data "README.pt-BR.md:." \
            --hidden-import scapy.layers.all \
            --hidden-import scapy.layers.inet \
            albion_insight.py
```

O executável estará localizado em `dist/AlbionInsight`.

**Nota:** No Linux, o executável ainda requer privilégios de root para capturar pacotes de rede:

```bash
sudo ./dist/AlbionInsight
```

### Windows

```bash
venv\Scripts\activate
pyinstaller --name "AlbionInsight" ^
            --onefile ^
            --windowed ^
            --add-data "README.md;." ^
            --add-data "README.pt-BR.md;." ^
            --hidden-import scapy.layers.all ^
            --hidden-import scapy.layers.inet ^
            albion_insight.py
```

O executável estará localizado em `dist\AlbionInsight.exe`.

**Nota:** No Windows, você deve executar o executável como Administrador (clique com o botão direito → Executar como Administrador).

### macOS

```bash
source venv/bin/activate
pyinstaller --name "AlbionInsight" \
            --onefile \
            --windowed \
            --add-data "README.md:." \
            --add-data "README.pt-BR.md:." \
            --hidden-import scapy.layers.all \
            --hidden-import scapy.layers.inet \
            albion_insight.py
```

O executável estará localizado em `dist/AlbionInsight`.

## Opções do PyInstaller Explicadas

*   `--name "AlbionInsight"`: Define o nome do arquivo executável.
*   `--onefile`: Cria um único arquivo executável (distribuição mais fácil).
*   `--windowed`: Oculta a janela do console (para aplicativos de desktop).
*   `--add-data`: Inclui arquivos adicionais (como README) no executável.
*   `--hidden-import`: Inclui explicitamente módulos que o PyInstaller pode ignorar (camadas do Scapy).

## Solução de Problemas

### Erros de "Módulo não encontrado"

Se você encontrar erros sobre módulos ausentes, adicione-os com `--hidden-import`:

```bash
--hidden-import nome_do_modulo
```

### Tamanho grande do executável

O executável terá cerca de 50-100 MB devido às dependências do Flet e Scapy. Isso é normal para aplicativos Python empacotados com PyInstaller.

### Falsos positivos de antivírus

Alguns softwares antivírus podem sinalizar o executável como suspeito. Este é um problema conhecido do PyInstaller. Você pode:

1.  Adicionar uma exceção no seu software antivírus.
2.  Assinar o executável com um certificado de assinatura de código (para lançamentos de produção).

## Distribuição

Após a construção, você pode distribuir o executável da pasta `dist/`. Os usuários não precisarão instalar o Python ou quaisquer dependências.

**Importante:** Sempre inclua um arquivo README explicando:

*   A aplicação requer privilégios de root/administrador.
*   Como executar a aplicação (ex: `sudo ./AlbionInsight` no Linux).
*   Quaisquer requisitos específicos do sistema (ex: `libpcap` no Linux).

## Criando um Release

Para criar um release no GitHub com o executável:

```bash
# 1. Construa o executável
./build.sh  # Ou siga os passos acima

# 2. Crie um release no GitHub
gh release create v0.0.2-beta \
    --title "Beta Release 0.0.2 - Executável Autônomo" \
    --notes "Inclui executável autônomo para Linux/Windows/macOS" \
    dist/AlbionInsight  # Anexe o executável
```

---

Para mais informações, consulte a [documentação do PyInstaller](https://pyinstaller.org/en/stable/).
