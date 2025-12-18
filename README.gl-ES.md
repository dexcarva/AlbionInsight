[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** é unha ferramenta de análise de estatísticas multiplataforma (Linux, Windows, macOS) para o xogo Albion Online, reimplementada en **Python** usando o framework **Flet**. Está deseñada para rastrexar estatísticas en tempo real dentro do xogo, incluíndo prata, fama e datos de combate (Medidor de Dano), analizando o tráfico de rede.

Este proxecto é unha alternativa moderna e de código aberto á ferramenta orixinal `AlbionOnline-StatisticsAnalysis` baseada en C#/WPF, centrándose na compatibilidade multiplataforma e na facilidade de uso.

## Características

*   **Compatibilidade Multiplataforma:** Execútase de forma nativa en Linux, Windows e macOS.
*   **Rastrexo en Tempo Real:** Utiliza a biblioteca `Scapy` para cheirar paquetes UDP nos portos de Albion Online (5055, 5056, 5058).
*   **Estrutura do Medidor de Dano:** Inclúe as estruturas de datos e a interface de usuario necesarias para mostrar estatísticas de combate en vivo (Dano Feito, Curación Feita, DPS).
*   **Interface de Usuario Moderna:** Construída con Flet, proporcionando unha aplicación de escritorio rápida e con aspecto nativo.
*   **Xestión de Sesións:** Permite iniciar, deter, restablecer e gardar as estatísticas da sesión.

## Requisitos Previos

*   Python 3.8+
*   Bibliotecas **Flet** e **Scapy**.
*   **Privilexios de Root/Administrador:** Necesarios para a captura de paquetes de rede.

## Instalación e Configuración

### Opción 1: Instalación Rápida (Linux - Recomendado)

Para os usuarios de Linux, proporcionamos scripts de instalación automatizados:

```bash
# 1. Clonar o repositorio
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Executar o script de instalación
./install.sh

# 3. Executar a aplicación
./run.sh
```

O script `install.sh` fará o seguinte:
- Instalar dependencias do sistema (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Crear un ambiente virtual de Python
- Instalar todos os paquetes de Python requiridos (Flet, Scapy)

O script `run.sh` solicitará automaticamente privilexios de root e executará a aplicación.

### Opción 2: Instalación Manual

#### 1. Instalar Dependencias do Sistema

**En Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**En Windows:**

Instalar Python 3.8+ dende [python.org](https://www.python.org/downloads/)

#### 2. Instalar Dependencias de Python

**En Linux (usando ambiente virtual - recomendado):**

```bash
# Crear ambiente virtual
python3 -m venv venv

# Activar ambiente virtual
source venv/bin/activate

# Instalar dependencias
pip install flet scapy
```

**En Linux (instalación a nivel de sistema):**

```bash
pip3 install flet scapy --break-system-packages
```

**En Windows:**

```bash
pip install flet scapy
```

#### 3. Executar a Aplicación

Dado que o cheirado de rede require privilexios elevados, debe executar a aplicación como root ou administrador.

**En Linux (con ambiente virtual):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**En Linux (instalación a nivel de sistema):**

```bash
sudo python3 -m albion_insight
```

**En Windows (Executar Símbolo do Sistema/PowerShell como Administrador):**

```bash
python -m albion_insight
```

A aplicación abrirase nunha xanela de escritorio nativa.

## Como Construír un Executable

A aplicación pódese empaquetar nun executable autónomo usando **PyInstaller**. Isto permite aos usuarios executar a aplicación sen instalar Python nin as súas dependencias.

Para instrucións detalladas sobre a construción de executables para Linux, Windows e macOS, consulte a guía **[PACKAGING.md](PACKAGING.md)**.

### Construción Rápida (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

O executable estará situado no cartafol `dist/`.

## Estrutura do Proxecto

A aplicación está estruturada en compoñentes modulares para unha mellor mantibilidade e escalabilidade:

| Ficheiro | Descrición |
| :--- | :--- |
| `albion_insight/core/` | Lóxica central, rastrexo de rede, modelos de datos e decodificación de protocolos. |
| `albion_insight/ui/` | Compoñentes da interface de usuario construídos con Flet. |
| `albion_insight/utils/` | Funcións de utilidade, configuración e rexistro. |
| `albion_insight/__main__.py` | Punto de entrada para a aplicación. |
| `README.md` | Esta documentación (Inglés). |
| `CONTRIBUTING.md` | Directrices para contribuír ao proxecto. |
| `CODE_OF_CONDUCT.md` | Código de Conduta do proxecto. |
| `SECURITY.md` | Política para informar de vulnerabilidades de seguridade. |
| `README.ar-SA.md` | توثيق باللغة العربية (Documentación en árabe). |
| `README.ca-ES.md` | Documentació en català (Documentación en catalán). |
| `README.cs-CZ.md` | Dokumentace v češtině (Documentación en checo). |
| `README.da-DK.md` | Dokumentation på dansk (Documentación en danés). |
| `README.de-DE.md` | Dokumentation in deutscher Sprache (Documentación en alemán). |
| `README.el-GR.md` | Τεκμηρίωση στα Ελληνικά (Documentación en grego). |
| `README.es-ES.md` | Documentación en español (Documentación en español). |
| `README.fa-IR.md` | مستندات به زبان فارسی (Documentación en persa). |
| `README.fi-FI.md` | Dokumentaatio suomeksi (Documentación en finés). |
| `README.fi.md` | Dokumentaatio suomeksi (Documentación en finés - Xenérico). |
| `README.fil-PH.md` | Dokumentasyon sa Filipino (Documentación en filipino). |
| `README.fr-FR.md` | Documentation en français (Documentación en francés). |
| `README.gl-ES.md` | Documentación en galego (Galician documentation). |
| `README.he-IL.md` | תיעוד בעברית (Documentación en hebreo). |
| `README.hi-IN.md` | Hindi में दस्तावेज़ीकरण (Documentación en hindi). |
| `README.hu-HU.md` | Dokumentáció magyar nyelven (Documentación en húngaro). |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia (Documentación en indonesio). |
| `README.it-IT.md` | Documentazione in italiano (Documentación en italiano). |
| `README.ja-JP.md` | 日本語のドキュメント (Documentación en xaponés). |
| `README.ko-KR.md` | 한국어 문서 (Documentación en coreano). |
| `README.lt-LT.md` | Dokumentacija lietuvių kalba (Documentación en lituano). |
| `README.lv-LV.md` | Dokumentācija latviešu valodā (Documentación en letón). |
| `README.ne-NP.md` | नेपालीमा कागजात (Documentación en nepalés). |
| `README.nl-NL.md` | Documentatie in het Nederlands (Documentación en neerlandés). |
| `README.no-NO.md` | Dokumentasjon på norsk (Documentación en noruegués). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Documentación en polaco). |
| `README.pt-BR.md` | Documentação em português do Brasil (Documentação em portugués do Brasil). |
| `README.pt-PT.md` | Documentação em português europeu (Documentação en portugués europeo). |
| `README.ro-RO.md` | Documentație în română (Documentación en romanés). |
| `README.ru-RU.md` | Документация на русском языке (Documentación en ruso). |
| `README.sk-SK.md` | Dokumentácia v slovenčine (Documentación en eslovaco). |
| `README.sv-SE.md` | Dokumentation på svenska (Documentación en sueco). |
| `README.th-TH.md` | เอกสารประกอบภาษาไทย (Documentación en tailandés). |
| `README.tr-TR.md` | Türkçe dokümantasyon (Documentación en turco). |
| `README.uk-UA.md` | Документація українською мовою (Documentación en ucraíno). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (Documentación en vietnamita). |
| `README.zh-CN.md` | 简体中文文档 (Documentación en chinés simplificado). |
| `README.zh-TW.md` | 繁體中文文件 (Documentación en chinés tradicional). |
| `README.zu-ZA.md` | Imibhalo ngolimi lwesiZulu (Documentación en zulú). |

## Estado Actual (Datos en Tempo Real)

A aplicación agora inclúe a lóxica de **Decodificación do Protocolo Photon**, traducida do proxecto orixinal en C#. Isto permite á aplicación procesar eventos en tempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` directamente do tráfico de rede.

**Nota:** A tradución completa de cada evento de combate (como `CastHit`, `Attack`) é un esforzo continuo. A implementación actual céntrase nas estatísticas centrais e na estrutura para o Medidor de Dano. O cálculo de DPS do Medidor de Dano baséase nos eventos decodificados.

## Contribuíndo

Damos a benvida ás contribucións da comunidade! Tanto se es un desenvolvedor, deseñador ou simplemente un entusiasta de Albion Online, hai moitas formas de axudar a mellorar Albion Insight.

Por favor, lea as nosas [Directrices de Contribución](CONTRIBUTING.md) para obter información detallada sobre como contribuír a este proxecto.

### Inicio Rápido para Contribuíntes:

1.  Faga un fork do repositorio: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone o seu fork: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Cree unha nova rama: `git checkout -b feature/o-seu-nome-de-característica`
4.  Faga os seus cambios e commit: `git commit -m "Engadir a súa característica"`
5.  Faga push ao seu fork: `git push origin feature/o-seu-nome-de-característica`
6.  Abra un Pull Request no repositorio principal

## Licenza

Este proxecto está licenciado baixo a Licenza MIT - consulte o ficheiro [LICENSE](LICENSE) para obter detalles.

## Agradecementos

- Proxecto orixinal: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) por Triky313
- Construído co framework [Flet](https://flet.dev/)
- Análise de rede impulsada por [Scapy](https://scapy.net/)

---
*Unha solución multiplataforma para a comunidade de Albion Online.*
