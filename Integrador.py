# =====================================
# LISTA DE PAISES
# =====================================

paises = []

def cargar_paises():

    try:

        with open("paises.csv", "r", encoding="utf-8") as archivo:

            next(archivo)

            for linea in archivo:

                datos = linea.strip().split(",")

                if len(datos) != 4:
                    continue

                pais = {
                    "nombre": datos[0],
                    "poblacion": int(datos[1]),
                    "superficie": int(datos[2]),
                    "continente": datos[3]
                }

                paises.append(pais)

        print("CSV cargado correctamente.")

    except FileNotFoundError:

        print("No se encontró paises.csv")


def guardar_pais_csv(pais):

    with open("paises.csv", "a", encoding="utf-8") as archivo:

        archivo.write(
            f"\n{pais['nombre']},"
            f"{pais['poblacion']},"
            f"{pais['superficie']},"
            f"{pais['continente']}"
        )

def guardar_todos_los_paises_csv():

    with open("paises.csv", "w", encoding="utf-8") as archivo:

        archivo.write(
            "nombre,poblacion,superficie,continente\n"
        )

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

    while True:

        texto = input(mensaje).strip()

        if texto == "":
            print("Error: no puede estar vacío.")

        elif not texto.replace(" ", "").isalpha():
            print("Error: solo se permiten letras.")

        else:
            return texto


def validar_numero(mensaje):

    while True:

        try:

            numero = int(input(mensaje))

            if numero < 0:
                print("Error: debe ser positivo.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un número.")


def validar_continente():

    continentes_validos = [
        "america",
        "europa",
        "asia",
        "africa",
        "oceania"
    ]

    while True:

        continente = input(
            "Continente (America, Europa, Asia, Africa, Oceania): "
        ).strip().lower()

        if continente in continentes_validos:
            return continente.capitalize()

        print("Continente inválido.")


# =====================================
# AGREGAR PAIS
# =====================================

def agregar_pais():

    nombre = validar_texto("Nombre del país: ")
    poblacion = validar_numero("Población: ")
    superficie = validar_numero("Superficie (km²): ")
    continente = validar_continente()

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)

    guardar_pais_csv(pais)

    print("País agregado correctamente.")


# =====================================
# ACTUALIZAR PAIS
# =====================================

def actualizar_pais():

    nombre = input(
        "Ingrese el nombre del país a actualizar: "
    ).lower()

    for pais in paises:

        if pais["nombre"].lower() == nombre:

            pais["poblacion"] = validar_numero(
                "Nueva población: "
            )
    
            pais["superficie"] = validar_numero(
                "Nueva superficie: "
            )

            guardar_todos_los_paises_csv()

            print("País actualizado correctamente.")
            return

    print("País no encontrado.")


# =====================================
# BUSCAR PAIS
# =====================================

def buscar_pais():

    texto = input(
        "Ingrese nombre o parte del nombre: "
    ).lower()

    encontrados = False

    for pais in paises:

        if texto in pais["nombre"].lower():

            print("\n", pais)

            encontrados = True

    if not encontrados:
        print("No se encontraron resultados.")


# =====================================
# FILTRAR CONTINENTE
# =====================================

def filtrar_continente():

    continente = validar_continente()

    encontrados = False

    for pais in paises:

        if pais["continente"] == continente:

            print(pais)

            encontrados = True

    if not encontrados:
        print("No hay resultados.")


# =====================================
# FILTRAR POBLACION
# =====================================

def filtrar_poblacion():

    minimo = validar_numero(
        "Población mínima: "
    )

    maximo = validar_numero(
        "Población máxima: "
    )

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:

            print(pais)


# =====================================
# FILTRAR SUPERFICIE
# =====================================

def filtrar_superficie():

    minimo = validar_numero(
        "Superficie mínima: "
    )

    maximo = validar_numero(
        "Superficie máxima: "
    )

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:

            print(pais)


# =====================================
# MENU FILTROS
# =====================================

def menu_filtros():

    print("\n--- FILTROS ---")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")

    opcion = input("Seleccione: ")

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

    print("\n--- ORDENAR ---")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion = input("Seleccione: ")

    orden = input(
        "Ascendente (A) o Descendente (D): "
    ).upper()

    reverse = orden == "D"

    if opcion == "1":

        ordenados = sorted(
            paises,
            key=lambda x: x["nombre"],
            reverse=reverse
        )

    elif opcion == "2":

        ordenados = sorted(
            paises,
            key=lambda x: x["poblacion"],
            reverse=reverse
        )

    elif opcion == "3":

        ordenados = sorted(
            paises,
            key=lambda x: x["superficie"],
            reverse=reverse
        )

    else:
        print("Opción inválida.")
        return

    for pais in ordenados:
        print(pais)


# =====================================
# ESTADISTICAS
# =====================================

def mostrar_estadisticas():

    if len(paises) == 0:

        print("No hay países cargados.")
        return

    mayor = max(
        paises,
        key=lambda x: x["poblacion"]
    )

    menor = min(
        paises,
        key=lambda x: x["poblacion"]
    )

    promedio_poblacion = (
        sum(
            pais["poblacion"]
            for pais in paises
        ) / len(paises)
    )

    promedio_superficie = (
        sum(
            pais["superficie"]
            for pais in paises
        ) / len(paises)
    )

    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n--- ESTADISTICAS ---")

    print(
        f"Mayor población: "
        f"{mayor['nombre']} "
        f"({mayor['poblacion']})"
    )

    print(
        f"Menor población: "
        f"{menor['nombre']} "
        f"({menor['poblacion']})"
    )

    print(
        f"Promedio población: "
        f"{promedio_poblacion:.2f}"
    )

    print(
        f"Promedio superficie: "
        f"{promedio_superficie:.2f}"
    )

    print("\nCantidad por continente:")

    for continente, cantidad in continentes.items():

        print(
            f"{continente}: {cantidad}"
        )


# =====================================
# MENU PRINCIPAL
# =====================================

def mostrar_menu():

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

    cargar_paises()

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        )

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