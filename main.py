from operaciones import agregar_pais, actualizar_pais, buscar_pais, menu_filtros, ordenar_paises, mostrar_estadisticas
from datos import cargar_paises


def mostrar_menu():
    """Muestra el menú principal del programa."""
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


if __name__ == "__main__":
    cargar_paises()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

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
