print ("login del programa")
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
        break
    else:
        print("Usuario o contraseña incorrectos. Inténtalo de nuevo.")      
    
