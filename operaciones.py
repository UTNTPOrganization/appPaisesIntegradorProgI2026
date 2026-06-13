from datos import paises, guardar_pais_csv, guardar_todos_los_paises_csv, CONTINENTES_MAPA
from validaciones import validar_texto, validar_numero, validar_continente


def mostrar_pais_formateado(pais):
    """Muestra un país en formato legible para consola."""
    nombre = pais["nombre"].title()
    continente = pais["continente"]
    poblacion = f"{pais['poblacion']:,}".replace(",", ".")
    superficie = f"{pais['superficie']:,}".replace(",", ".")
    print(f"País: {nombre:<20} | Continente: {continente:<10} | Población: {poblacion:>12} hab. | Superficie: {superficie:>10} km²")


def agregar_pais():
    nombre = validar_texto("Nombre del país: ").title()
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

    paises.append(pais)
    guardar_pais_csv(pais)
    print("País agregado correctamente.")


def actualizar_pais():
    nombre = input("Ingrese el nombre del país a actualizar: ").strip().lower()
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre:
            print("Datos actuales del país:")
            mostrar_pais_formateado(pais)
            pais["poblacion"] = validar_numero("Nueva población: ")
            pais["superficie"] = validar_numero("Nueva superficie: ")
            guardar_todos_los_paises_csv()
            print("País actualizado correctamente.")
            return

    print("Error: País no encontrado.")


def buscar_pais():
    texto = input("Ingrese nombre o parte del nombre a buscar: ").strip().lower()
    if texto == "":
        print("Error: la búsqueda no puede estar vacía.")
        return

    encontrados = False
    print("\nResultados de la búsqueda:")
    for pais in paises:
        if texto in pais["nombre"].lower():
            mostrar_pais_formateado(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron resultados.")


def filtrar_continente():
    continente = validar_continente()
    encontrados = False
    print(f"\nPaíses en {continente}:")
    for pais in paises:
        if pais["continente"] == continente:
            mostrar_pais_formateado(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron países en ese continente.")


def filtrar_poblacion():
    while True:
        minimo = validar_numero("Población mínima: ")
        maximo = validar_numero("Población máxima: ")
        if minimo <= maximo:
            break
        print("Error: La población mínima debe ser menor o igual a la máxima.")

    encontrados = False
    print("\nPaíses en el rango de población:")
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            mostrar_pais_formateado(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron países en ese rango de población.")


def filtrar_superficie():
    while True:
        minimo = validar_numero("Superficie mínima: ")
        maximo = validar_numero("Superficie máxima: ")
        if minimo <= maximo:
            break
        print("Error: La superficie mínima debe ser menor o igual a la máxima.")

    encontrados = False
    print("\nPaíses en el rango de superficie:")
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            mostrar_pais_formateado(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron países en ese rango de superficie.")


def menu_filtros():
    print("\n--- FILTROS ---")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")

    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        filtrar_continente()
    elif opcion == "2":
        filtrar_poblacion()
    elif opcion == "3":
        filtrar_superficie()
    else:
        print("Opción inválida.")


def ordenar_paises():
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

    ordenados = paises.copy()
    cantidad = len(ordenados)
    for i in range(cantidad):
        for j in range(0, cantidad - i - 1):
            intercambiar = False
            if opcion == "1":
                actual = ordenados[j]["nombre"].lower()
                siguiente = ordenados[j + 1]["nombre"].lower()
                intercambiar = actual > siguiente if orden == "A" else actual < siguiente
            elif opcion == "2":
                intercambiar = ordenados[j]["poblacion"] > ordenados[j + 1]["poblacion"] if orden == "A" else ordenados[j]["poblacion"] < ordenados[j + 1]["poblacion"]
            else:
                intercambiar = ordenados[j]["superficie"] > ordenados[j + 1]["superficie"] if orden == "A" else ordenados[j]["superficie"] < ordenados[j + 1]["superficie"]

            if intercambiar:
                ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]

    print("\nPaíses ordenados:")
    for pais in ordenados:
        mostrar_pais_formateado(pais)


def mostrar_estadisticas():
    if len(paises) == 0:
        print("No hay países cargados.")
        return

    mayor = paises[0]
    menor = paises[0]
    total_poblacion = 0
    total_superficie = 0

    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        continentes[continente] = continentes.get(continente, 0) + 1

    pob_mayor = f"{mayor['poblacion']:,}".replace(",", ".")
    pob_menor = f"{menor['poblacion']:,}".replace(",", ".")
    prom_pob = f"{promedio_poblacion:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    prom_sup = f"{promedio_superficie:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    print("\n--- ESTADISTICAS ---")
    print(f"Mayor población:    {mayor['nombre'].title()} ({pob_mayor} hab.)")
    print(f"Menor población:    {menor['nombre'].title()} ({pob_menor} hab.)")
    print(f"Promedio población:  {prom_pob} hab.")
    print(f"Promedio superficie: {prom_sup} km²")

    lista_continentes = sorted(continentes)
    print("\nCantidad por continente:")
    for continente in lista_continentes:
        print(f"- {continente}: {continentes[continente]}")
