from funciones.diccionarios import DiccionarioUsuario

def PedirUsuarioIn():
    usuario = input("Bienvenido, Cual es tu usuario? ")
    return usuario

def ValidarUsuario():
    intentos = 5
    DiccUsuarios = DiccionarioUsuario()
    
    while intentos > 0:
        
        usuario = PedirUsuarioIn()
        
        if usuario in DiccUsuarios:
            
            print("usuario correcto")
            return usuario
              
        else:
            intentos -=1
            print("Usuario incorrecto, intente de nuevo, quedan", intentos,"intentos")
            
            if intentos == 0:
                print("Sin intentos posibles")
                return False
               
def PedirContraseñaIN(usuario):
    print("Bienvendio", usuario)
    contraseña = input("Ingresa tu contraseña: ")
    return contraseña
        
def ValidarContraseña(usuario):
    
    intentos = 5
    DiccContraseña = DiccionarioUsuario()
    
    while intentos > 0:
        
        c = PedirContraseñaIN(usuario)
         
        if DiccContraseña[usuario] == c:
            print("Bienvenido")
            return c
        
        else:
            
            intentos -= 1

            print("Contraseña incorrecta te quedan", intentos, "intentos disponibles")
            
            if intentos == 0:
                print("Sin intentos disponibles, intente mas tarde")
                return False
            
def mainInicioDeSesion():
    usuario = ValidarUsuario()
    
    if usuario is not False:

        if ValidarContraseña(usuario) is not False:
            return usuario
        else:False
        
    else:
        return False
        
            
        


