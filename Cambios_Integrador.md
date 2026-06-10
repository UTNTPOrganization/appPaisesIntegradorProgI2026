# Informe de Cambios - Integrador.py

Este documento detalla todas las modificaciones realizadas sobre el código original del archivo `Integrador.py` para cumplir con las consignas académicas del Trabajo Práctico Integrador de **Programación 1** de la UTN. 

Todas las soluciones se desarrollaron empleando **conceptos básicos de manejo de archivos y estructuras de datos**, evitando módulos complejos o métodos avanzados que excedan el programa de estudio de primer año.

---

## Detalle de Modificaciones Realizadas

### 1. Robustez en la Carga de Datos (`cargar_paises`)
* **Problema anterior**: Si el archivo `paises.csv` contenía valores no numéricos en población o superficie, la función `int()` lanzaba `ValueError` e interrumpía el programa completo. Además, si el archivo CSV no existía, el sistema lo notificaba pero no creaba un archivo válido para futuras operaciones de escritura.
* **Solución aplicada**:
  - Se envolvió la asignación y conversión del diccionario `pais` dentro de un bloque `try...except ValueError` dentro del bucle. Si una línea tiene datos corruptos o valores numéricos inválidos, se ignora esa fila específica (`continue`) y el programa continúa cargando los demás países de forma normal.
  - Se agregó una sección dentro de `except FileNotFoundError` que crea de manera automática el archivo `paises.csv` y escribe su respectivo encabezado (`nombre,poblacion,superficie,continente\n`) usando operaciones de archivo básicas (`open(..., 'w')` y `write(...)`). Esto previene corrupciones y asegura que las futuras escrituras en modo append funcionen correctamente.

### 2. Estandarización y Manejo de Continentes con Tildes (`validar_continente`)
* **Problema anterior**: La validación solo permitía el ingreso de continentes en minúscula sin tilde (como `"america"`) y los capitalizaba de forma directa a `"America"`. Esto no coincidía si en el archivo CSV o en los criterios oficiales de la consigna se usaban nombres con tilde (como `"América"` u `"Oceanía"`), rompiendo las búsquedas y filtros.
* **Solución aplicada**:
  - Se definió un diccionario de mapeo global `CONTINENTES_MAPA` que asocia entradas tanto con tilde como sin tilde al formato de escritura estándar (ej. `"america"` y `"américa"` se mapean a `"América"`).
  - Al cargar los datos desde el CSV, se normaliza el continente mediante este diccionario antes de almacenarlo en memoria.
  - La función `validar_continente()` consulta este diccionario para validar y devolver siempre la versión estandarizada del continente, eliminando incompatibilidades por tildes y mayúsculas.

### 3. Evitar Duplicidad al Agregar Países (`agregar_pais`)
* **Problema anterior**: Al agregar un país, el sistema no verificaba si el nombre ya existía en la base de datos, lo que generaba registros duplicados en el archivo CSV.
* **Solución aplicada**:
  - Se añadió una comprobación de existencia previa en la lista `paises` de manera insensible a mayúsculas/minúsculas. Si el país ya existe, el programa muestra un error y cancela la operación de agregado.
  - Se estandarizó el nombre del país usando `.title()` (por ejemplo, convirtiendo `"reino unido"` en `"Reino Unido"`) para mantener consistencia visual.

### 4. Corrección de Escritura del CSV (`guardar_pais_csv`)
* **Problema anterior**: Al agregar un país al CSV en modo append (`"a"`), el script escribía un carácter de nueva línea inicial (`\n`) redundante, provocando la aparición de líneas en blanco acumulativas en el archivo `paises.csv`.
* **Solución aplicada**:
  - Se modificó la escritura para guardar cada registro finalizando con `\n` en lugar de comenzar con él, sincronizándolo con el formato de escritura del resto de las funciones y manteniendo el archivo CSV limpio y sin registros vacíos.

### 5. Validación de Rangos y Control de Resultados en Filtros
* **Problema anterior**: En los filtros de rango de población y de superficie no se controlaba que el valor mínimo ingresado por el usuario fuera menor o igual al máximo. Asimismo, si ningún país coincidía con el criterio de filtrado, la consola no devolvía ningún mensaje informativo.
* **Solución aplicada**:
  - Se implementó un bucle `while True` en las funciones `filtrar_poblacion()` y `filtrar_superficie()` que obliga a ingresar un rango válido (`minimo <= maximo`) antes de proceder con el filtrado.
  - Se añadió una bandera booleana (`encontrados`) para rastrear si se mostraron países. Si tras iterar la lista de países no hay coincidencias, se muestra un mensaje informativo claro en pantalla: `"No se encontraron países en ese rango..."`.

