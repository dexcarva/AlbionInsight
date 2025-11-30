# Contribuyendo a Albion Insight

**[Read in English](CONTRIBUTING.md)**

En primer lugar, ¡gracias por considerar contribuir a Albion Insight! Son personas como tú las que hacen de Albion Insight una herramienta tan valiosa para la comunidad de Albion Online.

## Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [¿Cómo Puedo Contribuir?](#cómo-puedo-contribuir)
  - [Reportar Errores](#reportar-errores)
  - [Sugerir Funcionalidades](#sugerir-funcionalidades)
  - [Contribuciones de Código](#contribuciones-de-código)
  - [Documentación](#documentación)
- [Configuración del Entorno de Desarrollo](#configuración-del-entorno-de-desarrollo)
- [Estándares de Codificación](#estándares-de-codificación)
- [Mensajes de Commit](#mensajes-de-commit)
- [Proceso de Solicitud de Extracción (Pull Request)](#proceso-de-solicitud-de-extracción-pull-request)

## Código de Conducta

Este proyecto y todos los que participan en él se rigen por nuestro Código de Conducta. Al participar, se espera que usted mantenga este código. Por favor, informe de comportamientos inaceptables a los mantenedores del proyecto.

## ¿Cómo Puedo Contribuir?

### Reportar Errores

Antes de crear informes de errores, por favor, revise los problemas existentes para evitar duplicados. Cuando cree un informe de error, incluya tantos detalles como sea posible utilizando la plantilla de informe de error.

**Los buenos informes de errores incluyen:**
- Un título claro y descriptivo
- Pasos exactos para reproducir el problema
- Comportamiento esperado frente a comportamiento real
- Capturas de pantalla si son aplicables
- Los detalles de su entorno (SO, versión de Python, etc.)
- Registros o mensajes de error relevantes

### Sugerir Funcionalidades

¡Las sugerencias de funcionalidades son bienvenidas! Por favor, utilice la plantilla de solicitud de funcionalidad y proporcione:
- Una descripción clara de la funcionalidad
- El problema que resuelve
- Posibles enfoques de implementación
- Cualquier alternativa que haya considerado

### Contribuciones de Código

¡Nos encantan las contribuciones de código! Aquí le explicamos cómo empezar:

1. **Bifurque el repositorio (Fork)** y cree su rama a partir de `master`
2. **Configure su entorno de desarrollo** (vea Configuración del Entorno de Desarrollo a continuación)
3. **Realice sus cambios** siguiendo nuestros estándares de codificación
4. **Pruebe sus cambios** a fondo
5. **Actualice la documentación** si es necesario
6. **Envíe una solicitud de extracción (Pull Request)** utilizando nuestra plantilla de PR

### Documentación

¡Las mejoras en la documentación siempre son apreciadas! Esto incluye:
- Archivos README
- Páginas Wiki
- Comentarios en el código
- Tutoriales y guías
- Traducciones a otros idiomas

## Configuración del Entorno de Desarrollo

### Requisitos Previos

- Python 3.8 o superior
- Git
- Privilegios de Root/Administrador (para la captura de paquetes)

### Configuración de Su Entorno

```bash
# Clonar su bifurcación
git clone https://github.com/SU_NOMBRE_DE_USUARIO/AlbionInsight.git
cd AlbionInsight

# Crear un entorno virtual
python3 -m venv venv

# Activar el entorno virtual
# En Linux/macOS:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Instalar dependencias de desarrollo
pip install pylint flake8 black pytest
```

### Ejecutar la Aplicación

```bash
# En Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# En Windows (como Administrador):
python albion_insight.py
```

## Estándares de Codificación

Seguimos las directrices de estilo PEP 8 para el código Python. Por favor, asegúrese de que su código se adhiere a estos estándares:

- Utilice 4 espacios para la indentación (sin tabulaciones)
- Longitud máxima de línea de 100 caracteres
- Utilice nombres de variables y funciones significativos
- Agregue docstrings a todas las funciones y clases
- Incluya sugerencias de tipo (type hints) cuando sea apropiado
- Mantenga las funciones enfocadas y concisas

**Herramientas para ayudar:**
```bash
# Formatee su código con black
black albion_insight.py

# Verifique problemas de estilo
flake8 albion_insight.py

# Ejecute el linter
pylint albion_insight.py
```

## Mensajes de Commit

Escriba mensajes de commit claros y significativos:

- Utilice el tiempo presente ("Añadir funcionalidad" y no "Añadió funcionalidad")
- Utilice el modo imperativo ("Mover el cursor a..." y no "Mueve el cursor a...")
- Limite la primera línea a 72 caracteres
- Referencie problemas y solicitudes de extracción cuando sea relevante

**Ejemplos:**
```
Añadir funcionalidad de exportación del medidor de daño

Corregir el análisis de paquetes de red para conexiones IPv6

Actualizar README con instrucciones de instalación para macOS

Cierra #123
```

## Proceso de Solicitud de Extracción (Pull Request)

1. **Actualice la documentación** para cualquier cambio en la funcionalidad
2. **Agregue pruebas** para nuevas funcionalidades o correcciones de errores
3. **Asegúrese de que todas las pruebas pasen** antes de enviar
4. **Actualice el README.md** si es necesario
5. **Rellene la plantilla de PR** completamente
6. **Vincule problemas relacionados** en la descripción de su PR
7. **Solicite revisión** a los mantenedores
8. **Aborde los comentarios** de manera rápida y profesional

### Lista de Verificación de PR

Antes de enviar su PR, asegúrese de que:
- [ ] El código sigue las directrices de estilo del proyecto
- [ ] La auto-revisión está completa
- [ ] Se añaden comentarios a las secciones de código complejas
- [ ] La documentación está actualizada
- [ ] No se generan nuevas advertencias
- [ ] Las pruebas se añaden y pasan
- [ ] Los cambios dependientes se fusionan

## ¿Preguntas?

¡No dude en hacer preguntas! Puede:
- Abrir un problema con la etiqueta "question"
- Unirse a nuestras discusiones comunitarias
- Ponerse en contacto con los mantenedores

¡Gracias por contribuir a Albion Insight! Sus esfuerzos ayudan a mejorar esta herramienta para toda la comunidad de Albion Online.
