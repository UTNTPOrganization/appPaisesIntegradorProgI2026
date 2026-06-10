# =====================================
# GESTIÓN DE PAÍSES - TPI Programación 1
# Sistema de consola: carga CSV, altas, búsquedas, filtros, orden y estadísticas
# =====================================
# CONSTANTES Y LISTA DE PAISES
# =====================================

# Mapeo de variantes (con/sin tilde, minúsculas) al nombre oficial del continente
CONTINENTES_MAPA = {
    "america": "América",
    "américa": "América",
    "europa": "Europa",
    "asia": "Asia",
    "africa": "África",
    "áfrica": "África",
    "oceania": "Oceanía",
    "oceanía": "Oceanía"
}

# Lista global en memoria: cada elemento es un diccionario con los datos de un país
paises = []

def mostrar_pais_formateado(pais):
    """Muestra los datos de un país en un formato legible en consola.
    
    Parámetros:
    pais (dict): Diccionario que representa un país.
    """
    nombre = pais["nombre"].title()
    continente = pais["continente"]
    # Separador de miles con punto (formato local): Python usa coma por defecto en :, 
    poblacion = f"{pais['poblacion']:,}".replace(",", ".")
    superficie = f"{pais['superficie']:,}".replace(",", ".")
    print(f"País: {nombre:<20} | Continente: {continente:<10} | Población: {poblacion:>12} hab. | Superficie: {superficie:>10} km²")


def cargar_paises():
    """Carga los países desde el archivo CSV.
    Si el archivo no existe, lo crea con el encabezado correcto usando operaciones básicas.
    Si el archivo tiene líneas mal formadas o valores inválidos, las ignora.
    """
    try:
        with open("paises.csv", "r", encoding="utf-8") as archivo:
            next(archivo)  # Salta la fila de encabezado (nombre,poblacion,superficie,continente)
            for linea in archivo:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue  # Ignora líneas vacías
                datos = linea_limpia.split(",")
                if len(datos) != 4:
                    continue  # Ignora filas con cantidad incorrecta de columnas
                try:
                    continente_raw = datos[3].strip().lower()
                    # Si el continente no está en el mapa, se capitaliza la primera letra
                    continente_normalizado = CONTINENTES_MAPA.get(continente_raw, continente_raw.capitalize())
                    
                    pais = {
                        "nombre": datos[0].strip(),
                        "poblacion": int(datos[1].strip()),
                        "superficie": int(datos[2].strip()),
                        "continente": continente_normalizado
                    }
                    paises.append(pais)
                except ValueError:
                    # Población o superficie no numéricas: se omite la fila sin detener el programa
                    continue
        print("CSV cargado correctamente.")
    except FileNotFoundError:
        print("No se encontró paises.csv. Se creará un archivo nuevo con el encabezado.")
        try:
            # Crea el CSV vacío para que futuras altas puedan usar modo append
            with open("paises.csv", "w", encoding="utf-8") as archivo:
                archivo.write("nombre,poblacion,superficie,continente\n")
        except IOError:
            print("Error al intentar crear el archivo paises.csv")


def guardar_pais_csv(pais):
    """Guarda un único país agregándolo al final del archivo CSV.
    Se usa al agregar un país nuevo (modo append, sin reescribir todo el archivo).
    
    Parámetros:
    pais (dict): El diccionario del país a guardar.
    """
    with open("paises.csv", "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{pais['nombre']},"
            f"{pais['poblacion']},"
            f"{pais['superficie']},"
            f"{pais['continente']}\n"
        )


def guardar_todos_los_paises_csv():
    """Sobrescribe el archivo CSV con la lista de países actual de la memoria.
    Se usa al actualizar datos, ya que un país existente debe modificarse en disco.
    """
    with open("paises.csv", "w", encoding="utf-8") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")
        for pais in paises:
            archivo.write(
                f"{pais['nombre']},"
                f"{pais['poblacion']},"
                f"{pais['superficie']},"
                f"{pais['continente']}\n"
            )


# =====================================
# VALIDACIONES
# =====================================

def validar_texto(mensaje):
    """Solicita una entrada de texto y valida que no esté vacía y contenga solo letras y espacios.
    
    Parámetros:
    mensaje (str): El prompt para el input del usuario.
    
    Retorna:
    str: El texto validado.
    """
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: no puede estar vacío.")
        # Se quitan espacios para validar letras; permite nombres compuestos como "Costa Rica"
        elif not texto.replace(" ", "").isalpha():
            print("Error: solo se permiten letras.")
        else:
            return texto


