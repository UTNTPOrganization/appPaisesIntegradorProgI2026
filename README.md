# Gestión de Datos de Países — TPI Programación 1

Aplicación en consola desarrollada en **Python 3** para gestionar información de países: carga desde CSV, altas, actualizaciones, búsquedas, filtros, ordenamientos y estadísticas.

**Materia:** Programación 1 — UTN TUPaD  
**Proyecto:** Trabajo Práctico Integrador (TPI)

---

## Integrantes

| Nombre | Legajo / Rol |
|--------|--------------|
| [Alejandro Fernández 1] | [Legajo] |
| [Gallardo Josue 2] | [Legajo] |

> Completar con los datos reales del equipo antes de la entrega.

---

## Estructura del repositorio (sugerida)

```
Integrador/
├── Integrador.py              # Código principal del sistema
├── paises.csv                 # Dataset base de países
├── README.md                  # Este archivo (obligatorio)
├── Cambios_Integrador.md      # Registro de mejoras aplicadas al código
├── Informe_TPI_Paises.pdf     # Informe académico (obligatorio en el .zip)
└── .gitignore                 # (opcional) para excluir __pycache__/
```

### Enlaces obligatorios (completar antes de entregar)

| Recurso | Enlace |
|---------|--------|
| Video demostrativo (10–15 min, público) | `[PENDIENTE — pegar URL de YouTube/Drive]` |
| Informe PDF | `[PENDIENTE — enlace o archivo en raíz del repo]` |
| Repositorio GitHub | https://github.com/alevanfof/appPaisesIntegradorProgI2026 |

---

## Requisitos

- Python 3.x instalado
- No requiere librerías externas (solo módulos estándar)

---

## Instrucciones de ejecución

1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python Integrador.py
```

4. El programa carga automáticamente `paises.csv` y muestra el menú principal.

---

## Menú principal

```
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Estadísticas
0. Salir
```

### Submenú de filtros (opción 4)

```
1. Continente
2. Rango de población
3. Rango de superficie
```

---

## Ejemplos de entrada y salida

### Carga inicial del CSV

```
CSV cargado correctamente.
```

### Agregar un país (opción 1)

```
Nombre del país: Uruguay
Población: 3477000
Superficie (km²): 176215
Continente (América, Europa, Asia, África, Oceanía): america
País agregado correctamente.
```

### Buscar país (opción 3)

```
Ingrese nombre o parte del nombre a buscar: arg

Resultados de la búsqueda:
País: Argentina           | Continente: América    | Población:   45.376.763 hab. | Superficie:  2.780.400 km²
```

### Estadísticas (opción 6)

```
--- ESTADISTICAS ---
Mayor población:    Brasil (213.993.437 hab.)
Menor población:    Alemania (83.149.300 hab.)
Promedio población:  117.027.625,00 hab.
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
|-------|------|-------------|
| `nombre` | texto | Nombre del país |
| `poblacion` | entero | Habitantes |
| `superficie` | entero | km² |
| `continente` | texto | América, Europa, Asia, África u Oceanía |

---

## Cómo subir cambios a la rama `ramaRevision` con token classic

### 1. Crear un Personal Access Token (Classic) en GitHub

1. Ir a **GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**.
2. Generar un token con permiso **`repo`** (acceso completo a repositorios privados/públicos).
3. Copiar el token y guardarlo en un lugar seguro. **No compartirlo ni subirlo al repositorio.**

### 2. Flujo de trabajo recomendado

```bash
# Ir a la carpeta del proyecto
cd "ruta/a/Integrador"

# Ver en qué rama estás
git branch

# Cambiar a la rama de revisión (si no estás ya en ella)
git checkout ramaRevision

# Ver qué archivos cambiaron
git status

# Agregar los archivos modificados
git add Integrador.py paises.csv README.md Cambios_Integrador.md

# Commit con convención PROY-N
git commit -m "PROY-1: Descripción breve del cambio realizado"

# Push: URL completa con usuario + token, y la rama al final
git push https://USUARIO:TOKEN@github.com/alevanfof/appPaisesIntegradorProgI2026.git ramaRevision
```

> Reemplazar `USUARIO` por tu usuario de GitHub y `TOKEN` por el token classic generado.  
> **En cada push** hay que escribir el comando completo (no se configura `origin` ni se guarda el token en el remoto).

### 3. Convención de commits sugerida

| Prefijo | Uso | Ejemplo |
|---------|-----|---------|
| `PROY-1` | Primera entrega / setup inicial | `PROY-1: Agregar estructura base del proyecto y CSV inicial` |
| `PROY-2` | Funcionalidades del menú | `PROY-2: Implementar filtros por continente y población` |
| `PROY-3` | Validaciones y manejo de errores | `PROY-3: Validar rangos mínimo/máximo en filtros` |
| `PROY-4` | Documentación | `PROY-4: Agregar README con instrucciones de uso` |
| `PROY-5` | Correcciones / revisión final | `PROY-5: Corregir dataset CSV y normalizar continentes` |

**Formato general:**

```
PROY-N: Verbo en infinitivo + qué se hizo
```

Ejemplos:

```bash
git commit -m "PROY-1: Cargar proyecto integrador con menú principal"
git commit -m "PROY-4: Documentar ejecución y estructura del repositorio"
git commit -m "PROY-5: Mejorar validaciones y formato de salida en consola"
```

### 4. Verificar que el push fue exitoso

```bash
git status
git log --oneline -3
```

Si el push fue correcto, Git mostrará las ramas actualizadas sin errores de autenticación.

**Comando de push (siempre el mismo formato):**

```bash
git push https://USUARIO:TOKEN@github.com/alevanfof/appPaisesIntegradorProgI2026.git ramaRevision
```

---

## Checklist de entrega (consigna TPI)

- [ ] Repositorio **público** en GitHub
- [ ] `Integrador.py` ejecutable sin errores
- [ ] `paises.csv` incluido en el repositorio
- [ ] `README.md` completo (integrantes, instrucciones, ejemplos, links)
- [ ] `Informe_TPI_Paises.pdf` con carátula, índice, marco teórico, diagrama de flujo, capturas, conclusiones y bibliografía
- [ ] Video de 10–15 min con ambos integrantes a cámara al inicio
- [ ] Archivo `.zip` con código fuente + PDF del informe

---

## Licencia

Proyecto académico — UTN TUPaD Programación 1.
