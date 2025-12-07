# Albion Insight

**Albion Insight** es una herramienta de análisis de estadísticas multiplataforma (Linux, Windows, macOS) para el juego Albion Online, reimplementada en **Python** utilizando el framework **Flet**. Está diseñada para rastrear estadísticas en tiempo real dentro del juego, incluyendo plata, fama y datos de combate (Medidor de Daño), mediante el análisis del tráfico de red.

Este proyecto es una alternativa moderna y de código abierto al original `AlbionOnline-StatisticsAnalysis` basado en C#/WPF, centrándose en la compatibilidad multiplataforma y la facilidad de uso.

## Características

*   **Compatibilidad Multiplataforma:** Se ejecuta de forma nativa en Linux, Windows y macOS.
*   **Rastreo en Tiempo Real:** Utiliza la librería `Scapy` para olfatear paquetes UDP en los puertos de Albion Online (5055, 5056, 5058).
*   **Estructura del Medidor de Daño:** Incluye las estructuras de datos y la interfaz de usuario necesarias para mostrar estadísticas de combate en vivo (Daño Realizado, Curación Realizada, DPS).
*   **Interfaz de Usuario Moderna:** Construida con Flet, proporcionando una aplicación de escritorio rápida y con apariencia nativa.
*   **Gestión de Sesiones:** Permite iniciar, detener, restablecer y guardar estadísticas de sesión.

## Prerrequisitos

*   Python 3.8+
*   Librerías **Flet** y **Scapy**.
*   **Privilegios de Root/Administrador:** Necesarios para la captura de paquetes de red.

## Instalación y Configuración

*(Para instrucciones detalladas, consulte la sección de Instalación Manual en el README principal.)*

## Cómo Construir un Ejecutable

La aplicación se puede empaquetar en un ejecutable independiente utilizando **PyInstaller**.

*(Para instrucciones detalladas, consulte la guía **PACKAGING.md**.)*

## Estructura del Proyecto

El proyecto está estructurado en componentes modulares para una mejor mantenibilidad y escalabilidad.

## Estado Actual (Datos en Tiempo Real)

La aplicación ahora incluye la **Lógica de Decodificación del Protocolo Photon**, traducida del proyecto original en C#. Esto permite que la aplicación procese eventos en tiempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` y `Died` directamente desde el tráfico de red.

## Contribución

¡Damos la bienvenida a las contribuciones de la comunidad!

Por favor, lea nuestras [Guías de Contribución](CONTRIBUTING.md) para obtener información detallada sobre cómo contribuir a este proyecto.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulte el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

*   Proyecto original: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) por Triky313
*   Construido con el framework [Flet](https://flet.dev/)
*   Análisis de red impulsado por [Scapy](https://scapy.net/)

_Una solución multiplataforma para la comunidad de Albion Online._
