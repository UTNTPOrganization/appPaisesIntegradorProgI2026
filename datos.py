import os
import csv

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

ARCHIVO_PAISES = "paises.csv"

paises = []


def _normalizar_continente(valor):
    valor_limpio = valor.strip().lower()
    if valor_limpio in CONTINENTES_MAPA:
        return CONTINENTES_MAPA[valor_limpio]
    return valor_limpio.capitalize()


def cargar_paises():
    """Carga los países desde el archivo CSV en la lista global `paises`."""
    paises.clear()

    if not os.path.exists(ARCHIVO_PAISES):
        print("No se encontró paises.csv. Se creará un archivo nuevo con el encabezado.")
        with open(ARCHIVO_PAISES, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")
        return

    with open(ARCHIVO_PAISES, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)

        for fila in lector:
            if len(fila) != 4:
                continue

            nombre, poblacion, superficie, continente = [dato.strip() for dato in fila]
            try:
                pais = {
                    "nombre": nombre,
                    "poblacion": int(poblacion),
                    "superficie": int(superficie),
                    "continente": _normalizar_continente(continente)
                }
                paises.append(pais)
            except ValueError:
                continue

    print("CSV cargado correctamente.")


def guardar_pais_csv(pais):
    """Agrega un país nuevo al final del archivo CSV."""
    with open(ARCHIVO_PAISES, "a", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([pais["nombre"], pais["poblacion"], pais["superficie"], pais["continente"]])


def guardar_todos_los_paises_csv():
    """Sobrescribe el archivo CSV con la lista de países en memoria."""
    with open(ARCHIVO_PAISES, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
        for pais in paises:
            escritor.writerow([pais["nombre"], pais["poblacion"], pais["superficie"], pais["continente"]])
