from datos import CONTINENTES_MAPA


def validar_texto(mensaje):
    """Solicita un texto válido que contenga solo letras y espacios."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: no puede estar vacío.")
        elif not texto.replace(" ", "").isalpha():
            print("Error: solo se permiten letras.")
        else:
            return texto


def validar_numero(mensaje):
    """Solicita un número entero mayor o igual a cero."""
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
    """Solicita un continente válido y devuelve su forma normalizada."""
    while True:
        continente = input("Continente (América, Europa, Asia, África, Oceanía): ").strip().lower()
        if continente in CONTINENTES_MAPA:
            return CONTINENTES_MAPA[continente]
        print("Error: Continente inválido.")
