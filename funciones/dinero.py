from funciones.diccionarios import DiccionarioDinero
from funciones.validaciones import ValidarQueSeaNum , ValidarNumPositivo
from funciones.menus import OpcionesPrincipalesDinero

def DecisionPrincipalDinero():
    Desicion = int(input ("Que quieres hacer? "))
    
    if Desicion == 1:
        return 1
        
    elif Desicion == 2:
        return 2
    
    elif Desicion == 3:
        print("Sailendo del sistema...")
        
def Retiro(usuario):
    
    op = 5
    DiccDinero = DiccionarioDinero()
    DineroUsuario = int(DiccDinero[usuario])
      
    while op > 0:
        
        cantidad = ValidarQueSeaNum() 
        
        if cantidad is None:
            op -= 1
            print("Te quedan", op ,"intentos")
            continue
        
        if ValidarNumPositivo(cantidad) == False:
            op -= 1
            print("Te quedan", op , "intentos")
            continue       

        NuevoDinero = OperacionRetiro(cantidad , DineroUsuario)

        if NuevoDinero is not None:
            return NuevoDinero
        else:
            op -= 1
            print("Te quedan", op ,"intentos")
    
    print("Demasiados intentos, vuelva mas tarde")
    return None

def OperacionRetiro(cantidad , DineroUsuario):
    if cantidad <= DineroUsuario: 
        
        NuevoDinero = DineroUsuario - cantidad
        print("Tu nuevo saldo es de", NuevoDinero , "pesos") 
        return NuevoDinero

    elif cantidad > DineroUsuario:
        
        print("Cantidad no disponible intente de nuevo")
        print("La cantidad disponible a retirar es de", DineroUsuario , "pesos")
        return None

def GuardarNuevoDinero( NuevoDinero , usuario ):
    DiccDinero = DiccionarioDinero()
    DiccDinero[usuario] = NuevoDinero
    with open ("datos/Dinero.txt", "w")as archivo:
        for usuario in DiccDinero:
            DineroActualizado = f"{usuario}:{DiccDinero[usuario]}\n"
            archivo.write(DineroActualizado)

def Deposito(usuario):
    intentos = 5
    DiccDinero = DiccionarioDinero()
    DineroUsuario = DiccDinero[usuario]
    
    print('Su dinero en cueta es de:', DineroUsuario , 'pesos')

    while  intentos > 0:
        cantidad = ValidarQueSeaNum()
        
        if cantidad is None:
            intentos -=1
            print("Ingresa un valor valido")
            continue
        
        if ValidarNumPositivo() == False:
            intentos -=1
            print("No se pueden ingresar numeros negativos")
            print("Ingrese un valor valido")
            continue

        NuevoDinero = cantidad + int(DineroUsuario)

        if NuevoDinero is not None:
            
            print('Su nuevo saldo es de', NuevoDinero , "pesos")
            return NuevoDinero
        else:
            intentos -=1
            print("Cantidad no disponible a retirar")
            
    print("Demasiados intentos vuelva mas tarde")
    return None
    
def mainRetiro(usuario):
    NuevoDinero = Retiro(usuario)
    if NuevoDinero is not None:
        GuardarNuevoDinero(NuevoDinero , usuario)

    else:
        print("Fallo inesperado, intente mas tarde")
    
def mainDeposito(usuario):
    NuevoDinero = Deposito(usuario)
    
    if NuevoDinero is not None:
        GuardarNuevoDinero(NuevoDinero , usuario)

    else:
        print("Fallo insesperado, intente mas tarde")

def mainDinero(usuario):
    
    
    OpcionesPrincipalesDinero()
    r = DecisionPrincipalDinero()
    
    if r == 1:
        mainRetiro(usuario)
        
    elif r == 2:
        mainDeposito(usuario)
    
        