### 6. Estandarización de Búsqueda y Actualización
* **Problema anterior**: En `actualizar_pais()` y `buscar_pais()`, el programa aceptaba entradas de texto que podían estar vacías, lo que causaba comportamientos inesperados o listados parciales.
* **Solución aplicada**:
  - Se agregaron controles para evitar entradas vacías (`strip() == ""`).
  - Al realizar una actualización, el sistema primero muestra en pantalla una ficha formateada con los datos actuales del país antes de solicitar los nuevos valores numéricos.

### 7. Formato Estético de Consola (`mostrar_pais_formateado`)
* **Problema anterior**: Al realizar búsquedas, ordenamientos o filtros, el programa imprimía en pantalla los objetos diccionarios tal y como Python los almacena en memoria (ej. `{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'}`), lo cual dificultaba la lectura.
* **Solución aplicada**:
  - Se implementó la función `mostrar_pais_formateado(pais)`, la cual se encarga de presentar la información de cada país estructurada en columnas alineadas.
  - Se formatearon las cifras numéricas grandes agregando puntos como separadores de miles (ej. `45.376.763` en lugar de `45376763`), mejorando la legibilidad de la información.

### 8. Ordenamiento Case-Insensitive (`ordenar_paises`)
* **Problema anterior**: Al ordenar países por nombre de forma alfabética, Python priorizaba las letras mayúsculas por encima de las minúsculas según la codificación ASCII (provocando que `"alemania"` se ordenara después de `"Brasil"`).
* **Solución aplicada**:
  - Se implementó ordenamiento por **método de burbuja** con bucles `for` anidados, comparando nombres con `.lower()` para no distinguir mayúsculas.
  - Se agregó validación al orden ("A" para ascendente y "D" para descendente), impidiendo que opciones inválidas rompan el flujo de ejecución.
  - Se copia la lista `paises` a `ordenados` antes de ordenar, para no modificar los datos originales en memoria.

### 9. Modularización y Documentación Completa
* **Problema anterior**: La rúbrica penaliza los códigos que no contienen comentarios o docstrings explicando la finalidad de las funciones.
* **Solución aplicada**:
  - Se añadió un **docstring descriptivo** en formato estándar a cada una de las funciones del archivo `Integrador.py`, detallando su funcionamiento general, parámetros de entrada y valores de retorno.

### 10. Corrección del Dataset Base (`paises.csv`)
* **Problema detectado en la revisión**: El archivo CSV contenía datos de prueba inconsistentes (población y superficie en `1` para Argentina, nombres en minúscula como `brasil` y `alemania`, continente escrito como `America` sin tilde). Esto no coincidía con el ejemplo oficial de la consigna y podía generar estadísticas irreales en la demostración del video.
* **Solución aplicada**:
  - Se reemplazó el contenido por el dataset de referencia de la consigna: Argentina, Japón, Brasil y Alemania, con valores reales de población y superficie, y continentes con tilde (`América`, `Asia`, `Europa`).

### 11. Normalización de Entrada en el Menú Principal
* **Problema detectado en la revisión**: La opción del menú principal no aplicaba `.strip()` al `input`, a diferencia del resto de los menús del sistema. Un espacio accidental antes o después del número podía interpretarse como opción inválida.
* **Solución aplicada**:
  - Se agregó `.strip()` al `input` de la opción del menú principal en el bloque `if __name__ == "__main__"`.

### 12. Creación de `README.md` (entregable obligatorio)
* **Problema detectado en la revisión**: La consigna y la rúbrica exigen un `README.md` en la raíz del repositorio con descripción del programa, instrucciones de uso, ejemplos de entrada/salida, participación de integrantes y enlaces al video y al PDF. El repositorio no lo tenía.
* **Solución aplicada**:
  - Se creó `README.md` con: descripción del proyecto, estructura sugerida del repo, requisitos, instrucciones de ejecución, ejemplos de consola, formato del CSV, checklist de entrega, guía para subir a la rama `ramaRevision` con token classic de GitHub y convención de commits `PROY-N`.

---

## Revisión contra Consigna y Rúbrica (junio 2025)

Revisión realizada sobre:
- `Consigna_TPI_Prog-1.docx.pdf`
- `Rúbrica de corrección - Programacion 1.pdf`
- `Integrador Programación 1 2 C 2025.pdf`
- `Integrador.py`
- `paises.csv`
- `Informe_TPI_Paises.pdf` *(informe del compañero, editado en esta revisión)*

### Estado del código (`Integrador.py`) — Cumple los requisitos mínimos

