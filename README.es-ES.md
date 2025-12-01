# Albion Insight (ES)

[![Licencia: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Versión Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Plataforma](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![Issues en GitHub](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contribuciones Bienvenidas](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** es una herramienta de análisis estadístico multiplataforma (Linux, Windows, macOS) para el juego Albion Online, reimplementada en **Python** con el framework **Flet**. Está diseñada para rastrear estadísticas en tiempo real dentro del juego, incluyendo plata, fama y datos de combate (Medidor de Daño), analizando el tráfico de red.

Este proyecto es una alternativa moderna y de código abierto a la herramienta original `AlbionOnline-StatisticsAnalysis` basada en C#/WPF, centrándose en la compatibilidad multiplataforma y la facilidad de uso.

## Características

*   **Compatibilidad Multiplataforma:** Se ejecuta de forma nativa en Linux, Windows y macOS.
*   **Seguimiento en Tiempo Real:** Utiliza la biblioteca `Scapy` para olfatear paquetes UDP en los puertos de Albion Online (5055, 5056, 5058).
*   **Estructura del Medidor de Daño:** Incluye las estructuras de datos y la interfaz de usuario necesarias para mostrar estadísticas de combate en vivo (Daño Infligido, Curación Realizada, DPS).
*   **Interfaz de Usuario Moderna:** Construida con Flet, proporcionando una aplicación de escritorio rápida y con apariencia nativa.
*   **Gestión de Sesiones:** Permite iniciar, detener, restablecer y guardar estadísticas de sesión.

## Requisitos Previos

*   Python 3.8+
*   Bibliotecas **Flet** y **Scapy**.
*   **Privilegios de Root/Administrador:** Necesarios para la captura de paquetes de red.

## Instalación y Configuración

### Opción 1: Instalación Rápida (Linux - Recomendado)

Para usuarios de Linux, proporcionamos scripts de instalación automatizados:

\`\`\`bash
# 1. Clonar el repositorio
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Ejecutar el script de instalación
./install.sh

# 3. Ejecutar la aplicación
./run.sh
\`\`\`

El script `install.sh` hará lo siguiente:
- Instalar dependencias del sistema (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Crear un entorno virtual de Python
- Instalar todos los paquetes de Python requeridos (Flet, Scapy)

El script `run.sh` solicitará automáticamente privilegios de root y ejecutará la aplicación.

### Opción 2: Instalación Manual

#### 1. Instalar Dependencias del Sistema

**En Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**En Windows:**

Instale Python 3.8+ desde [python.org](https://www.python.org/downloads/)

#### 2. Instalar Dependencias de Python

**En Linux (usando entorno virtual - recomendado):**

\`\`\`bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install flet scapy
\`\`\`

**En Linux (instalación a nivel de sistema):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**En Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Ejecutar la Aplicación

Dado que el olfateo de red requiere privilegios elevados, debe ejecutar la aplicación como root o administrador.

**En Linux (con entorno virtual):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**En Linux (instalación a nivel de sistema):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**En Windows (Ejecutar Símbolo del Sistema/PowerShell como Administrador):**

\`\`\`bash
python -m albion_insight
\`\`\`

La aplicación se abrirá en una ventana de escritorio nativa.

## Cómo Construir un Ejecutable

La aplicación se puede empaquetar en un ejecutable independiente utilizando **PyInstaller**. Esto permite a los usuarios ejecutar la aplicación sin instalar Python ni sus dependencias.

Para obtener instrucciones detalladas sobre cómo construir ejecutables para Linux, Windows y macOS, consulte la guía **[PACKAGING.md](PACKAGING.md)**.

### Construcción Rápida (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

El ejecutable se encontrará en la carpeta `dist/`.

## Estructura del Proyecto

La aplicación está estructurada en componentes modulares para una mejor mantenibilidad y escalabilidad:

| Archivo | Descripción |
| :--- | :--- |
| `albion_insight/core/` | Lógica central, seguimiento de red, modelos de datos y decodificación de protocolo. |
| `albion_insight/ui/` | Componentes de la interfaz de usuario construidos con Flet. |
| `albion_insight/utils/` | Funciones de utilidad, configuración y registro (logging). |
| `albion_insight/__main__.py` | Punto de entrada para la aplicación. |
| `README.md` | Este archivo de documentación principal (en Inglés). |
| `README.pt-BR.md` | Este archivo de documentación en Portugués de Brasil. |
| `README.fr-FR.md` | Este archivo de documentación en Francés. |
| `README.es-ES.md` | Este archivo de documentación en Español. |
| `CONTRIBUTING.md` | Directrices para la contribución al proyecto. |
| `CODE_OF_CONDUCT.md` | El Código de Conducta del proyecto. |
| `SECURITY.md` | Política para informar vulnerabilidades de seguridad. |

## Estado Actual (Datos en Tiempo Real)

La aplicación ahora incluye la lógica de **Decodificación del Protocolo Photon**, traducida del proyecto C# original. Esto permite que la aplicación procese eventos en tiempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` y `Died` directamente desde el tráfico de red.

**Nota:** La traducción completa de cada evento de combate (como `CastHit`, `Attack`) es un esfuerzo continuo. La implementación actual se centra en las estadísticas centrales y la estructura para el Medidor de Daño. El cálculo del DPS del Medidor de Daño se basa en los eventos decodificados.

## Contribución

¡Damos la bienvenida a las contribuciones de la comunidad! Ya seas desarrollador, diseñador o simplemente un entusiasta de Albion Online, hay muchas maneras de ayudar a mejorar Albion Insight.

Por favor, lee nuestras [Directrices de Contribución](CONTRIBUTING.md) para obtener información detallada sobre cómo contribuir a este proyecto.

### Inicio Rápido para Contribuidores:

1.  Haz un Fork del repositorio: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clona tu fork: `git clone https://github.com/TU_USUARIO/AlbionInsight.git`
3.  Crea una nueva rama: `git checkout -b feature/tu-nombre-de-caracteristica`
4.  Realiza tus cambios y haz commit: `git commit -m "Añadir tu característica"`
5.  Sube a tu fork: `git push origin feature/tu-nombre-de-caracteristica`
6.  Abre un Pull Request en el repositorio principal

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

- Proyecto original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) por Triky313
- Construido con el framework [Flet](https://flet.dev/)
- Análisis de red impulsado por [Scapy](https://scapy.net/)

---
*Una solución multiplataforma para la comunidad de Albion Online.*
