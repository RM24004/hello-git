print ("login del programa")
while True:
    print("ingrese su usuario")
    usuario = input()   
    print("ingrese su contraseña")
    contraseña = input()    
    if usuario == "admin" and contraseña == "admin123":
        print("Bienvenido, " + usuario + "!")
        break
    else:
        print("Usuario o contraseña incorrectos. Inténtalo de nuevo.")      
    