| Requisito de la consigna | Estado |
|--------------------------|--------|
| Agregar país (sin campos vacíos) | ✅ `validar_texto`, `validar_numero`, `validar_continente` |
| Actualizar población y superficie | ✅ `actualizar_pais` |
| Buscar por nombre (parcial o exacta) | ✅ `buscar_pais` |
| Filtrar por continente, población y superficie | ✅ `menu_filtros` |
| Ordenar por nombre, población, superficie (A/D) | ✅ `ordenar_paises` |
| Estadísticas (mayor/menor, promedios, por continente) | ✅ `mostrar_estadisticas` |
| Lectura CSV con manejo de errores | ✅ `cargar_paises` con `try/except` |
| Código modularizado con funciones | ✅ |
| Validaciones y mensajes claros | ✅ |

### Puntos de atención para maximizar la nota

**Código (ya resuelto o menor prioridad):**
- El CSV base ya usa datos coherentes con la consigna.
- El repositorio incluye `__pycache__/` sin `.gitignore`; conviene agregar un `.gitignore` con `__pycache__/` antes del push final.

**Entregables pendientes (críticos — reglas excluyentes de la rúbrica):**

| Entregable | Estado | Acción requerida |
|------------|--------|------------------|
| `README.md` | ✅ Creado | Completar nombres de integrantes y links al video/PDF |
| `Informe_TPI_Paises.pdf` | ✅ Editado | Completar integrantes, capturas reales y URL del video |
| Video 10–15 min | ⚠️ Pendiente | Ambos integrantes a cámara al inicio; mostrar todos los flujos |
| Repositorio público | ⚠️ Verificar | Debe ser accesible con CSV incluido |
| `.zip` de entrega | ⚠️ Pendiente | Código fuente + PDF del informe |

---

## Recomendaciones para `Informe_TPI_Paises.pdf`

El archivo **no se encontró** en la carpeta del proyecto. Según la consigna y la rúbrica (30% del puntaje), el informe debe incluir obligatoriamente:

### Estructura sugerida (basada en consigna + tutorial UTN)

1. **Carátula**
   - UTN — TUPaD, Programación 1, título del TPI, nombres de integrantes, fecha.

2. **Índice**
   - Con numeración de páginas.

3. **Marco teórico** *(15 pts — conceptos fundamentales)*
   - Explicar y **relacionar con el proyecto** (no solo definir):
     - Listas → `paises = []`
     - Diccionarios → cada país como `{"nombre": ..., "poblacion": ..., ...}`
     - Funciones → modularización (`agregar_pais`, `filtrar_poblacion`, etc.)
     - Condicionales → menús, validaciones
     - Ordenamientos → método de burbuja con bucles `for`
     - Estadísticas básicas → recorrido con `for`, acumuladores y promedios
     - Archivos CSV → `cargar_paises`, `guardar_pais_csv`
   - Mínimo **3 fuentes** citadas correctamente (APA básico): Python Docs, material de cátedra, artículo técnico.

4. **Decisiones técnicas y arquitectura** *(diagrama de flujo obligatorio)*
   - Diagrama del flujo: carga CSV → menú → opciones (agregar / buscar / filtrar / ordenar / estadísticas).
   - **Capturas de pantalla** de cada funcionalidad ejecutándose en consola (la rúbrica las valora en "Carpeta Digital").

5. **Dificultades y conclusiones** *(5 pts)*
   - Obstáculos: normalización de continentes con tildes, validación de rangos, líneas corruptas en CSV.
   - Aprendizajes sobre estructuras de datos, modularidad y persistencia en archivos.

6. **Bibliografía / Webgrafía**
   - Links a documentación oficial de Python y fuentes usadas.

7. **Anexos / Links**
   - Link al repositorio: `https://github.com/alevanfof/appPaisesIntegradorProgI2026`
   - Link al video demostrativo (cuando esté disponible).

### Contenido que conviene mencionar en el informe (alineado con `Cambios_Integrador.md`)

Documentar las mejoras aplicadas al código original, especialmente:
- Manejo de `ValueError` al cargar CSV corrupto.
- Diccionario `CONTINENTES_MAPA` para tildes.
- Validación anti-duplicados al agregar países.
- Control de rangos mínimo/máximo en filtros.
- Función `mostrar_pais_formateado` para salida legible.

