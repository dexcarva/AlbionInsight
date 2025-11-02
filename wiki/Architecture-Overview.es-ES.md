# Visión General de la Arquitectura

**[Read in English](Architecture-Overview.md)**
**[Leia em Português](Architecture-Overview.pt-BR.md)**

Este documento proporciona una visión general de alto nivel de la arquitectura de Albion Insight, explicando cómo los diferentes componentes trabajan juntos para rastrear y mostrar las estadísticas de Albion Online.

## Arquitectura del Sistema

Albion Insight sigue una arquitectura modular con tres capas principales:

### 1. Capa de Captura de Red

La capa de captura de red es responsable de interceptar y filtrar los paquetes de red de Albion Online. Esta capa utiliza la librería **Scapy** para realizar el olfateo de paquetes de bajo nivel.

**Componentes Clave:**
- **Olfateador de Paquetes (Packet Sniffer)**: Captura paquetes UDP en los puertos de Albion Online (5055, 5056, 5058)
- **Filtro de Paquetes (Packet Filter)**: Filtra el tráfico que no es de Albion para reducir la sobrecarga de procesamiento
- **Gestor de Búfer (Buffer Manager)**: Gestiona las colas de paquetes entrantes para prevenir la pérdida de datos

**Tecnologías:**
- Librería Python Scapy
- Acceso a sockets sin procesar (requiere privilegios de root/administrador)
- Manejo del protocolo UDP

### 2. Capa de Decodificación de Protocolo

Una vez que los paquetes son capturados, necesitan ser decodificados del formato del Protocolo Photon a eventos de juego significativos. Esta capa traduce la lógica de decodificación original de C# a Python.

**Componentes Clave:**
- **Decodificador Photon (Photon Decoder)**: Analiza los paquetes del Protocolo Photon
- **Despachador de Eventos (Event Dispatcher)**: Dirige los eventos decodificados a los manejadores apropiados
- **Manejadores de Eventos (Event Handlers)**: Procesan tipos de eventos específicos (UpdateMoney, UpdateFame, CastHit, etc.)
- **Gestor de Estado (State Manager)**: Mantiene el estado del juego y la información del jugador

**Estructura del Protocolo Photon:**
```
Paquete Photon
├── Cabecera
│   ├── Tipo de Protocolo
│   ├── Tipo de Comando
│   └── Número de Secuencia
└── Carga Útil (Payload)
    ├── Código de Evento
    ├── Contador de Parámetros
    └── Parámetros
        ├── Tipo
        ├── Clave
        └── Valor
```

**Tipos de Eventos Implementados Actualmente:**
- Actualizaciones de dinero (plata ganada/gastada)
- Actualizaciones de fama (fama ganada)
- Muertes y asesinatos de jugadores
- Eventos de combate (implementación parcial)

### 3. Capa de Interfaz de Usuario

La capa de UI presenta las estadísticas rastreadas al usuario en una interfaz limpia y con apariencia nativa. Construida con **Flet**, proporciona una experiencia de aplicación de escritorio multiplataforma.

**Componentes Clave:**
- **Ventana Principal (Main Window)**: Contenedor de la aplicación y navegación
- **Vista del Medidor de Daño (Damage Meter View)**: Visualización de estadísticas de combate en tiempo real
- **Gestor de Sesiones (Session Manager)**: Controles para iniciar, detener y guardar sesiones
- **Panel de Estadísticas (Statistics Dashboard)**: Resumen de los datos de la sesión
- **Módulo de Exportación (Export Module)**: Funcionalidad para guardar datos de la sesión

**Framework de UI:**
- Flet (Flutter para Python)
- Enlace de datos reactivo
- Componentes de Material Design

## Flujo de Datos

El siguiente diagrama ilustra cómo fluyen los datos a través del sistema:

```
Cliente de Albion Online
    ↓ (Paquetes UDP)
Interfaz de Red
    ↓
Captura de Paquetes Scapy
    ↓
Filtro de Paquetes
    ↓
Decodificador del Protocolo Photon
    ↓
Despachador de Eventos
    ↓ ↓ ↓
Manejadores de Eventos
    ↓
Gestor de Estado
    ↓
Enlace de Datos de UI
    ↓
Componentes de UI de Flet
    ↓
Visualización del Usuario
```

