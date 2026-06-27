from funciones.menus import MostrarOpciones
from funciones.validaciones import ValidarQueSeaNum , ValidarNumPositivo

def PedirUsuarioR():
    usuario = input("Con que nombre de usuario se desea registrar? ")
    return usuario

def PedirContraseña(usuario):
    contraseña = input("Que contraseña desea? ")
    
    UsuarioContraseña = f"{usuario}:{contraseña}"
    return UsuarioContraseña

def GuardarUsuarioContraseñaDicc(UsuarioContraseña):
    with open ("datos/Usuarios.txt", "a")as archivo:
        archivo.write(UsuarioContraseña + "\n")
        
def PedirAUsuarioDinero(usuario):
    op = 5
    while op > 0:
        dinero = ValidarQueSeaNum()
        
        if dinero is None:
            op -= 1
            print("Intente de nuevo")
            print("Ingrese un numero")
            continue
        
        if ValidarNumPositivo(dinero) == False:
            op -= 1
            print("Intente de nuevo")
            print("Ingrese un numero positivo")
            continue
        
        if dinero is not None:
            DineroUsuario = f"{usuario}:{dinero}"
            print("Has registrado", dinero ,"pesos")
            return DineroUsuario
        else:
            op -= 1
            print("Intente de nuevo")       
    print("Demasiados intentos")
    return None

def GuardarDineroUsuarioDicc(DineroUsuario):
        with open ("datos/Dinero.txt", "a")as archivo:
            archivo.write(DineroUsuario + "\n")
            
def mainRegistro():    
    ##Registro

    usuario = PedirUsuarioR()
    UsuarioContraseña = PedirContraseña(usuario)
    DineroUsuario = PedirAUsuarioDinero(usuario)
    
    if DineroUsuario is not None:
        GuardarDineroUsuarioDicc(DineroUsuario)
        GuardarUsuarioContraseñaDicc(UsuarioContraseña)
        print("Registro exitoso")
    else:
        print("Fallo al ingresar algun dato")

    