### 13. Mejora de comentarios en `Integrador.py`
* **Motivo**: La rúbrica valora legibilidad y comentarios; conviene documentar la lógica no obvia dentro de cada función, no solo los docstrings.
* **Solución aplicada**:
  - Encabezado general del archivo con propósito del sistema.
  - Comentarios en `cargar_paises`: salto de encabezado, filas inválidas, normalización de continentes, creación de CSV vacío.
  - Comentarios en persistencia: diferencia entre `guardar_pais_csv` (append) y `guardar_todos_los_paises_csv` (sobrescritura).
  - Comentarios en validaciones: nombres compuestos, captura de `ValueError`, estandarización de continentes.
  - Comentarios en operaciones CRUD: anti-duplicados, actualización parcial, búsqueda parcial, bandera `encontrados`.
  - Comentarios en filtros y ordenamiento: rangos inclusivos, burbuja sin mutar la lista original.
  - Comentarios en estadísticas: formato numérico local y conteo por continente con diccionario auxiliar.
  - Comentarios en el bloque principal: carga inicial y bucle del menú.

### 14. Adecuación al programa de 1er año UTN (sin conceptos avanzados)
* **Motivo**: El código debía usar solo contenidos vistos en Programación 1 — 1er cuatrimestre: funciones, listas, diccionarios, condicionales, bucles, archivos y estructuras básicas. No se vio `lambda` ni funciones de ordenamiento avanzadas.
* **Solución aplicada**:
  - **`ordenar_paises`**: se reemplazó `sorted()` con `lambda` por **ordenamiento de burbuja** con `for` anidados.
  - **`mostrar_estadisticas`**: se reemplazó `max()`, `min()` y `sum()` con generadores por recorridos `for` y variables acumuladoras.
  - **Conteo por continente**: se reemplazó `.get()` por `if continente in continentes` / `else`.
  - **`cargar_paises`**: se reemplazó `CONTINENTES_MAPA.get()` por `if` / `else`; `next(archivo)` por `readline()`.
  - **Listado de continentes**: se ordenan alfabéticamente con burbuja en lugar de `sorted(continentes.items())`.

### 15. Revisión y edición de `Informe_TPI_Paises.pdf` (informe del compañero)

Se revisó el PDF existente contra la consigna, la rúbrica y el código actual de `Integrador.py`. **No se generó un informe nuevo**: se editó el archivo original del compañero. Copia de seguridad: `Informe_TPI_Paises_backup.pdf`.

#### Hallazgos de la revisión (antes de editar)

| Requisito de la consigna | Estado inicial |
|--------------------------|----------------|
| Carátula con datos institucionales | ✅ Presente (faltan nombres reales de integrantes) |
| Índice con páginas | ⚠️ Presente pero incompleto |
| Diagrama de flujo | ✅ Presente (pág. 9–10) |
| Capturas de pantalla | ❌ Faltaban |
| Dificultades y conclusiones | ❌ Faltaban |
| Bibliografía (≥3 fuentes) | ✅ Presente |
| Links repositorio y video | ❌ Faltaban |

#### Cambios aplicados al PDF

1. **Marco teórico — Listas (1.1)**: se quitó comprensiones y `sorted()`; se dejó `append()` y `for`.
2. **Marco teórico — Diccionarios (1.2)**: ejemplo con `"América"` (con tilde).
3. **Marco teórico — Ordenamientos (1.5)**: se reemplazó `sorted()` + `lambda` por **método de burbuja**, alineado con `Integrador.py`.
4. **Marco teórico — Estadísticas (1.6)**: se reemplazó `max()`, `min()`, `sum()` y `.get()` por `for` y acumuladores.
5. **Marco teórico — CSV (1.7)**: se actualizó a `readline()`, `try/except`, tildes y funciones de guardado correctas.
6. **Decisiones técnicas (2.1)**: tabla corregida (`guardar_todos_los_paises_csv()`, burbuja, acumuladores).
7. **Índice (pág. 2)**: actualizado con secciones nuevas.
8. **Sección 2.3 Capturas (pág. 11)**: agregada con placeholders para imágenes reales.
9. **Sección 3 Dificultades y Conclusiones (pág. 12)**: agregada (exigida por consigna).
10. **Bibliografía (pág. 13)**: reescrita sin referencias a `sorted()`/`lambda`.
11. **Sección 5 Enlaces (pág. 14)**: link al repo; placeholder para video.

#### Pendientes manuales antes de entregar

- [ ] Reemplazar **"Alumno 1 — Alumno 2"** en la carátula por nombres y legajos reales.
- [ ] Insertar **capturas de pantalla reales** en la sección 2.3.
- [ ] Completar la **URL del video** en la sección 5 y en el `README.md`.
- [x] Actualizar nombres de integrantes y fecha en `Informe_TPI_Paises.pdf`.
- [x] Corregir el índice del PDF para que refleje las secciones y páginas reales.

