from Persona import Persona
import os

class main():
    while True:
        print("\n")
        print("Seleccione una de las siguientes opciones:")
        print("1.- Registrar prestamo")
        print("2.- Mostrar prestamos")
        print("3.- Modificar prestamo")
        print("4.- Eliminar prestamo")
        print("5.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:

            os.system("cls")
            print("Registro de prestamos\n")
            id = int(input("Ingrese id: "))
            nombre = input("Ingrese el nombre: " )
            correo = input("Ingrese el correo: " )
            balon = int(input("Balones: " ))
            porteria = int(input("Porterias: " ))
            valla = int(input("Vallas: "))

            Persona.registrarPrestamo(id, nombre, correo, balon, porteria, valla)

        elif opcion == 2:

            os.system("cls")
            print("Listado de prestamos\n")
            Persona.listadoPrestamos()

        elif opcion == 3:
            os.system("cls")
            print("Modificar prestamo\n")
            id = int(input("Ingrese el id a modificar: " ))
            Persona.modificarPrestamo(id)

        elif opcion == 4:

            os.system("cls")
            print("Eliminar prestamo\n")
            id = int(input("Ingrese el id a eliminar: " ))
            Persona.eliminarPrestamo(id)

        elif opcion == 5:

            os.system("cls")
            Persona.salir()
            
if __name__ == '__main__':
    main();
