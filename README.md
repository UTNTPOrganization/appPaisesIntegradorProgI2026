# Gestión de Datos de Países — TPI Programación 1

Aplicación en consola desarrollada en **Python 3** para gestionar información de países: carga desde CSV, altas, actualizaciones, búsquedas, filtros, ordenamientos y estadísticas.

**Materia:** Programación 1 — UTN TUPaD  
**Proyecto:** Trabajo Práctico Integrador (TPI)

---

## Integrantes

| Nombre | Legajo |
|----------|----------|
| Alejandro Fernández | [Legajo] |
| Josué Gallardo | [Legajo] |

> Completar los legajos antes de la entrega.

---

## Estructura del repositorio

```text
Integrador/
├── main.py                    # Punto de entrada y menú principal
├── datos.py                   # Carga y persistencia de datos CSV
├── validaciones.py            # Funciones de validación
├── operaciones.py             # Funcionalidades del sistema
├── paises.csv                 # Base de datos de países
├── README.md                  # Documentación del proyecto
├── Cambios_Integrador.md      # Registro de mejoras realizadas
├── Informe_TPI_Paises.pdf     # Informe académico
└── .gitignore                 # Exclusión de archivos temporales
```

### Descripción de módulos

- **main.py**: controla el flujo principal de ejecución y muestra el menú.
- **datos.py**: administra la carga y guardado de información en el archivo CSV.
- **validaciones.py**: contiene funciones reutilizables para validar textos, números y continentes.
- **operaciones.py**: implementa las operaciones del sistema (altas, búsquedas, filtros, ordenamientos y estadísticas).

---

## Enlaces obligatorios

| Recurso | Enlace |
|----------|----------|
| Video demostrativo (10–15 min) | https://www.youtube.com/watch?v=DCn2WmIa1L4 |
| Informe PDF | Informe_TPI_Paises.pdf |
| Repositorio GitHub | https://github.com/UTNTPOrganization/appPaisesIntegradorProgI2026 |

---

## Requisitos

- Python 3.x
- No requiere librerías externas

---

## Ejecución del programa

1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

El programa cargará automáticamente los datos desde `paises.csv` y mostrará el menú principal.

---

## Menú principal

```text
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Estadísticas
0. Salir
```

### Submenú de filtros

```text
1. Continente
2. Rango de población
3. Rango de superficie
```

---

## Ejemplos de uso

### Carga inicial

```text
CSV cargado correctamente.
```

### Agregar país

```text
Nombre del país: Uruguay
Población: 3477000
Superficie (km²): 176215
Continente (América, Europa, Asia, África, Oceanía): america

País agregado correctamente.
```

### Buscar país

```text
Ingrese nombre o parte del nombre a buscar: arg

Resultados de la búsqueda:

País: Argentina           | Continente: América    | Población:   45.376.763 hab. | Superficie: 2.780.400 km²
```

### Estadísticas

```text
--- ESTADISTICAS ---

Mayor población:    Brasil (213.993.437 hab.)
Menor población:    Alemania (83.149.300 hab.)

Promedio población: 117.027.625,00 hab.
Promedio superficie: 3.036.541,00 km²

Cantidad por continente:
- América: 2
- Asia: 1
- Europa: 1
```

---

## Formato del archivo CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

| Campo | Tipo | Descripción |
|---------|---------|---------|
| nombre | texto | Nombre del país |
| poblacion | entero | Cantidad de habitantes |
| superficie | entero | Superficie en km² |
| continente | texto | América, Europa, Asia, África u Oceanía |

---

## Flujo de trabajo con Git

### Verificar estado

```bash
git status
```

### Agregar cambios

```bash
git add .
```

### Crear commit

```bash
git commit -m "PROY-N: Descripción del cambio"
```

### Enviar cambios

```bash
git push origin main
```

---

## Convención de commits

| Prefijo | Uso |
|----------|----------|
| PROY-1 | Implementación inicial |
| PROY-2 | Nuevas funcionalidades |
| PROY-3 | Validaciones y correcciones |
| PROY-4 | Documentación |
| PROY-5 | Revisión final |

### Ejemplos

```bash
git commit -m "PROY-1: Crear estructura modular del proyecto"
git commit -m "PROY-2: Implementar filtros por continente"
git commit -m "PROY-3: Mejorar validaciones de entrada"
git commit -m "PROY-4: Actualizar documentación"
git commit -m "PROY-5: Corregir errores finales"
```

---

## Checklist de entrega

- [ ] Repositorio público en GitHub
- [ ] Código modularizado (`main.py`, `datos.py`, `validaciones.py`, `operaciones.py`)
- [ ] Archivo `paises.csv`
- [ ] README completo
- [ ] Informe PDF incluido
- [ ] Video de demostración (10–15 minutos)
- [ ] Archivo ZIP con código fuente e informe

---

## Licencia

Proyecto académico desarrollado para la carrera **TUPaD — UTN** en el marco de la materia **Programación 1**.