## Modelo de Hilos (Threading Model)

Albion Insight utiliza una arquitectura multihilo para asegurar una UI responsiva y un procesamiento eficiente de paquetes:

- **Hilo Principal (Main Thread)**: Ejecuta el bucle de eventos de la UI de Flet
- **Hilo de Captura (Capture Thread)**: Captura continuamente paquetes de red
- **Hilo de Procesamiento (Processing Thread)**: Decodifica y procesa eventos Photon
- **Hilo de Actualización de UI (UI Update Thread)**: Actualiza periódicamente la UI con nuevas estadísticas

**Comunicación entre Hilos:**
- Colas seguras para el paso de paquetes
- Bloqueos (Locks) para el acceso a estados compartidos
- Actualizaciones de UI impulsadas por eventos

## Estructura de Archivos

La aplicación está diseñada con simplicidad en mente, contenida principalmente en un solo archivo:

```
AlbionInsight/
├── albion_insight.py       # Archivo principal de la aplicación
│   ├── Modelos de Datos
│   ├── Captura de Red
│   ├── Decodificador Photon
│   ├── Manejadores de Eventos
│   ├── Gestión de Estado
│   └── UI de Flet
├── install.sh              # Script de instalación para Linux
├── run.sh                  # Script de ejecución para Linux
├── requirements.txt        # Dependencias de Python
├── README.md               # Documentación
└── PACKAGING.md            # Instrucciones de compilación
```

## Principios de Diseño

### 1. Compatibilidad Multiplataforma

Todos los componentes están diseñados para funcionar en Linux, Windows y macOS sin código específico de plataforma siempre que sea posible. Las diferencias de plataforma se manejan a través de capas de abstracción.

### 2. Dependencias Mínimas

El proyecto mantiene intencionalmente las dependencias al mínimo para simplificar la instalación y reducir posibles problemas de compatibilidad. Las dependencias principales son:
- Python 3.8+
- Flet (framework de UI)
- Scapy (captura de red)

### 3. Extensibilidad

El sistema de manejadores de eventos está diseñado para ser fácilmente extensible. Agregar soporte para nuevos eventos Photon requiere:
1. Identificar el código del evento
2. Crear una función manejadora
3. Registrar el manejador con el despachador

### 4. Rendimiento

Las optimizaciones de rendimiento incluyen:
- Filtrado eficiente de paquetes para reducir la carga de procesamiento
- Procesamiento asíncrono de eventos
- Carga perezosa (Lazy loading) de componentes de UI
- Mínima huella de memoria

## Comparación con el Proyecto Original

| Aspecto | AlbionOnline-StatisticsAnalysis | Albion Insight |
|--------|--------------------------------|----------------|
| Lenguaje | C# | Python |
| Framework de UI | WPF | Flet (Flutter) |
| Plataforma | Solo Windows | Multiplataforma |
| Librería de Red | Personalizada/Npcap | Scapy |
| Arquitectura | Solución de múltiples proyectos | Aplicación de un solo archivo |
| Cobertura de Eventos | Completa | Creciente (impulsada por la comunidad) |

## Futuras Mejoras Arquitectónicas

Las mejoras arquitectónicas planificadas incluyen:

1. **Sistema de Plugins**: Permitir extensiones desarrolladas por la comunidad
2. **Sistema de Configuración**: Archivos de configuración externos para personalización
3. **Integración de Base de Datos**: Almacenamiento persistente opcional para datos históricos
4. **Servidor API**: API REST para integraciones externas
5. **Estructura de Archivos Modular**: Dividir en múltiples módulos a medida que la complejidad crezca

## Contribuyendo a la Arquitectura

Si está interesado en contribuir a la arquitectura:

1. Revise las [Guías de Contribución](../CONTRIBUTING.md)
2. Discuta los principales cambios arquitectónicos primero en las Issues de GitHub
3. Asegure la compatibilidad con versiones anteriores cuando sea posible
4. Documente las decisiones arquitectónicas

---

*Última actualización: Octubre de 2025*