def validar_numero(mensaje):
    """Solicita un número y valida que sea un entero mayor o igual a cero.
    
    Parámetros:
    mensaje (str): El prompt para el input del usuario.
    
    Retorna:
    int: El número entero positivo validado.
    """
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Error: debe ser positivo.")
            else:
                return numero
        except ValueError:
            # Captura entradas no numéricas (letras, decimales con punto, etc.)
            print("Error: debe ingresar un número.")


def validar_continente():
    """Solicita y valida un continente de una lista preestablecida, admitiendo tildes.
    
    Retorna:
    str: El continente normalizado con tilde y mayúscula inicial.
    """
    while True:
        continente = input(
            "Continente (América, Europa, Asia, África, Oceanía): "
        ).strip().lower()

        # Se valida en minúsculas; se devuelve siempre el nombre estandarizado con tilde
        if continente in CONTINENTES_MAPA:
            return CONTINENTES_MAPA[continente]

        print("Error: Continente inválido.")


# =====================================
# AGREGAR PAIS
# =====================================

def agregar_pais():
    """Agrega un nuevo país a la memoria y lo escribe en el archivo CSV.
    Valida que el país no exista previamente.
    """
    nombre = validar_texto("Nombre del país: ").title()  # Ej: "reino unido" -> "Reino Unido"
    
    # Comparación insensible a mayúsculas para evitar duplicados (ej: "brasil" vs "Brasil")
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"Error: El país '{nombre}' ya está registrado.")
            return

    poblacion = validar_numero("Población: ")
    superficie = validar_numero("Superficie (km²): ")
    continente = validar_continente()

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)       # Persistencia en memoria (lista global)
    guardar_pais_csv(pais)    # Persistencia en disco (append al CSV)
    print("País agregado correctamente.")


# =====================================
# ACTUALIZAR PAIS
# =====================================

def actualizar_pais():
    """Busca un país por nombre y actualiza su población y superficie."""
    nombre = input(
        "Ingrese el nombre del país a actualizar: "
    ).strip().lower()

    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre:
            print("Datos actuales del país:")
            mostrar_pais_formateado(pais)
            
            # Solo se actualizan población y superficie (según consigna)
            pais["poblacion"] = validar_numero("Nueva población: ")
            pais["superficie"] = validar_numero("Nueva superficie: ")

            # Reescribe el CSV completo porque el registro ya existía en el archivo
            guardar_todos_los_paises_csv()
            print("País actualizado correctamente.")
            return

    print("Error: País no encontrado.")


# =====================================
# BUSCAR PAIS
# =====================================

