from funciones.DiccJson import leerDicc
import json

def PedirU():
    u = input("Que usuario desea? ")
    return u

def PedirD():
    i = 5
    while i > 0:

        try:
            d = int(input("Cuanto dinero desea ingresar?"))
            return d
        
        except ValueError:
            i -= 1
            print("Error: Se debe de ingresar un numero")
            print("Intente de nuevo")
            if i == 0:
                print("Sin intentos posibles")
                return None

def PedirC():    
    c = input( "Ingrese una contraseña: ")
    return c


def GuardarDatosJson(u , d , c ):
    try:
        DU = leerDicc() 
    except FileNotFoundError:   
        DU = {}

    DU[u]={
        "dinero":d,
        "Contraseña": c
    }

    with open ("mi_base_datos.json", "w") as archivo:
        json.dump(DU, archivo, indent=4 )
    
def mainRegistroJson():
    u = PedirU()
    d = PedirD()
    if d is not None:
        c = PedirC()
        GuardarDatosJson(u , d , c )
        return u
    else:
        print("No se a podido crear el usuario vuelva mas tarde")