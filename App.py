# ================================
# app.py
# Programa principal
# ===============================

from Cliente_Manager import (
    ensure_storage,
    create_new_client,
    add_service_to_existing_client,
    view_client_file,
    list_clients,
    find_client
)



# --------------------------------
# Función: mostrar menú
# Muestra las opciones disponibles para el usuario
# --------------------------------

def menu():
    print("====================================")
    print(" SKY v2.0 - Gestion de Clientes ")
    print("====================================")
    print("1) Registrar cliente NUEVO")
    print("2) Cliente RECURRENTE (agregar servicio)")
    print("3) Ver expediente de un cliente")
    print("4) Listar clientes")
    print("5) Buscar cliente por nombre")
    print("6) Salir")
    print("")

# --------------------------------
# Función principal del programa
# Fucion principal qye controla el flujo del programa
# Mostrando el menú y ejecutando las funciones correspondientes según la opción seleccionada por el usuario
# --------------------------------

def main():
    ensure_storage()

    while True:
        menu()
        opt = input("Selecciona una opcion: ").strip()

        if opt == "1":
            create_new_client()
        elif opt == "2":
            add_service_to_existing_client()
        elif opt == "3":
            view_client_file()
        elif opt == "4":
            list_clients()
        elif opt == "5":
            find_client()
        elif opt == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no válida.")

        input("\nPresiona ENTER para continuar...")
        print("\n" * 2)


if __name__ == "__main__":
    main()