def buscar_pais():
    """Busca países por nombre (coincidencia parcial o exacta) y los muestra."""
    texto = input(
        "Ingrese nombre o parte del nombre a buscar: "
    ).strip().lower()

    if texto == "":
        print("Error: la búsqueda no puede estar vacía.")
        return

    encontrados = False  # Bandera para avisar si hubo coincidencias
    print("\nResultados de la búsqueda:")
    for pais in paises:
        # Coincidencia parcial: "arg" encuentra "Argentina"
        if texto in pais["nombre"].lower():
            mostrar_pais_formateado(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron resultados.")


# =====================================
# FILTRAR CONTINENTE
# =====================================

def filtrar_continente():
    """Filtra y muestra los países de un continente seleccionado."""
    continente = validar_continente()
    encontrados = False
    print(f"\nPaíses en {continente}:")
    for pais in paises:
        # Comparación exacta: el continente ya está normalizado al cargar/ingresar
        if pais["continente"] == continente:
            mostrar_pais_formateado(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron países en ese continente.")


# =====================================
# FILTRAR POBLACION
# =====================================

def filtrar_poblacion():
    """Filtra y muestra los países que estén dentro del rango de población dado."""
    # Repite la carga del rango hasta que mínimo <= máximo
    while True:
        minimo = validar_numero("Población mínima: ")
        maximo = validar_numero("Población máxima: ")
        if minimo <= maximo:
            break
        print("Error: La población mínima debe ser menor o igual a la máxima.")

    encontrados = False
    print("\nPaíses en el rango de población:")
    for pais in paises:
        # Rango inclusivo: incluye países en los extremos minimo y maximo
        if minimo <= pais["poblacion"] <= maximo:
            mostrar_pais_formateado(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron países en ese rango de población.")


# =====================================
# FILTRAR SUPERFICIE
# =====================================

def filtrar_superficie():
    """Filtra y muestra los países que estén dentro del rango de superficie dado."""
    while True:
        minimo = validar_numero("Superficie mínima: ")
        maximo = validar_numero("Superficie máxima: ")
        if minimo <= maximo:
            break
        print("Error: La superficie mínima debe ser menor o igual a la máxima.")

    encontrados = False
    print("\nPaíses en el rango de superficie:")
    for pais in paises:
        # Rango inclusivo en km²
        if minimo <= pais["superficie"] <= maximo:
            mostrar_pais_formateado(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron países en ese rango de superficie.")


# =====================================
# MENU FILTROS
# =====================================

def menu_filtros():
    """Muestra el menú secundario de filtros de países y ejecuta la opción elegida."""
    print("\n--- FILTROS ---")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")

    opcion = input("Seleccione una opción: ").strip()

    # Despacha al filtro correspondiente según la opción del submenú
    if opcion == "1":
        filtrar_continente()
    elif opcion == "2":
        filtrar_poblacion()
    elif opcion == "3":
        filtrar_superficie()
    else:
        print("Opción inválida.")


# =====================================
# ORDENAR
# =====================================

def ordenar_paises():
    """Ordena los países por nombre, población o superficie (ascendente o descendente) y los muestra."""
    print("\n--- ORDENAR ---")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Seleccione criterio: ").strip()
    if opcion not in ["1", "2", "3"]:
        print("Opción inválida.")
        return

    while True:
        orden = input("Ascendente (A) o Descendente (D): ").strip().upper()
        if orden in ["A", "D"]:
            break
        print("Error: Ingrese 'A' o 'D'.")

    reverse = (orden == "D")  # True = descendente, False = ascendente

    # Se define la clave de orden según el criterio elegido
    if opcion == "1":
        clave = lambda x: x["nombre"].lower()  # Alfabético sin distinguir mayúsculas
    elif opcion == "2":
        clave = lambda x: x["poblacion"]
    else:
        clave = lambda x: x["superficie"]

    # sorted() no modifica la lista original; devuelve una copia ordenada
    ordenados = sorted(paises, key=clave, reverse=reverse)

    print("\nPaíses ordenados:")
    for pais in ordenados:
        mostrar_pais_formateado(pais)


# =====================================
# ESTADISTICAS
# =====================================

def mostrar_estadisticas():
    """Calcula y muestra estadísticas como promedios y conteos sobre los países cargados."""
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    # País con mayor y menor población del dataset cargado
    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])

    promedio_poblacion = sum(pais["poblacion"] for pais in paises) / len(paises)
    promedio_superficie = sum(pais["superficie"] for pais in paises) / len(paises)

    # Conteo de países por continente usando un diccionario auxiliar
    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        continentes[continente] = continentes.get(continente, 0) + 1

    print("\n--- ESTADISTICAS ---")

    # Enteros: separador de miles con punto
    pob_mayor = f"{mayor['poblacion']:,}".replace(",", ".")
    pob_menor = f"{menor['poblacion']:,}".replace(",", ".")
    # Decimales: coma como separador decimal y punto como separador de miles
    prom_pob = f"{promedio_poblacion:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    prom_sup = f"{promedio_superficie:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    print(f"Mayor población:    {mayor['nombre'].title()} ({pob_mayor} hab.)")
    print(f"Menor población:    {menor['nombre'].title()} ({pob_menor} hab.)")
    print(f"Promedio población:  {prom_pob} hab.")
    print(f"Promedio superficie: {prom_sup} km²")

    print("\nCantidad por continente:")
    for continente, cantidad in sorted(continentes.items()):
        print(f"- {continente}: {cantidad}")


# =====================================
# MENU PRINCIPAL
# =====================================

def mostrar_menu():
    """Muestra el menú de opciones principal del sistema en la consola."""
    print("\n====================")
    print("GESTION DE PAISES")
    print("====================")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Estadísticas")
    print("0. Salir")


# =====================================
# PROGRAMA PRINCIPAL
# =====================================

if __name__ == "__main__":

    # Al iniciar, se leen los países del CSV a la lista global en memoria
    cargar_paises()

    # Bucle principal: el menú se repite hasta que el usuario elige salir (0)
    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()  # strip() evita errores por espacios alrededor del número

        if opcion == "1":
            agregar_pais()

        elif opcion == "2":
            actualizar_pais()

        elif opcion == "3":
            buscar_pais()

        elif opcion == "4":
            menu_filtros()

        elif opcion == "5":
            ordenar_paises()

        elif opcion == "6":
            mostrar_estadisticas()

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")