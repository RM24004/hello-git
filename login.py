print ("login del programa version 2.2")
while True:
    print("ingrese su usuario")
    usuario = input()   
    print("ingrese su contraseña")
    contraseña = input()    
    if usuario == "admin" and contraseña == "admin123":
        print("Bienvenido, " + usuario + "!")
        print("Has iniciado sesión correctamente.")
        print("Ahora puedes acceder a las funciones del programa.")
        print("El progrma esta en desarrollo, por lo que no hay funciones disponibles por el momento.")
        print("Menu de funciones:")
        print("1. Función 1")
        print("2. Función 2")   
        print("3. Función 3")
        print("4. Salir")
        print("Selecciona una opción:")
        seleccion = input()
        if seleccion == "1":
            print("Has seleccionado la Función 1.")
            print("Esta función aún no está disponible. ¡Próximamente!")
            # Aquí puedes agregar el código para la Función 1
        elif seleccion == "2":
            print("Has seleccionado la Función 2.")
            print("Esta función aún no está disponible. ¡Próximamente!")
            # Aquí puedes agregar el código para la Función 2
        elif seleccion == "3":
            print("Has seleccionado la Función 3.")
            # Aquí puedes agregar el código para la Función 3
            print("Esta función aún no está disponible. ¡Próximamente!")
        elif seleccion == "4":
            print(" Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Usuario o contraseña incorrectos. Inténtalo de nuevo.")      
    
